import sys


def binary_search(edge, task, cities, req):
    l = 0
    r = edge
    while l < r - 1:
        m = (l + r) // 2
        if req == cities[m]:
            return m
        elif req > cities[m]:
            l = m
        else:
            r = m
    if task == 0:
        return r
    else:
        return l


def main():
    n = int(sys.stdin.readline())
    cities = list(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline())
    request = [[0, 0, 0]] * k
    for i in range(k):
        req = list(map(int, sys.stdin.readline().split()))
        request[i] = req
    for i in range(n):
        cities[i] = (cities[i], i + 1)
    cities.sort()
    cities.insert(0, (float('-inf'), 0))
    cities.append((float('inf'), n + 1))
    ans = ''
    for i in range(k):
        edge = n + 1
        left = request[i][0]
        right = request[i][1]
        count = request[i][2]
        ind1 = binary_search(edge, 0, cities, (count, left))
        ind2 = binary_search(edge, 1, cities, (count, right))
        if (ind2 - ind1 + 1) > 0:
            ans += '1'
        else:
            ans += '0'
    sys.stdout.write(ans)


if __name__ == "__main__":
    main()