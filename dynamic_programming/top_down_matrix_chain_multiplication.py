import sys


def matrix_chain_order(p, i, j):
    results = [[sys.maxsize for _ in range(len(p))] for _ in range(len(p))]

    return matrix_chain_order_internal(p, i, j, results)


def matrix_chain_order_internal(p, i, j, results):
    if results[i][j] < sys.maxsize:
        return results[i][j]
    else:
        if i == j:
            result = 0
        else:
            result = sys.maxsize
            for k in range(i, j):
                result = min(result, matrix_chain_order_internal(
                    p, i, k, results) + matrix_chain_order_internal(p, k + 1, j, results) + p[i] * p[k + 1] * p[j + 1])

        results[i][j] = result

        return result


if __name__ == '__main__':
    p = [30, 35, 15, 5, 10, 20, 25]

    print("  i |", end='')
    for i in range(len(p) - 1):
        print(f"{i:^7}|", end='')
    print('')
    print("A[i]|", end='')
    for i in range(len(p) - 1):
        print(f"{p[i]:>3}*{p[i + 1]:>3}|", end='')
    print('')

    diff = 0
    while diff < len(p) - 1:
        print(f"--- {diff} ---")

        i, j = 0, diff
        while j < len(p) - 1:
            result = matrix_chain_order(p, i, j)

            print(f"(i, j) = {i, j} / result = {result}")

            i += 1
            j += 1

        diff += 1
