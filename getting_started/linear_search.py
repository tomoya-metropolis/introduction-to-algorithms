import random


def search(data, key):
    for i, d in enumerate(data):
        if d == key:
            return i

    return -1


if __name__ == '__main__':
    data = [random.randint(1, 20) for _ in range(20)]

    print("--- data ---")
    print(data)

    print("input key > ", end='')
    key = int(input())

    result = search(data, key)
    if result == -1:
        print(f"{key} is not found.")
    else:
        print(f"result = {result}")
