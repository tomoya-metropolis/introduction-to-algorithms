import random


def sort(data):
    bucket = [[] for _ in range(max(data) // 10 + 1)]

    for d in data:
        bucket[d // 10].append(d)

    print("--- bucket before sorting ---")
    for i, b in enumerate(bucket):
        print(i, ': ', b)

    for b in bucket:
        b.sort()

    print("--- bucket after sorting ---")
    for i, b in enumerate(bucket):
        print(i, ': ', b)

    data.clear()
    for b in bucket:
        data.extend(b)


if __name__ == '__main__':
    data = [random.randint(1, 100) for _ in range(100)]

    print("--- before ---")
    print(data)

    print("--- sort ---")
    sort(data)

    print("--- after ---")
    print(data)
