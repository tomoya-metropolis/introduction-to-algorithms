import sys


def optimal_bst(p, q):
    results = [[sys.maxsize for _ in range(
        len(p) + 1)] for _ in range(len(p) + 1)]
    w = [[0.0 for _ in range(
        len(p) + 1)] for _ in range(len(p) + 1)]
    roots = [[-1 for _ in range(
        len(p) + 1)] for _ in range(len(p) + 1)]

    for i in range(1, len(p) + 1):
        results[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]

    diff = 0
    while diff < len(p) - 1:
        i = 0
        j = i + diff

        while j < len(p):
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            w[i][j] = round(w[i][j], 2)

            result = sys.maxsize
            for r in range(i, j + 1):
                if result > w[i][j] + results[i][r - 1] + results[r + 1][j]:
                    result = w[i][j] + results[i][r - 1] + results[r + 1][j]
                    roots[i][j] = r

            results[i][j] = result

            i += 1
            j += 1

        diff += 1

    return results, w, roots


if __name__ == '__main__':
    p = [0, 0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]

    print("  i |", end='')
    for i in range(len(p)):
        print(f"{i:^4}|", end='')
    print('')
    print("p[i]|", end='')
    for _p in p:
        print(f"{_p:.2f}|", end='')
    print('')
    print("q[i]|", end='')
    for _q in q:
        print(f"{_q:.2f}|", end='')
    print('')

    results, w, roots = optimal_bst(p, q)

    diff = -1
    while diff < len(p) - 1:
        print(F"--- diff = {diff} ---")

        i = 1
        j = i + diff
        while j < len(p):

            print(
                f"i = {i}, j = {j} / result = {results[i][j]:.2f}, w = {w[i][j]:.2f}", end=' ')
            if j != i - 1:
                print(f", root = {roots[i][j]}", end='')
            print('')

            i += 1
            j += 1

        diff += 1
