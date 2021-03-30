import sys


def main():
    start = sys.stdin.readline()
    finish = sys.stdin.readline()
    matrix = [[0 for i in range(8)] for j in range(8)]
    d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    d2 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

    start1 = 8 - int(start[1])
    start2 = d1[start[0]] - 1

    finish1 = 8 - int(finish[1])
    finish2 = d1[finish[0]] - 1

    q = [([(start1, start2)], 1)]
    matrix[start1][start2] = 1
    path_global = []

    while q:
        v = q.pop(0)
        path = v[0]
        prio = v[1]
        prio += 1
        i = path[-1][0]
        j = path[-1][1]

        for m in [i - 2, i - 1, i + 1, i + 2]:
            if 0 <= m <= 7:
                if m == (i - 1) or m == (i + 1):
                    lst = [j - 2, j + 2]
                else:
                    lst = [j - 1, j + 1]

                for n in lst:
                    if (0 <= n <= 7) and matrix[m][n] == 0:
                        matrix[m][n] = prio
                        if m == finish1 and n == finish2:
                            path_global = path + [(m, n)]
                            break
                        q.append((path + [(m, n)], prio))
                if path_global:
                    break

    for i in path_global:
        ans = (d2[i[1]], 8 - i[0])
        sys.stdout.write("".join(map(str, ans)) + '\n')


if __name__ == "__main__":
    main()