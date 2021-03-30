def sift_down(heap):
    i = 0
    k = len(heap) - 1
    while 2*i + 1 <= k:
        left = 2*i + 1
        right = 2*i + 2
        j = left
        if right <= k and heap[right] < heap[left]:
            j = right
        if heap[i] <= heap[j]:
            break
        heap[i], heap[j] = heap[j], heap[i]
        i = j


def sift_up(heap):
    i = len(heap) - 1
    while i > 0 and heap[i] < heap[(i - 1) // 2]:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2
    # return heap?


def extract_min(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    result = heap.pop()
    sift_down(heap)
    return result


def add(heap, x):
    heap.append(x)
    sift_up(heap)


def main():
    n = int(input())
    heap = []
    for i in range(n):
        x = input().split()
        if len(x) == 1:
            print(extract_min(heap))
        else:
            add(heap, int(x[1]))


if __name__ == "__main__":
    main()