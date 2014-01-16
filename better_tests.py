import sys
import fpformat
from StringIO import StringIO
from math import sqrt, fsum
from sys import argv
import drone_game
import argparse

parser = argparse.ArgumentParser(description='Testing and comparing algorithms')
parser.add_argument('-s', metavar='Size', default=0, type=int, required=True, action='store', help='Size of the matrix representing the world')
parser.add_argument('-r', default=False, action='store_true', help='Exclude the borders of the matrix from the possible final point')
parser.add_argument('--save-output', metavar="Output-file", action='store', help='Save the results in the specified file')
parser.add_argument('--input-file', metavar="Input-file", action='store', help='Make the calculations using a previously created file for non optimal algorithm')
args = vars(parser.parse_args())

RIDOTTI = args['r']
MATRIX_SIZE = args['s']
OUTPUTFILE = args['save_output']
INPUTFILE = args['input_file']

def tests(size, knowledge=False, reduxed=False):
    results = []
    j = 0
    counter = 1
    test_size = size
    if reduxed:
        j = 2
        test_size -= 2
    print "--------------------------------------------------------------------------------------"
    print "Eseguo i test..."
    for end_x in range(j, test_size):
        for end_y in range(j, test_size):
            for start_x in range(j, test_size):
                for start_y in range(j, test_size):
                    # Mostro la percentuale di avanzamento dello script
                    i = (counter * 100 / (test_size - j)**4)
                    sys.stdout.write("\r%d%%" %i)
                    sys.stdout.flush()
                    counter += 1
                    # Sopprimo lo stdout mentre eseguo lo script
                    actualstdout = sys.stdout
                    sys.stdout = StringIO()
                    results.append(drone_game.main(size, end_x, end_y, start_x, start_y, knowledge))
                    sys.stdout = actualstdout
    print
    return results

def save_results(results, name):
    size = len(results)
    print "Saving results in " + str(name)
    file = open(name, 'w')
    for ris in results:
        print>>file, ris
    file.close()


def stats(results):
    # Average, fails and worst case
    sum = 0
    not_found = 0
    worst = 0
    for ris in results:
        sum += ris
        if ris > worst:
            worst = ris
        if ris == 0:
            not_found += 1
    # Calculate the parameters
    size = len(results)
    avg = sum / size
    varianza = fsum([(x - avg)**2 for x in results]) / size
    scarto = fpformat.fix(sqrt(varianza), 2)
    valori = set(results)
    frequenze = dict(zip(valori, [results.count(v) for v in valori]))
    sorted_frequenze = sorted(frequenze, key=frequenze.get, reverse=True)
    sorted_frequenze = sorted_frequenze[:10]
    return not_found, worst, avg, scarto, frequenze, sorted_frequenze

def make_test():

    optimal_file = "OPTIMAL-" + str(MATRIX_SIZE) + ".txt"
    try:
        f = open(optimal_file, 'r')
        optimal = [int(x) for x in f.readlines()]
        f.close()
        print "--------------------------------------------------------------------------------------"
        print "Trovato file con i risultati dell'algoritmo ottimale!\nNon verranno eseguiti nuovamente i test!"
        print "(se vuoi rieseguire i test, cancella il file " + optimal_file + ")"
    except:
        optimal = tests(MATRIX_SIZE, knowledge=True, reduxed=RIDOTTI)
        save_results(optimal, optimal_file)
    if INPUTFILE:
        try:
            f = open(INPUTFILE, 'r')
            results = [int(x) for x in f.readlines()]
            f.close()
            print "--------------------------------------------------------------------------------------"
            print "Calcolo le statistiche dal file " + INPUTFILE
        except:
            print "--------------------------------------------------------------------------------------"
            print "File non trovato! Rieseguo i test"
            results = tests(MATRIX_SIZE, knowledge=False, reduxed=RIDOTTI)
    else:
        results = tests(MATRIX_SIZE, knowledge=False, reduxed=RIDOTTI)
    if OUTPUTFILE:
        save_results(results, OUTPUTFILE)

    not_found, worst, avg, scarto, frequenze, sorted_frequenze = stats(results)
    opt_not_found, opt_worst, opt_avg, opt_scarto, opt_frequenze, opt_sorted_frequenze = stats(optimal)
    ratio_avg = fpformat.fix(float(avg) / float(opt_avg), 2)
    ratio_worst = fpformat.fix(float(worst) / float(opt_worst), 2)
    ratio_scarto = fpformat.fix((float(scarto) / float(opt_scarto)), 2)

    print "--------------------------------------------------------------------------------------"
    print "Statistiche:\t\t\t\tOffline\t\tOnline\t\tRapporto"
    print "Numero di test eseguiti:\t\t " + str(len(results)) + "\t\t" + str(len(optimal))
    print "Carburante esaurito:\t\t\t " + str(not_found) + "\t\t" + str(opt_not_found)
    print "Caso peggiore:\t\t\t\t " + str(worst) + "\t\t" + str(opt_worst) + "\t\t" + str(ratio_worst)
    print "Media aritmetica dei risultati:\t\t " + str(avg) + "\t\t" + str(opt_avg) + "\t\t" + str(ratio_avg)
    print "Scarto quadratico medio:\t\t " + str(scarto) + "\t\t" + str(opt_scarto) + "\t\t" + str(ratio_scarto)
    print "I dieci risultati piu' riscontrati nell'algoritmo non ottimale:"
    print "Costo:\tOttenuto:\tSotto la media?"
    for el in sorted_frequenze:
        sotto = "media"
        if el < avg:
            sotto = "si"
        elif el > avg:
            sotto = "no"
        print str(el) + "\t" + str(frequenze[el]) + "\t\t" + sotto
#    print "I dieci risultati piu' riscontrati nell'algoritmo ottimale:"
#    print "Costo:\tOttenuto:\tSotto la media?"
#    for el in opt_sorted_frequenze:
#        sotto = "media"
#        if el < opt_avg:
#            sotto = "si"
#        elif el > opt_avg:
#            sotto = "no"
#        print str(el) + "\t" + str(opt_frequenze[el]) + "\t\t" + sotto

make_test()
