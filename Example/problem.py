import sys
import shlex
import os

parser = None


def debug_redirect():
    global parser
    if os.environ.has_key('PYCHARM_HOSTED'):
        sys.stdin = open("input1.txt", 'r')
        #sys.stdout = open("output1.txt", 'wc')
    parser = shlex.shlex(sys.stdin)
    parser.whitespace_split = True


def parse_inputs():
    pass


def main():
    debug_redirect()
    parse_inputs()




if "__main__" == __name__:
    main()