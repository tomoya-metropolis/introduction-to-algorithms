import random


def sort(data):
    quick_sort(data, 0, len(data) - 1)


def quick_sort(data, idx_of_start, idx_of_end):
    if idx_of_start < idx_of_end:
        idx_of_partition = partition(data, idx_of_start, idx_of_end)

        quick_sort(data, idx_of_start, idx_of_partition - 1)
        quick_sort(data, idx_of_partition + 1, idx_of_end)


def partition(data, idx_of_start, idx_of_end):
    pivot = data[idx_of_end]

    i = idx_of_start
    for j in range(idx_of_start, idx_of_end):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1

    data[i], data[idx_of_end] = data[idx_of_end], data[i]

    print(data)

    return i


if __name__ == '__main__':
    data = [random.randint(1, 20) for _ in range(20)]

    print("--- before ---")
    print(data)

    print("--- sort ---")
    sort(data)

    print("--- after ---")
    print(data)
