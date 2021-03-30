import sys


def init(n):
    p = [i for i in range(n)]
    r = [0 for i in range(n)]
    return p, r


def get(x, p):
    if x == p[x]:
        return x, p
    else:
        p[x], p = get(p[x], p)
        return p[x], p


def link(c1, c2, p, r):
    if r[c2] < r[c1]:
        p[c2] = c1
    else:
        p[c1] = c2
        if r[c1] == r[c2]:
            r[c2] += 1
    return p, r


def main():
    v, e = map(int, sys.stdin.readline().split())
    edges = [[0, 0, 0] for i in range(e)]
    for i in range(e):
        a, b, w = map(int, sys.stdin.readline().split())
        edges[i] = [w, a - 1, b - 1]

    answer = 0
    p, r = init(v)
    edges.sort()
    for e in edges:
        v, u = e[1], e[2]
        c1, p = get(v, p)
        c2, p = get(u, p)
        if c1 != c2:
            p, r = link(c1, c2, p, r)
            answer += e[0]
    sys.stdout.write(str(answer))


if __name__ == "__main__":
    main()