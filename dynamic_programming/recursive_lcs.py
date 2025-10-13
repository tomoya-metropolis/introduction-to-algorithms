def common_lcs(x, y, i, j):
    if i == 0 and j == 0:
        return 1 if x[i] == y[j] else 0
    elif i == 0:
        return 1 if x[i] == y[j] else common_lcs(x, y, i, j - 1)
    elif j == 0:
        return 1 if x[i] == y[j] else common_lcs(x, y, i - 1, j)
    else:
        if x[i] == y[j]:
            return 1 + common_lcs(x, y, i - 1, j - 1)
        else:
            l1 = common_lcs(x, y, i - 1, j)
            l2 = common_lcs(x, y, i, j - 1)
            return l1 if l1 > l2 else l2


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"

    for i in range(len((x))):
        print(f"--- i = {i} ---")
        for j in range(len(y)):
            result = common_lcs(x, y, i, j)

            print(f"i = {i}, j = {j}, x = {x[:i + 1]}, y = {y[:j + 1]} / result = {result}")
