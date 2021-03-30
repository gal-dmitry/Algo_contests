import sys
import threading


def processDFSTree(graph, stack, visited):
    for v in graph[stack[-1]]:
        if visited[v] == "in_stack":
            print("YES")
            stack2 = []
            stack2.append(stack[-1])
            stack.pop()
            while stack2[-1] != v:
                stack2.append(stack[-1])
                stack.pop()
            while stack2:
                print(stack2[-1] + 1, end=" ")
                stack.append(stack2[-1])
                stack2.pop()
            exit()
        elif visited[v] == "not_visited":
            stack.append(v)
            visited[v] = "in_stack"
            processDFSTree(graph, stack, visited)
    visited[stack[-1]] = "done"
    stack.pop()


def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = [set() for _ in range(n)]
    for _ in range(m):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1 - 1].add(v2 - 1)

    visited = ["not_visited"] * n
    for v in range(n):
        if visited[v] == "not_visited":
            stack = []
            stack.append(v)
            visited[v] = "in_stack"
            processDFSTree(graph, stack, visited)

    print("NO")


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
