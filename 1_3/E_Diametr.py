import sys


def main():
    n = int(sys.stdin.readline())
    matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = float('inf')

    d = matrix
    for k in range(n):
        for v in range(n):
            for u in range(n):
                d[v][u] = min(d[v][u], d[v][k] + d[k][u])

    eccen = [0 for i in range(n)]
    for i in range(n):
        eccen[i] = max(d[i])

    diam = max(eccen)
    radius = min(eccen)
    sys.stdout.write(str(diam) + '\n')
    sys.stdout.write(str(radius))


if __name__ == "__main__":
    main()