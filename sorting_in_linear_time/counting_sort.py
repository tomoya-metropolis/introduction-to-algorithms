import random


def sort(data):
    counting_table = [0 for _ in range(max(data) + 1)]

    for d in data:
        counting_table[d] += 1

    print(counting_table)

    for i in range(len(counting_table) - 1):
        counting_table[i + 1] += counting_table[i]

    print(counting_table)

    temp = [-1 for _ in range(len(data))]
    for i in reversed(range(len(data))):
        target = data[i]
        idx_to_place = counting_table[target] - 1
        temp[idx_to_place] = target
        counting_table[target] -= 1

    data.clear()
    data.extend(temp)


if __name__ == '__main__':
    data = [random.randint(1, 20) for _ in range(40)]

    print("--- before ---")
    print(data)

    print("--- sort ---")
    sort(data)

    print("--- after ---")
    print(data)
