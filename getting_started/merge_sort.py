import random


def sort(data):
    merge_sort(data, 0, len(data) - 1)


def merge_sort(data, idx_of_start, idx_of_end):
    if idx_of_start < idx_of_end:
        idx_of_mid = (idx_of_start + idx_of_end) // 2

        merge_sort(data, idx_of_start, idx_of_mid)
        merge_sort(data, idx_of_mid + 1, idx_of_end)
        merge(data, idx_of_start, idx_of_mid, idx_of_end)

        print(data)


def merge(data, idx_of_start, idx_of_mid, idx_of_end):
    first_half = data[idx_of_start:idx_of_mid + 1]
    second_half = data[idx_of_mid + 1:idx_of_end + 1]

    i = j = 0
    for k in range(idx_of_start, idx_of_end + 1):
        if i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                data[k] = first_half[i]
                i += 1
            else:
                data[k] = second_half[j]
                j += 1
        elif i < len(first_half):
            data[k] = first_half[i]
            i += 1
        else:
            data[k] = second_half[j]
            j += 1


if __name__ == '__main__':
    data = [random.randint(1, 20) for _ in range(20)]

    print("--- before ---")
    print(data)

    print("--- sort ---")
    sort(data)

    print("--- after ---")
    print(data)
