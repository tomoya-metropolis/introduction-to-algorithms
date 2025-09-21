import sys


def find_maximum_subarray(data, idx_of_start, idx_of_end):
    if idx_of_start == idx_of_end:
        return data[idx_of_start], idx_of_start, idx_of_end
    else:
        idx_of_mid = (idx_of_start + idx_of_end) // 2

        sum_of_first, start_idx_of_first, end_idx_of_first = find_maximum_subarray(
            data, idx_of_start, idx_of_mid)
        sum_of_second, start_idx_of_second, end_idx_of_second = find_maximum_subarray(
            data, idx_of_mid + 1, idx_of_end)
        sum_of_crossing, start_idx_of_crossing, end_idx_of_crossing = find_max_crossing_subarray(
            data, idx_of_start, idx_of_mid, idx_of_end)

        if sum_of_first > sum_of_second and sum_of_first > sum_of_crossing:
            return sum_of_first, start_idx_of_first, end_idx_of_first
        elif sum_of_second > sum_of_first and sum_of_second > sum_of_second:
            return sum_of_second, start_idx_of_second, end_idx_of_second
        else:
            return sum_of_crossing, start_idx_of_crossing, end_idx_of_crossing


def find_max_crossing_subarray(data, idx_of_start, idx_of_mid, idx_of_end):
    sum_of_first = -sys.maxsize
    summary = 0
    for i in reversed(range(idx_of_start, idx_of_mid + 1)):
        summary += data[i]
        if summary > sum_of_first:
            sum_of_first = summary
            start = i

    sum_of_second = -sys.maxsize
    summary = 0
    for i in range(idx_of_mid + 1, idx_of_end + 1):
        summary += data[i]
        if summary > sum_of_second:
            sum_of_second = summary
            end = i

    return sum_of_first + sum_of_second, start, end


if __name__ == '__main__':
    data = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    print("  i |", end='')
    for i in range(len(data)):
        print(f"{i:>3}|", end='')
    print('')
    print("d[i]|", end='')
    for d in data:
        print(f"{d:>3}|", end='')
    print('')

    summary, idx_of_first, idx_of_second = find_maximum_subarray(
        data, 0, len(data) - 1)
    print(f"result = {summary} [", end='')
    for i in range(idx_of_first, idx_of_second + 1):
        print(data[i], end=', ' if i != idx_of_second else ']')
    print('')
