import sys
import shlex
import os


def route_count(n, k):
    print "*", n, k
    if k == 1:
        return 2
    if k == 2:
        return 2*(n-2)
    return n + route_count(n-1, k-2)


def pathfinder(x, y, N, turns, max_turns):
    if turns > max_turns:
        return []





def main():
    M = 1000000007
    if os.environ.has_key('PYCHARM_HOSTED'):
        sys.stdin = open("input1.txt", 'r')
        #sys.stdout = open("output1.txt", 'wc')
    parser = shlex.shlex(sys.stdin)
    parser.whitespace_split = True
    while 1:
        a, b = int(parser.get_token()), int(parser.get_token())
        if a == b == 0:
            break
        print route_count(a, b) % M


if "__main__" == __name__:
    main()