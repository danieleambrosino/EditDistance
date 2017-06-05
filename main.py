import file_manager
import test
from timeit import default_timer as timer
from os import system

from sys import version_info
assert version_info[0] == 2 and version_info[1] == 7


def main():
    file_manager.ngram_populate()
    query = raw_input('Insert name: ')
    distance = int(raw_input('Insert max distance: '))

    time = timer()
    edit_result = test.test_edit(query, distance)
    time = timer() - time
    print 'Using simple Edit Distance:', time
    print edit_result, len(edit_result)

    for n in xrange(2, 4):
        time = timer()
        ngram_result = test.test_ngram(query, distance, n)
        time = timer() - time
        print 'Using Edit Distance with %d-grams: %g' % (n, time)
        print ngram_result, len(ngram_result)


if __name__ == '__main__':
    try:
        main()
    finally:
        system('cd res/digrams && rm *')
        system('cd res/trigrams && rm *')
