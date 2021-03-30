import sys
from _continuation import continulet


def invoke(_, callable, arg):
    return callable(*arg)


def bootstrap(c):
    callable, *arg = c.switch()
    while True:
        to = continulet(invoke, callable, arg)
        callable, *arg = c.switch(to=to)


cont = continulet(bootstrap)
cont.switch()


def dfs(vertex, adjacency_list, dp, visited):
    visited[vertex] = True
    for i in range(len(adjacency_list[vertex])):
        if not visited[adjacency_list[vertex][i]]:
            cont.switch((dfs, adjacency_list[vertex][i], adjacency_list, dp, visited))
        dp[vertex] = max(dp[vertex], 1 + dp[adjacency_list[vertex][i]])


sys.stdin = open("longpath.in", "r")
sys.stdout = open("longpath.out", "w")

n, m = (int(i) for i in sys.stdin.readline().split())
adjacency_list = [[] for _ in range(n + 1)]
for _ in range(m):
    vertex_1, vertex_2 = (int(i) for i in sys.stdin.readline().split())
    adjacency_list[vertex_1].append(vertex_2)

dp = [0] * (n + 1)
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, adjacency_list, dp, visited)

result = 0
for i in range(1, n + 1):
    result = max(result, dp[i])

sys.stdout.write(str(result))
