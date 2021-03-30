def main():
    sys.stdin = open("connect.in", "r")
    v, e = list(map(int, sys.stdin.readline().split()))
    lst = [[] for i in range(v)]
    visited = [0 for i in range(v)]
    for i in range(e):
        a, b = list(map(int, sys.stdin.readline().split()))
        lst[a - 1].append(b - 1)
        lst[b - 1].append(a - 1)
    sys.stdin.close()

    count = 1
    for i in range(v):
        if visited[i] == 0:
            visited[i] = count
            queue = [i]
            while queue:
                vertex = int(queue.pop(0))
                for j in lst[vertex]:
                    if visited[j] == 0:
                        visited[j] = count
                        queue.append(j)
            count += 1

    sys.stdout = open("connect.out", "w")
    sys.stdout.write(str(count - 1) + '\n')
    sys.stdout.write(' '.join(map(str, visited)))
    sys.stdout.close()


import sys, threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()


if __name__ == "__main__":
    main()