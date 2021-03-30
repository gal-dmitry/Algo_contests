import sys


def cost(a, b):
    if a == b:
        return 0
    return 1


def editing_distance(str1, str2, n, m, d):
    if d[m][n] == float("inf"):
        if n == 0:
            d[m][n] = m
        elif m == 0:
            d[m][n] = n
        else:
            opt1 = editing_distance(str1, str2, n - 1, m, d) + 1
            opt2 = editing_distance(str1, str2, n, m - 1, d) + 1
            opt3 = editing_distance(str1, str2, n - 1, m - 1, d) + cost(str1[n - 1], str2[m - 1])
            d[m][n] = min(opt1, opt2, opt3)
    return d[m][n]


def main():
    sys.stdin = open("editdist.in", "r")
    str1 = sys.stdin.readline()
    str2 = sys.stdin.readline()
    sys.stdin.close()

    n = len(str1)
    m = len(str2)
    d = [[float("inf") for i in range(n + 1)] for j in range(m + 1)]
    result = str(editing_distance(str1, str2, n, m, d))

    sys.stdout = open("editdist.out", "w")
    sys.stdout.write(result)
    sys.stdout.close()


if __name__ == "__main__":
    main()