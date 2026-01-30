import sys


def cut_rod(prices):
    results = [-sys.maxsize for _ in range(len(prices) + 1)]
    thresholds = [-1 for _ in range(len(prices) + 1)]

    results[0] = 0
    for j in range(1, len(prices)):
        result = -sys.maxsize
        for i in range(j + 1):
            if result < prices[i] + results[j - i]:
                result = prices[i] + results[j - i]
                thresholds[j] = i

        results[j] = result

    return results, thresholds


def print_optimal_strategy(thresholds, n):
    print('(', end='')

    rest = n
    while rest > 0:
        print(thresholds[rest], end='')

        if rest - thresholds[rest] > 0:
            print(' + ', end='')

        rest -= thresholds[rest]

    print(')', end='')


if __name__ == '__main__':
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    results, thresholds = cut_rod(prices)
    for i in range(len(prices)):
        print(f"n = {i} / result = {results[i]} ", end='')
        if i != 0:
            print_optimal_strategy(thresholds, i)
        print('')
