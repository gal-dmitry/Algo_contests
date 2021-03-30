import sys


def dfs(s, f, c_min, path, used, matrix, n):
    if s == f:
        return c_min
    used[s] = 1

    for i in range(n):
        if used[i] == 0 and matrix[s][i] != float('inf') and (matrix[s][i][0] > 0 or matrix[i][s][1] < 0):


            delta = dfs(s, f, min(c_min, разница), path, used, matrix, n)
            if delta = 0

            if matrix[s][i][0] > 0:
                delta = dfs(i, f, min(c_min,  matrix[s][i][0]), path, used, matrix, n)



            else:


            if i == f:
                used[i] = 1
                break
            else:
                path = dfs(i, f, path, used, matrix, n)
                if path[-1][-1] == f:
                    break

    print(path)
    print()
    for i in range(n):
        print(matrix[i])
    print()
    return path


def main():
    n, m = map(int, sys.stdin.readline().split())
    matrix = [[float('inf') for i in range(n)] for j in range(n)]
    for i in range(m):
        u, v, c = list(map(int, sys.stdin.readline().split()))
        matrix[u - 1][v - 1] = [c, 0]
        matrix[v - 1][u - 1] = [c, 0]

    # печать
    for i in range(n):
        print(matrix[i])
    print()
    ###

    s = 0
    f = n - 1

    # пока можем найти путь из s в f
    while True:
    # for i in range(10):
        path = []
        used = [0 for i in range(n)]
        new_path = dfs(s, f, path, used, matrix, n)
        if not new_path: #не смог выйти из истока => один исток лежит в S
            for i in range(n):
                print(matrix[s][i])
            break

        if new_path[-1][-1] != f:
            break

        for edge in new_path:
            orient, u, v = edge[0], edge[1], edge[2]
            if orient == 'direct':
                matrix[u][v][0] -= 1
                matrix[u][v][1] -= 1
            else:
                matrix[v][u][0] += 1
                matrix[v][u][1] += 1

    ###
    for i in range(n):
        print(matrix[i])
    ###


if __name__ == "__main__":
    main()