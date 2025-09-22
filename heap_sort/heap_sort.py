import random


def sort(data):
    build_max_heap(data)

    print(data)

    for i in reversed(range(len(data))):
        data[0], data[i] = data[i], data[0]

        print(data)

        max_heapify(data, 0, i - 1)


def build_max_heap(data):
    for i in reversed(range(len(data) // 2)):
        max_heapify(data, i, len(data) - 1)


def max_heapify(data, idx_of_target, idx_of_heap):
    idx_of_largest = idx_of_target

    idx_of_left = 2 * idx_of_target + 1
    if idx_of_left <= idx_of_heap and data[idx_of_left] > data[idx_of_largest]:
        idx_of_largest = idx_of_left
    idx_of_right = 2 * (idx_of_target + 1)
    if idx_of_right <= idx_of_heap and data[idx_of_right] > data[idx_of_largest]:
        idx_of_largest = idx_of_right

    if idx_of_largest != idx_of_target:
        data[idx_of_target], data[idx_of_largest] = data[idx_of_largest], data[idx_of_target]

        max_heapify(data, idx_of_largest, idx_of_heap)


if __name__ == '__main__':
    data = [random.randint(1, 20) for _ in range(20)]

    print("--- before ---")
    print(data)

    print("--- sort ---")
    sort(data)

    print("--- after ---")
    print(data)
