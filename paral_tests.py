from sys import argv
import drone_game
from multiprocessing import Process, Queue, Array


def p(q, size, end_x, end_y, start_x, start_y, knowledge):
    q.value =  (drone_game.main(size, end_x, end_y, start_x, start_y, knowledge))

def tests_paral(size, knowledge=False):
    test_size = size - 1
    j = 1
    q = Array('i', 15000)
    for end_x in range(test_size/2 - test_size/4, test_size/2 + test_size/4):
        for end_y in range(test_size/2 - test_size/4, test_size/2 + test_size/4):
            for start_x in range(j, test_size - 1):
                for start_y in range(j, test_size - 1):
                    Process(target=p, args=(q, size, end_x, end_y, start_x, start_y, knowledge)).start()
    return q


def tests(size, knowledge=False):
    results = []
    test_size = size - 1
    j = 1

    for end_x in range(test_size/2 - test_size/4, test_size/2 + test_size/4):
        for end_y in range(test_size/2 - test_size/4, test_size/2 + test_size/4):
            for start_x in range(j, test_size - 1):
                for start_y in range(j, test_size - 1):
                    results.append(drone_game.main(size, end_x, end_y, start_x, start_y, knowledge))

    return results

def main():
    script, MATRIX_SIZE = argv
    print tests_paral(int(MATRIX_SIZE))

if __name__ == "__main__":
    main()