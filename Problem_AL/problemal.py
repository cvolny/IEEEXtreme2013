import itertools
import os
import sys

def powerset_generator(i):
    for subset in itertools.chain.from_iterable(itertools.combinations(i, r) for r in range(len(i)+1)):
        yield subset


def palgen(word):
    for p in powerset_generator(range(len(word))):
        if p:
            w = [word[i] for i in p]
            if w == w[::-1]:
                yield p


def main():
    if os.environ.has_key('PYCHARM_HOSTED'):
        sys.stdin = open("input3.txt", 'r')
    N = int(raw_input())
    M = 12345678
    line = raw_input()[:N]
    i = 0
    for p in palgen(line):
        #print i
        i = (i + 1) % M
        #if i > M:
            #print >> sys.stderr, "Rolling..."
        #    i %= M
    print i

if "__main__" == __name__:
    main()
    #print >> sys.stderr, timeit.Timer(main).repeat(10,1)