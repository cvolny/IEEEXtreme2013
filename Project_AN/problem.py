import sys
import shlex
import os

parser = None
ctext = ""
wdict = []
cdict = {}
dictlen = -1
hits = {}


def guess_lengths(x):
#>>> x = "qwertyui"
#>>> chunks, chunk_size = len(x), len(x)/4
#>>> [ x[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
    blocks = [ctext[i:x] for i in range(0, len(ctext), x)]
    print blocks


def modchar(c, offset):
    ic = ord(c) - ord('A')
    ic += offset
    ic %= 26
    return chr(ic + ord('A'))


def debug_redirect():
    global parser, wdict, cdict, dictlen
    if os.environ.has_key('PYCHARM_HOSTED'):
        sys.stdin = open("input1.txt", 'r')
        #sys.stdout = open("output1.txt", 'wc')
    parser = shlex.shlex(sys.stdin)
    parser.whitespace_split = True

    ctext = raw_input()
    raw_input()
    dictlen = int(raw_input())
    for j in range(26):
        cdict[j] = []
    for i in range(dictlen):
        word = parser.get_token()
        wdict.append(word)
        for j in range(26):
            cdict[j].append([modchar(c, j) for c in word])



def main():
    debug_redirect()
    guess_lengths(5)



if "__main__" == __name__:
    main()