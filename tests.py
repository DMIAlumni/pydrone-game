import sys
import fpformat
from StringIO import StringIO
from math import sqrt, fsum
from sys import argv
import drone_game

script, size = argv
MATRIX_SIZE = int(size)

def tests(size):
    results = []
    j = 0
    counter = 1
    test_size = size
    print "------------------------------------------------"
    if raw_input("Test completi o ridotti [C/r]? ") == "r":
        j = 2
        test_size -= 2
    print "------------------------------------------------"
    print "Eseguo i test..."
    for end_x in range(j, test_size):
        for end_y in range(j, test_size):
            i = (counter * 100 / (test_size - j)**4)
            sys.stdout.write("\r%d%%" %i)
            sys.stdout.flush()
            for start_x in range(j, test_size):
                for start_y in range(j, test_size):
                    counter += 1
                    actualstdout = sys.stdout
                    sys.stdout = StringIO()
                    results.append(drone_game.main(size, end_x, end_y, start_x, start_y))
                    sys.stdout = actualstdout
    print
    return results

def save_results(results, size):
    print "Saving the results in test_" + str(size) + ".txt"
    file = open("test_" + str(size) + ".txt", 'w')
    for ris in results:
        print>>file, ris

def stats(results):
    sum = 0
    notfound = 0
    worst = 0
    for ris in results:
        sum += ris
        if ris > worst:
            worst = ris
        if ris == 0:
            notfound += 1

    avg = sum / len(results)
    varianza = fsum([(x - avg)**2 for x in results]) / len(results)
    scarto = fpformat.fix(sqrt(varianza), 2)
    print "-------------------------------------------------"
    print "Statistiche:"
    print "Numero di test eseguiti:\t\t " + str(len(results))
    print "Carburante esaurito:\t\t\t " + str(notfound)
    print "Caso peggiore:\t\t\t\t " + str(worst)
    print "Media aritmetica dei risultati:\t\t " + str(avg)
    print "Scarto quadratico medio:\t\t " + str(scarto)


results = tests(MATRIX_SIZE)
if not raw_input("Vuoi salvare i risultati? [S/n]") == "n":
    save_results(results, MATRIX_SIZE)
stats(results)

