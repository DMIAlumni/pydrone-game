import sys
import fpformat
from StringIO import StringIO
from math import sqrt, fsum
from sys import argv
import drone_game


def tests(size, knowledge=False):
    results = []
    j = 0
    counter = 1
    test_size = size
    print "------------------------------------------------"
    if raw_input("Test [C]ompleti o [r]idotti? ") == "r":
        j = 2
        test_size -= 2
    print "------------------------------------------------"
    print "Eseguo i test..."
    for end_x in range(j, test_size):
        for end_y in range(j, test_size):
            for start_x in range(j, test_size):
                for start_y in range(j, test_size):
                    i = (counter * 100 / (test_size - j) ** 4)
                    sys.stdout.write("\r%d%%" % i)
                    sys.stdout.flush()
                    counter += 1
                    actualstdout = sys.stdout
                    sys.stdout = StringIO()
                    results.append(drone_game.main(size, end_x, end_y, start_x, start_y, knowledge))
                    sys.stdout = actualstdout
    print
    return results


def save_results(results, size):
    print "Saving the results in test_" + str(size) + ".txt"
    file = open("test_" + str(size) + ".txt", 'w')
    for ris in results:
        print>>file, ris


def first_stats(results):
    sum = 0
    notfound = 0
    worst = 0
    for ris in results:
        sum += ris
        if ris > worst:
            worst = ris
        if ris == 0:
            notfound += 1
    return sum, notfound, worst


def stats(results, optimal=None):
    sum, notfound, worst = first_stats(results)
    avg = sum / len(results)
    varianza = fsum([(x - avg) ** 2 for x in results]) / len(results)
    scarto = fpformat.fix(sqrt(varianza), 2)
    valori = set(results)
    frequenze = dict(zip(valori, [results.count(v) for v in valori]))
    sorted_frequenze = sorted(frequenze, key=frequenze.get, reverse=True)
    sorted_frequenze = sorted_frequenze[:10]
    if optimal:
        opt_sum, opt_nf, opt_worst = first_stats(optimal)
        opt_avg = opt_sum / len(optimal)
        opt_scarto = fpformat.fix(sqrt(fsum([(x - opt_avg) ** 2 for x in optimal]) / len(optimal)), 2)
        ratio_avg = avg / opt_avg
        ratio_worst = worst / opt_worst
        ratio_scarto = fpformat.fix((float(scarto) / float(opt_scarto)), 2)

    print "-------------------------------------------------"
    print "Statistiche:\t\t\t\tOffline\tOnline\tRapporto"
    print "Numero di test eseguiti:\t\t " + str(len(results)) + "\t" + str(len(optimal))
#    print "Carburante esaurito:\t\t\t " + str(notfound)
    print "Caso peggiore:\t\t\t\t " + str(worst) + "\t" + str(opt_worst) + "\t" + str(ratio_worst)
    print "Media aritmetica dei risultati:\t\t " + str(avg) + "\t" + str(opt_avg) + "\t" + str(ratio_avg)
    print "Scarto quadratico medio:\t\t " + str(scarto) + "\t" + str(opt_scarto) + "\t" + str(ratio_scarto)
    print "I dieci risultati piu' riscontrati:"
    print "Costo:\tOttenuto:\tSotto la media?"
    for el in sorted_frequenze:
        sotto = "media"
        if el < avg:
            sotto = "si"
        elif el > avg:
            sotto = "no"
        print str(el) + "\t" + str(frequenze[el]) + "\t\t" + sotto


def stat_from_file(file):
    f = open(file, 'r')
    results = [int(x) for x in f.readlines()]
    f.close()
    stats(results)


script, size = argv
MATRIX_SIZE = int(size)
# ans = raw_input("[E]seguire i test, o [A]nalizzare un file? ")
# if ans == "E" or ans == "e":
results_optimal = tests(MATRIX_SIZE, True)
results = tests(MATRIX_SIZE)
print "-------------------------------------------------"
if not raw_input("Vuoi salvare i risultati? [S/n]") == "n":
    save_results(results, MATRIX_SIZE)
stats(results, results_optimal)
# elif ans == "A" or ans == "a":
#    file = str(raw_input("Nome del file: "))
#    stat_from_file(file)
