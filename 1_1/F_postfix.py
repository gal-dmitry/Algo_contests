import sys


def main():
    string = list(sys.stdin.readline().split())
    stack1 = []
    stack2 = []
    # print(string)
    while string:
        stack1.append(string.pop())
    # print(stack1)
    while stack1:
        item = stack1.pop()
        if item == '+':
            a = int(stack2.pop())
            b = int(stack2.pop())
            stack2.append(a + b)
        elif item == '*':
            a = int(stack2.pop())
            b = int(stack2.pop())
            stack2.append(a * b)
        elif item == '-':
            a = int(stack2.pop())
            b = int(stack2.pop())
            stack2.append(b - a)
        else:
            stack2.append(int(item))
        # print(stack2)
    sys.stdout.write(''.join(map(str, stack2)))


if __name__ == "__main__":
    main()