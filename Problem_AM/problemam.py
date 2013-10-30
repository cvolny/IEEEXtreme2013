import sys
import shlex
import os
import timeit


def pathfinder(row, col, table, N, M):
    if row == N-1:
        yield [(row, col)]
    else:
        for i in range(max(0, col-1), min(M-1, col+2)):
            for path in pathfinder(row+1, i, table, N, M):
                yield [(row, col)] + path


def cost(path, table):
    return sum([table[r][c] for r, c in path])


def main():
    N, M = 0, 0
    table = None
    if os.environ.has_key('PYCHARM_HOSTED'):
        sys.stdin = open("input2.txt", 'r')
    parser = shlex.shlex(sys.stdin)
    parser.whitespace_split = True

    N = int(parser.get_token())
    M = int(parser.get_token())

    table = [[None]*M for x in range(N)]

    for i in range(N):
        for j in range(M):
            table[i][j] = int(parser.get_token())

    cheapest = None
    cheapcost = sys.maxint

    for col in range(0, M):
        for path in pathfinder(0, col, table, N, M):
            newcost = cost(path, table)
            if newcost < cheapcost:
                cheapest = path
                cheapcost = newcost

    print "Minimum risk path = [%s]" % "][".join(["%d,%d" % x for x in cheapest])
    print "Risks along the path = %d" % cheapcost


if "__main__" == __name__:
    print min(timeit.Timer(main,).repeat(5, 1))
    #main()