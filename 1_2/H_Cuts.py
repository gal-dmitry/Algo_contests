def main():
    n = int(input())
    cuts = [[0, 0] for i in range(n)]
    for i in range(n):
        cuts[i] = [int(i) for i in input().split()]

    print(cuts)
    cuts.sort(key=lambda i: i[1])
    print(cuts)

    i = 1
    count = 1
    current = cuts[0]
    while i < n:
        if cuts[i][0] >= current[1]:
            count += 1
            current = cuts[i]
        i += 1

    print(count)


if __name__ == "__main__":
    main()