import sys


def cut_rod(prices, n):
    if n == 0:
        return 0

    result = -sys.maxsize
    for i in range(1, n + 1):
        result = max(result, prices[i] + cut_rod(prices, n - i))

    return result


if __name__ == '__main__':
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    print("  i |", end='')
    for i in range(len(prices)):
        print(f"{i:>3}|", end='')
    print('')
    print("p[i]|", end='')
    for p in prices:
        print(f"{p:>3}|", end='')
    print('')

    for i in range(len(prices)):
        result = cut_rod(prices, i)

        print(f"length = {i} / result = {result}")
