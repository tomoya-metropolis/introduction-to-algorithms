def search(data, key):
    idx_of_start = 0
    idx_of_end = len(data) - 1

    while idx_of_start <= idx_of_end:
        idx_of_mid = (idx_of_start + idx_of_end) // 2
        if data[idx_of_mid] == key:
            return idx_of_mid
        elif data[idx_of_mid] < key:
            idx_of_start = idx_of_mid + 1
        else:
            idx_of_end = idx_of_mid - 1

    return -1


if __name__ == '__main__':
    data = [i ** 2 for i in range(20)]

    print(data)

    print("input key > ", end='')
    key = int(input())

    result = search(data, key)
    if result != -1:
        print(f"result = {result}")
    else:
        print(f"{key} is not found.")
