import random


def sort(data):
    for i in reversed(range(1, len(data))):
        for j in range(i):
            if data[j + 1] < data[j]:
                data[j], data[j + 1] = data[j + 1], data[j]

        print(data)


if __name__ == '__main__':
    data = [random.randint(1, 20) for _ in range(20)]

    print("--- before ---")
    print(data)

    print("--- sort ---")
    sort(data)

    print("--- after ---")
    print(data)
