def common_lcs(x, y, i, j):
    results = [[-1 for _ in range(max(i + 1, j + 1))]
               for _ in range(max(i + 1, j + 1))]

    return common_lcs_internal(x, y, i, j, results)


def common_lcs_internal(x, y, i, j, results):
    if results[i][j] > -1:
        return results[i][j]

    if i == 0 and j == 0:
        result = 1 if x[i] == y[j] else 0
    elif i == 0:
        result = 1 if x[i] == y[j] else common_lcs_internal(x, y, i, j - 1, results)
    elif j == 0:
        result = 1 if x[i] == y[j] else common_lcs_internal(x, y, i - 1, j, results)
    else:
        if x[i] == y[j]:
            result = common_lcs_internal(x, y, i - 1, j - 1, results) + 1
        else:
            l1 = common_lcs_internal(x, y, i - 1, j, results)
            l2 = common_lcs_internal(x, y, i, j - 1, results)
            result = l1 if l1 > l2 else l2

    results[i][j] = result
    
    return result


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"

    for i in range(len((x))):
        print(f"--- i = {i} ---")
        for j in range(len(y)):
            result = common_lcs(x, y, i, j)

            print(f"i = {i}, j = {j}, x = {x[:i + 1]}, y = {y[:j + 1]} / result = {result}")
