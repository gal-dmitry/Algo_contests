import sys
from collections import deque


def bfs(adj_list, exits, N):
    dist = [None] * (N + 1)
    nearest_exit = [None] * (N + 1)
    for ex in exits:
        dist[ex] = 0
        nearest_exit[ex] = ex

    q = deque(exits)
    while q:
        ex = q.popleft()
        for neighbor in adj_list[ex]:
            if dist[neighbor] is None:
                dist[neighbor] = dist[ex] + 1
                nearest_exit[neighbor] = nearest_exit[ex]
                q.append(neighbor)
            else:
                if nearest_exit[ex] < nearest_exit[neighbor] and dist[neighbor] == dist[ex] + 1:
                    nearest_exit[neighbor] = nearest_exit[ex]
                    q.append(neighbor)
    return dist, nearest_exit


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
exits = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
adj_list = [set() for _ in range(N + 1)]
for _ in range(M):
    bunker_1, bunker_2 = map(int, sys.stdin.readline().split())
    adj_list[bunker_1].add(bunker_2)
    adj_list[bunker_2].add(bunker_1)

dist, nearest_exit = bfs(adj_list, exits, N)
print(*dist[1::])
print(*nearest_exit[1::])
