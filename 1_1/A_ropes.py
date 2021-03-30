def counting(n, k, ropes, m):
    count = 0
    for i in range(n):
        count += ropes[i] // m
        if count >= k:
            return True
    return False


def binary_search(n, k, longest, ropes):
    l = 1
    r = longest
    while l < r - 1:
        m = (l + r) // 2
        if counting(n, k, ropes, m):
            l = m
        else:
            r = m
    # print(l, r)
    if counting(n, k, ropes, r):
        return r
    elif counting(n, k, ropes, l):
        return l
    else:
        return 0


def main():
    n, k = (int(i) for i in input().split())
    ropes = []
    for i in range(n):
        ropes.append(int(input()))
    longest = max(ropes)
    print(binary_search(n, k, longest, ropes))
    # print(ropes)
    # for i in range(n):
    #     print(type(ropes[i]))
    # print(longest)
    # print(type(longest))


if __name__ == "__main__":
    main()