import sys
import shlex
import os

parser = None
n = 0
m = 0
k = 0
t = 0
count = 0
seqs = []
outs = []
answ = []

def debug_redirect():
    global parser
    if os.environ.has_key('PYCHARM_HOSTED'):
        sys.stdin = open("lenovo.input2.txt", 'r')
        sys.stdout = open("lenovo.output2.txt", 'wc')
    parser = shlex.shlex(sys.stdin)
    parser.whitespace_split = True


def parse_inputs():
    global n, m, k, t, seqs, outs

    n = int(parser.get_token())
    for i in range(n):
        token = parser.get_token()
        l = len(token)
        m = max(m, l)
        t += l
        seqs.append(token)

    k = int(parser.get_token())
    for i in range(k):
        outs.append(int(parser.get_token()))


def trim_alignment(alignment):
    l = 0
    for a in alignment:
        l = max(l, len(a.rstrip('-')))
    return [x[:l] for x in alignment]


def permgen(sequence, current, low, total):
    high = total - len(sequence) + current + 1
    for i in xrange(low, high):
        if current == (len(sequence)-1):
            yield (i,)
        else:
            for perm in permgen(sequence, current+1, i, total):
                yield (i,) + tuple(perm)


def aligngen(sequences, current, total):
    for perm in permgen(sequences[current], 0, 0, total):
        if len(set(perm)) == len(sequences[current]):
            if current == (len(sequences)-1):
                yield (perm,)
            else:
                for perms in aligngen(sequences, current+1, total):
                    yield (perm,) + perms


def seqtostr(seq, coords, total, drop):
    seqlst = ['-']*total
    for i in range(len(coords)):
        seqlst[coords[i]] = seq[i]
    for i in range(len(drop)-1,-1,-1):
        if drop[i]:
            del seqlst[i]
    return "".join(seqlst)


def aligntostr(align, total):
    length = len(align)
    result = [None]*length
    drop = [1]*total
    for i in range(total):
        for j in range(length):
            if i in align[j]:
                drop[i] = 0
    for i in range(len(align)):
        result[i] = seqtostr(seqs[i], align[i], total, drop)
    return tuple(result)


def alignment_generator():
    global count, t, seqs
    seen = set()
    count = 0
    for align in aligngen(seqs, 0, t):
        r = aligntostr(align, t)
        if r not in seen:
            seen.add(r)
            answ.append(r)
            count += 1


def alignment_compare(x, y):
    global seqs
    if len(x[0]) < len(y[0]):
        return -1
    elif len(x[0]) > len(y[0]):
        return 1

    return 0


def format_alignment(alignment):
    return "\n".join(alignment)


# TODO: GENERATE, SORT
def main():
    global answ, count
    debug_redirect()
    parse_inputs()

    alignment_generator()
    answ.sort(cmp=alignment_compare)

    print "Possible Alignments: %d" % count
    for out in outs:
        if 0 < out <= len(answ):
            print "Alignment at Position: %d" % (out,)
            print format_alignment(answ[out-1])
        else:
            print "There is no alignment at position: %d" % (out,)


if "__main__" == __name__:
    main()