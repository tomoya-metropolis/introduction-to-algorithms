import enum


class Direction(enum.Enum):

    UP = 'up'
    LEFT = 'left'
    DIAGONAL = 'diagonal'


def common_lcs(x, y):
    results = [[-1 for _ in range(max(len(x), len(y)))]
               for _ in range(max(len(x), len(y)))]
    directions = [[None for _ in range(max(len(x), len(y)))]
                  for _ in range(max(len(x), len(y)))]

    for i in range(len(x)):
        for j in range(len(y)):
            if i == 0 and j == 0:
                if x[i] == y[j]:
                    results[i][j] = 1
                    directions[i][j] = Direction.DIAGONAL
                else:
                    results[i][j] = 0
                    directions[i][j] = Direction.UP
            elif i == 0:
                if x[i] == y[j]:
                    results[i][j] = 1
                    directions[i][j] = Direction.DIAGONAL
                else:
                    results[i][j] = results[i][j - 1]
                    directions[i][j] = Direction.LEFT
            elif j == 0:
                if x[i] == y[j]:
                    results[i][j] = 1
                    directions[i][j] = Direction.DIAGONAL
                else:
                    results[i][j] = results[i - 1][j]
                    directions[i][j] = Direction.UP
            else:
                if x[i] == y[j]:
                    results[i][j] = results[i - 1][j - 1] + 1
                    directions[i][j] = Direction.DIAGONAL
                elif results[i - 1][j] < results[i][j - 1]:
                    results[i][j] = results[i][j - 1]
                    directions[i][j] = Direction.LEFT
                else:
                    results[i][j] = results[i - 1][j]
                    directions[i][j] = Direction.UP

    return results, directions


def print_optimal_strategy(x, i, j, directions):
    if i < 0 or j < 0:
        return
    if directions[i][j] == Direction.DIAGONAL:
        print_optimal_strategy(x, i - 1, j - 1, directions)
        print(x[i], end='')
    elif directions[i][j] == Direction.UP:
        print_optimal_strategy(x, i - 1, j, directions)
    else:
        print_optimal_strategy(x, i, j - 1, directions)


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"

    results, directions = common_lcs(x, y)
    for i in range(len(x)):
        print(f"--- i = {i} ---")
        for j in range(len(y)):

            print(
                f"(i, j) = {i, j} / x = {x[:i + 1]}, y = {y[:j + 1]} / result = {results[i][j]} ", end='')
            if i != 0 and y != 0:
                print('(', end='')
                print_optimal_strategy(x, i, j, directions)
                print(')', end='')
            print('')
