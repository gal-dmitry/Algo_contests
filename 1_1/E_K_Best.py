import random
import sys


def random_select(a, l, r, stat):
    if l >= r:
        return a[l]
    x = a[random.randint(l, r)][0]
    i = l
    j = r
    while i <= j:
        while a[i][0] < x:
            i += 1
        while a[j][0] > x:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if l <= stat <= j:
        random_select(a, l, j, stat)
    elif i <= stat <= r:
        random_select(a, i, r, stat)
    else:
        return x


def main():
    n, k = list(map(int, sys.stdin.readline().split()))
    stat = n - k
    lst = [(0, 0)] * n
    ans = [0] * k
    for i in range(n):
        v, w = list(map(int, sys.stdin.readline().split()))
        p = v / w
        lst[i] = (p, i + 1)
    lst.sort()
    random_select(lst, 0, n - 1, stat)
    for i in range(k):
        ans[i] = lst.pop()[1]
    sys.stdout.write(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()