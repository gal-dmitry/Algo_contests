import sys

sys.stdin = open("calcul.in", "r")
sys.stdout = open("calcul.out", "w")

n = int(sys.stdin.readline())

dp = [-1, 0]
array = [0, 1]
for i in range(2, n + 1):
    first_case = second_case = third_case = n
    if i % 2 == 0:
        first_case = dp[int(i / 2)]
    if i % 3 == 0:
        second_case = dp[int(i / 3)]
    if i - 1 >= 0:
        third_case = dp[i - 1]
    dp.append(min(second_case + 1, first_case + 1, third_case + 1))
    if second_case <= min(first_case, third_case):
        array.append(int(i / 3))
    elif first_case <= min(second_case, third_case):
        array.append(int(i / 2))
    elif third_case <= min(second_case, first_case):
        array.append(i - 1)

sys.stdout.write(f"{dp[n]}\n")
result = [n]

print(dp)
print(array)
for i in range(dp[n]):
    result.append(array[n])
    n = array[n]
print(*result[::-1])
