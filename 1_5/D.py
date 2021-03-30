import sys


def gcd(n, m):
    if m == 0:
        return n, 1, 0
    d, x, y = gcd(m, n % m)
    return d, y, (x - y * (n // m))


def main():
    n, m = map(int, sys.stdin.readline().split())
    gcd_1, x, y = gcd(n, m)
    if gcd_1 == 1:
        x %= m
        sys.stdout.write(str(x))
    else:
        sys.stdout.write('-1')


if __name__ == "__main__":
    main()