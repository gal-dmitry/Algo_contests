import sys


def gcd(n, m):
    if m == 0:
        return n, 1, 0
    d, x, y = gcd(m, n % m)
    return d, y, (x - y * (n // m))


def euler(n):
    func = n
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            while n % i == 0:
                n /= i
            func -= func / i
        i += 1
    if n > 1:
        func -= func / n
    return func


def main():

    n = int(sys.stdin.readline())
    e = int(sys.stdin.readline())
    c = int(sys.stdin.readline())

    f = euler(n)
    g, x, y = gcd(e, f)
    d = int(x % f)

    answer = pow(c, d, n)
    sys.stdout.write(str(answer))


if __name__ == "__main__":
    main()