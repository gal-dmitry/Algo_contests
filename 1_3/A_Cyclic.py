import sys
import threading


def explore(lst, stack, visited):
    for i in lst[stack[-1]]:
        if visited[i] == 1:
            sys.stdout.write('YES' + '\n')
            stack2 = [stack[-1]]
            stack.pop()
            while stack2[-1] != i:
                stack2.append(stack[-1])
                stack.pop()
            while stack2:
                sys.stdout.write(str(stack2[-1] + 1) + ' ')
                stack.append(stack2[-1])
                stack2.pop()
            exit()
        elif visited[i] == 0:
            stack.append(i)
            visited[i] = 1
            explore(lst, stack, visited)
    visited[stack[-1]] = 2
    stack.pop()


def main():
    v, e = map(int, sys.stdin.readline().split())
    lst = [set() for i in range(v)]
    for i in range(e):
        a, b = map(int, sys.stdin.readline().split())
        lst[a - 1].add(b - 1)

    visited = [0 for i in range(v)]

    for i in range(v):
        if visited[i] == 0:
            stack = [i]
            visited[i] = 1
            explore(lst, stack, visited)

    sys.stdout.write('NO')


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()