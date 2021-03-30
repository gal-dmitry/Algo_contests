import sys


def main():
    n, s, f = map(int, sys.stdin.readline().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    s -= 1
    f -= 1

    d = [matrix[s][i] if matrix[s][i] != -1 else float('inf') for i in range(n)]
    q = {i: d[i] for i in range(n)}

    while q:
        u = min(q.items(), key=lambda x: x[1])[0]
        if u == f:
            break
        dist = q.pop(u)
        if dist == float('inf'):
            break
        for i in range(n):
            if matrix[u][i] != -1 and d[i] > matrix[u][i] + d[u]:
                d[i] = d[u] + matrix[u][i]
                q[i] = d[i]

    if d[f] == float('inf'):
        d[f] = -1
    sys.stdout.write(str(d[f]))


if __name__ == "__main__":
    main()