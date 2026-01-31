import sys


def matrix_chain_order(p):
    results = [[sys.maxsize for _ in range(len(p))] for _ in range(len(p))]
    thresholds = [[0 for _ in range(len(p))] for _ in range(len(p))]

    for i in range(len(p)):
        results[i][i] = 0

    diff = 1
    while diff < len(p) - 1:
        i, j = 0, diff
        while j < len(p) - 1:
            result = sys.maxsize
            for k in range(i, j):
                if result > results[i][k] + results[k + 1][j] + p[i] * p[k + 1] * p[j + 1]:
                    result = results[i][k] + results[k +
                                                     1][j] + p[i] * p[k + 1] * p[j + 1]
                    thresholds[i][j] = k

            results[i][j] = result

            i += 1
            j += 1

        diff += 1

    return results, thresholds


def print_optimal_strategy(thresholds, i, j):
    if i == j:
        print(f"A{i}", end='')
    else:
        print('(', end='')
        print_optimal_strategy(thresholds, i, thresholds[i][j])
        print_optimal_strategy(thresholds, thresholds[i][j] + 1, j)
        print(')', end='')


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

    results, thresholds = matrix_chain_order(p)
    diff = 0
    while diff < len(p) - 1:
        print(f"--- {diff} ---")

        i, j = 0, diff
        while j < len(p) - 1:
            print(f"(i, j) = {i, j} / result = {results[i][j]} ", end='')
            if i != j:
                print_optimal_strategy(thresholds, i, j)
            print('')

            i += 1
            j += 1

        diff += 1
