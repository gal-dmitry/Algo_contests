import sys


def main():
    h, n = map(int, sys.stdin.readline().split())
    points = [[0, 0] for i in range(n)]
    for i in range(n):
        points[i] = list(map(int, sys.stdin.readline().split()))

    matrix = [[0 for i in range(n + 2)] for j in range(n + 2)]
    matrix[n][n + 1] = h
    matrix[n + 1][n] = h

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j] = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
            matrix[j][i] = matrix[i][j]

    for i in range(n):
        matrix[i][n] = points[i][1]
        matrix[n][i] = matrix[i][n]

    for i in range(n):
        matrix[i][n + 1] = h - points[i][1]
        matrix[n + 1][i] = matrix[i][n]

    s = n
    f = n + 1
    n += 2

    d = [matrix[s][i] for i in range(n)]
    q = {i: d[i] for i in range(n)}

    while q:
        u = min(q.items(), key=lambda x: x[1])[0]
        if u == f:
            break
        q.pop(u)
        for i in range(n):
            new_dist = max(matrix[u][i], d[u])
            if d[i] > new_dist:
                d[i] = new_dist
                q[i] = d[i]

    rast = "{0:.9f}".format(d[f])
    sys.stdout.write(str(rast))


if __name__ == "__main__":
    main()