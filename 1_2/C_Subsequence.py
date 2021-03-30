def main():
    with open("lcs.in", "r") as lcs_in:
        n = int(lcs_in.readline())
        str1 = lcs_in.readline().split()
        m = int(lcs_in.readline())
        str2 = lcs_in.readline().split()

    d0 = [0 for i in range(n + 1)]
    d1 = [0 for i in range(n + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[j - 1] == str2[i - 1]:
                d1[j] = d0[j - 1] + 1
            else:
                d1[j] = max(d0[j], d1[j - 1])
        d0, d1 = d1, [0 for i in range(n + 1)]
    result = str(d0[n])

    with open("lcs.out", "w") as lcs_out:
        lcs_out.write(result)


if __name__ == "__main__":
    main()