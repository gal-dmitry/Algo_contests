def out(stack1, stack2):
    if not stack1 and not stack2:
        return -1
    elif not stack1:
        return stack2[-1][1]
    elif not stack2:
        return stack1[-1][1]
    return min(stack1[-1][1], stack2[-1][1])


def add(item, stack):
    if not stack:
        stack.append((item, item))
    else:
        stack.append((item, min(stack[-1][1], item)))


def extract(stack1, stack2):
    if not stack2:
        while stack1:
            add(stack1.pop()[0], stack2)
    stack2.pop()


def main():
    n = int(input())
    stack1 = []
    stack2 = []
    for i in range(n):
        item = input().split()
        if len(item) == 1:
            extract(stack1, stack2)
        else:
            add(int(item[1]), stack1)
        print(out(stack1, stack2))


if __name__ == "__main__":
    main()