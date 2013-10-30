import sys
import shlex
import os

parser = None
target = ""
roads  = []
routes = set()

def debug_redirect():
    global parser
    if os.environ.has_key('PYCHARM_HOSTED'):
        sys.stdin = open("problemas.input1.txt", 'r')
        sys.stdout = open("problemas.output1.txt", 'wc')
    parser = shlex.shlex(sys.stdin)
    parser.whitespace_split = True


def parse_inputs():
    global target, roads
    target = parser.get_token()
    while 1:
        a, b = parser.get_token(), parser.get_token()
        if a == b == "A":
            break
        roads.append((a, b,))


def get_new_visited(v, a):
    r = v.copy()
    r.add(a)
    return r


def generate_path(current, visited):
    global roads, target
    if current == target:
        yield [current]
    else:
        for a, b in [x for x in roads if (x[0] == current or x[1] == current)]:
            src, dst = (a, b) if a == current else (b, a)
            if src not in visited:
                for res in generate_path(dst, get_new_visited(visited, src)):
                    yield [src] + res


def routecmp(a, b):
    if len(a) < len(b):
        return -1
    elif len(b) < len(a):
        return 1
    return cmp(a, b)


def main():
    global routes
    debug_redirect()
    parse_inputs()
    #print >> sys.stderr, target
    #print >> sys.stderr, roads
    short = sys.maxint
    for route in generate_path('F', set()):
        routes.add(tuple(route))
        short = min(short, len(route))

    paths = len(routes)
    routes = sorted(list(routes), cmp=routecmp)

    #for route in routes:
    #    print >> sys.stderr, route

    if paths:
        print "Total Routes: %d" % (paths,)
        print "Shortest Route Length: %d" % (short,)
        print "Shortest Route after Sorting of Routes of length %d: %s" % (short, " ".join(routes[0]))
    else:
        print "No Route Available from F to %s" % (target,)




if "__main__" == __name__:
    main()