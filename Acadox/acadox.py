import sys
import os
import operator

parser = None


def debug_redirect():
    if os.environ.has_key('PYCHARM_HOSTED'):
        sys.stdin = open("input4.txt", 'r')
    pass


def error_exit():
    print "ERROR"
    sys.exit(0)


def bound(n):
    return max(0, min(0xffff, n))


myops = {
    '+':  operator.add,
    '-':  operator.sub,
    '|': operator.or_,
    '&': operator.and_,
    '^': operator.xor,
}


def main():
    global myops
    debug_redirect()
    stack = []
    for token in raw_input().split():
        if token == "~":
            stack[-1] ^= 0xffff
        elif token in myops:
            func = myops[token]
            a, b = None, None
            try:
                b, a = stack.pop(), stack.pop()
                #print >> sys.stderr, a, token, b
                stack.append(bound(func(a, b)))
            except IndexError:
                print >> sys.stderr, "Index error while performing '%s' with '%s' and '%s'." % (token, a, b)
                error_exit()
        else:
            try:
                stack.append(int(token, 16))
            except ValueError:
                print >> sys.stderr, "Invalid int value: %s" % token
                error_exit()

    if len(stack) != 1:
        error_exit()
    else:
        print ("%04X" % bound(stack.pop()))


if "__main__" == __name__:
    main()