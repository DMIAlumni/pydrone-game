import curses
import sys
import fpformat
from StringIO import StringIO
from math import sqrt, fsum
import drone_game
import glob


def tests(size, screen, knowledge=False, reduxed=False):
    results = []
    counter = 1
    test_size = size - 1
    j = 1
    prepare_window(screen)
    screen.addstr(2, 2, "Eseguo i test...")

    for end_x in range(test_size / 2 - test_size / 4, test_size / 2 + test_size / 4):
        for end_y in range(test_size / 2 - test_size / 4, test_size / 2 + test_size / 4):
            for start_x in range(j, test_size - 1):
                for start_y in range(j, test_size - 1):
                    # Mostro la percentuale di avanzamento dello script
                    i = (counter * 100) / (((test_size - j - 1) ** 2) * ((test_size / 4) * 2) ** 2)
                    screen.addstr(4, 2, str(i) + "%")
                    screen.refresh()
                    counter += 1
                    results.append(drone_game.main(size, end_x, end_y, start_x, start_y, knowledge))

    return results


def save_results(results, name, screen):
    prepare_window(screen)
    get_param("Saving results in " + str(name), screen, True)
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
    varianza = fsum([(x - avg) ** 2 for x in results]) / size
    scarto = fpformat.fix(sqrt(varianza), 2)
    valori = set(results)
    frequenze = dict(zip(valori, [results.count(v) for v in valori]))
    sorted_frequenze = sorted(frequenze, key=frequenze.get, reverse=True)
    sorted_frequenze = sorted_frequenze[:10]
    return not_found, worst, avg, scarto, frequenze, sorted_frequenze


def prepare_window(screen):
    screen.clear()
    screen.border(0)


def get_matrix_size(screen):
    prepare_window(screen)
    curses.echo()
    curses.nocbreak()
    curses.curs_set(0)
    screen.addstr(2, 2, "Enter matrix size (integer):")
    size = screen.getstr(4, 2, 60)
    try:
        if int(size) > 5:
            return int(size)
        else:
            return get_matrix_size(screen)
    except:
        return get_matrix_size(screen)


def get_file(string, screen, ms):
    x = None
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    files = glob.glob('./*' + str(ms) + '*.txt')
    h = curses.A_REVERSE  # h is the coloring for a highlighted menu option
    n = curses.A_NORMAL  # n is the coloring for a non highlighted menu option
    pos = 0
    old_pos = 1
    while x != ord('\n'):
        cnt = 6
        prepare_window(screen)
        if pos != old_pos:
            old_pos = pos
            screen.addstr(2, 2, string)
            screen.addstr(4, 2, "(suggerimenti: possibili file trovati nella cartella attuale)")
            i = 0
            for file in files:
                style = n if i != pos else h
                screen.addstr(cnt, 2, "%s" % (file), style)
                cnt += 2
                i += 1
            style = n
            style = h if pos == len(files) else n
            screen.addstr(cnt, 2, "%s" % ("Altro file"), style)
            style = h if pos == len(files) + 1 else n
            screen.addstr(cnt + 2, 2, "%s" % ("Nessun file"), style)
            screen.refresh()
        x = screen.getch()

        if x == 258:  # down arrow
            if pos < len(files) + 1:
                pos += 1
            else:
                pos = 0
        elif x == 259:  # up arrow
            if pos > 0:
                pos += -1
            else:
                pos = len(files) + 1

    # return index of the selected item
    if pos == len(files):
        prepare_window(screen)
        curses.echo()
        curses.curs_set(1)
        screen.addstr(2, 2, string)
        file = screen.getstr(4, 2, 60)
        curses.noecho()
        curses.curs_set(0)
    elif pos == len(files) + 1:
        file = ""
    else:
        file = files[pos]
    return file


def get_param(prompt_string, screen, cbreak=False):
    prepare_window(screen)
    curses.echo()
    curses.cbreak() if cbreak else curses.nocbreak()
    curses.curs_set(0)
    screen.addstr(2, 2, prompt_string)
    screen.refresh()
    input = screen.getch()
    return input


def close(screen):
    curses.cbreak()
    curses.noecho()
    a = screen.getch()
    if a == 113:
        curses.nocbreak()
        curses.echo()
        screen.keypad(0)
        curses.endwin()
    else:
        close(screen)


def main(screen):
    MATRIX_SIZE = get_matrix_size(screen)
    optimal_file = "OPTIMAL-" + str(MATRIX_SIZE) + ".txt"
    RIDOTTI = True if get_param("Calcoli ridotti? [s/N]", screen, True) == 115 else False
    INPUTFILE = get_file("File da cui prendere i risultati per i calcoli ('Nessun file' per eseguire i calcoli)", screen, MATRIX_SIZE)
    OUTPUTFILE = get_file("File in cui salvare i risultati ('Nessun file' per non salvare)", screen, MATRIX_SIZE)
    try:
        f = open(optimal_file, 'r')
        optimal = [int(x) for x in f.readlines()]
        f.close()
        get_param("Trovato file con i risultati dell'algoritmo ottimale! (" + optimal_file + ")", screen, True)
    except:
        optimal = tests(MATRIX_SIZE, screen, knowledge=True, reduxed=RIDOTTI)
        save_results(optimal, optimal_file, screen)
    if not INPUTFILE == "":
        try:
            f = open(INPUTFILE, 'r')
            results = [int(x) for x in f.readlines()]
            f.close()
            get_param("Calcolo le statistiche dal file " + INPUTFILE, screen, True)
        except:
            get_param("File non trovato! Rieseguo i test", screen, True)
            results = tests(MATRIX_SIZE, screen, knowledge=False, reduxed=RIDOTTI)
    else:
        results = tests(MATRIX_SIZE, screen, knowledge=False, reduxed=RIDOTTI)
    if OUTPUTFILE:
        save_results(results, OUTPUTFILE, screen)

    not_found, worst, avg, scarto, frequenze, sorted_frequenze = stats(results)
    opt_not_found, opt_worst, opt_avg, opt_scarto, opt_frequenze, opt_sorted_frequenze = stats(optimal)
    ratio_avg = fpformat.fix(float(avg) / float(opt_avg), 2)
    ratio_worst = fpformat.fix(float(worst) / float(opt_worst), 2)
    ratio_scarto = fpformat.fix((float(scarto) / float(opt_scarto)), 2)
    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Statistiche:\t\t\t\tOffline\t\tOnline\t\tRapporto")
    screen.addstr(4, 2, "Numero di test eseguiti:\t\t " + str(len(results)) + "\t\t" + str(len(optimal)))
    screen.addstr(6, 2, "Carburante esaurito:\t\t\t " + str(not_found) + "\t\t" + str(opt_not_found))
    screen.addstr(8, 2, "Caso peggiore:\t\t\t " + str(worst) + "\t\t" + str(opt_worst) + "\t\t" + str(ratio_worst))
    screen.addstr(10, 2, "Media aritmetica dei risultati:\t " + str(avg) + "\t\t" + str(opt_avg) + "\t\t" + str(ratio_avg))
    screen.addstr(12, 2, "Scarto quadratico medio:\t\t " + str(scarto) + "\t\t" + str(opt_scarto) + "\t\t" + str(ratio_scarto))
    screen.addstr(14, 1, "-" * (screen.getmaxyx()[1] - 2))
    screen.addstr(16, 2, "I dieci risultati piu' riscontrati nell'algoritmo non ottimale:")
    screen.addstr(18, 2, "Costo:\tOttenuto:\tSotto la media?")
    cnt = 20
    for el in sorted_frequenze:
        sotto = "media"
        if el < avg:
            sotto = "si"
        elif el > avg:
            sotto = "no"
        screen.addstr(cnt, 2, str(el) + "\t\t" + str(frequenze[el]) + "\t\t" + sotto)
        cnt += 2
    screen.addstr(cnt, 2, "Premere q per uscire")
    close(screen)


if __name__ == '__main__':
    curses.wrapper(main)
