import sys


def main():
    sys.stdin = open("knapsack.in", "r")
    full_w, n = list(map(int, sys.stdin.readline().split()))
    w = list(map(int, sys.stdin.readline().split()))
    sys.stdin.close()
    w.insert(0, 0)

    d = [[0 for j in range(full_w + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, full_w + 1):
            d[i][j] = d[i - 1][j]
            if w[i] <= j:
                d[i][j] = max(d[i][j], d[i - 1][j - w[i]] + w[i])
    result = str(d[n][full_w])

    sys.stdout = open("knapsack.out", "w")
    sys.stdout.write(result)
    sys.stdout.close()


if __name__ == "__main__":
    main()