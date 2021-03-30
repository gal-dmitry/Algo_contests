import sys


def get(p, x):
    if p[x] == x:
        return x
    return get(p, p[x])


def union(rk, p, total, x, y):
    x_p = get(p, x)
    y_p = get(p, y)

    if x_p != y_p:
        if rk[x_p] >= rk[y_p]:
            p[y_p] = x_p
            rk[x_p] += rk[y_p]
            total[y_p] -= total[x_p]

        else:
            p[x_p] = y_p
            rk[y_p] += rk[x_p]
            total[x_p] -= total[y_p]

    return rk, p, total


def main():
    n, m = (map(int, sys.stdin.readline().split()))
    total = [0 for i in range(n)]
    p = [j for j in range(n)]
    rk = [1 for i in range(n)]

    for i in range(m):
        ord = sys.stdin.readline().split()

        if ord[0] == 'get':
            x = int(ord[1]) - 1
            score = 0
            score += total[x]
            while x != p[x]:
                x = p[x]
                score += total[x]
            sys.stdout.write(str(score) + '\n')

        elif ord[0] == 'add':
            x, v = int(ord[1]) - 1, int(ord[2])
            root = get(p, x)
            total[root] += v

        else:
            x, y = int(ord[1]) - 1, int(ord[2]) - 1
            rank, p, experience = union(rk, p, total, x, y)


if __name__ == "__main__":
    main()