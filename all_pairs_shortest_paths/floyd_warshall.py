import copy
import sys


def floyd_warshall(W):
    n = len(W)
    D = copy.deepcopy(W)
    PI = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j or W[i][j] == sys.maxsize:
                PI[i][j] = sys.maxsize
            elif i != j and W[i][j] < sys.maxsize:
                PI[i][j] = i

    print("--- after initializing ---")
    print("--- D ---")
    prrint_matrix(D)
    print("--- PI ---")
    prrint_matrix(PI)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    d = D[i][k] + D[k][j]
                    pi = PI[k][j]
                else:
                    d = D[i][j]
                    pi = PI[i][j]

                D[i][j] = d
                PI[i][j] = pi

        print(f"--- k = {k} ---")
        print("--- D ---")
        prrint_matrix(D)
        print("--- PI ---")
        prrint_matrix(PI)

    return D, PI


def prrint_matrix(A):
    for a in A:
        for i in range(len(a)):
            print(a[i] if a[i] < 1000 else '-',
                  end=', ' if i < len(a) - 1 else '\n')


if __name__ == '__main__':
    W = [
        [0, 3, 8, sys.maxsize, -4],
        [sys.maxsize, 0, sys.maxsize, 1, 7],
        [sys.maxsize, 4, 0, sys.maxsize, sys.maxsize],
        [2, sys.maxsize, -5, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, sys.maxsize, 6, 0]
    ]

    print("--- adjacency matrix ---")
    prrint_matrix(W)

    print("--- Floyd-Warshall algorithm ---")
    D, PI = floyd_warshall(W)

    print("--- result ---")
    print("--- D ---")
    prrint_matrix(D)
    print("--- PI ---")
    prrint_matrix(PI)
