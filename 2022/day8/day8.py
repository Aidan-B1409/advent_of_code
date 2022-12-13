from typing import Iterator
import numpy as np
import operator
import itertools
import functools


def is_edge_visible(arr: np.ndarray, i: int, j: int) -> bool:
    return (
        (all(arr[i, 0:j] < arr[i][j]))
        or (all(arr[i, j + 1 : arr.shape[1]] < arr[i][j]))
        or (all(arr[0:i, j] < arr[i][j]))
        or (all(arr[i + 1 : arr.shape[0], j] < arr[i][j]))
    )


def inclusive_takewhile(x: np.ndarray, condition) -> int:
    if len(x) > 0:
        l = len(list(itertools.takewhile(condition, x)))
        if l == len(x):
            return l
        return l + 1
    return 0


def calculate_visibility_score(arr: np.ndarray, i: int, j: int) -> int:
    scans = [
        np.flip(arr[i, 0:j]),
        arr[i, j + 1 : arr.shape[1]],
        np.flip(arr[0:i, j]),
        arr[i + 1 : arr.shape[0], j],
    ]
    print(f"\n\n{arr[i][j]}")
    print(list(map(lambda x: inclusive_takewhile(x, lambda y: y < arr[i, j]), scans)))
    return functools.reduce(
        operator.mul,
        list(map(lambda x: inclusive_takewhile(x, lambda y: y < arr[i, j]), scans)),
    )


def main():
    max = 0
    with open("input.txt") as input:
        arr = np.array([list(map(int, [*line[:-1]])) for line in input.readlines()])
    sum = 0
    print(
        len(
            list(
                itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 5, 6, 4, 3, 2, 1])
            )
        )
    )
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            score = calculate_visibility_score(arr, i, j)
            if score > max:
                max = score

            #  if is_edge_visible(arr, i, j):
            #      sum += 1
    print(sum)
    print(max)


if __name__ == "__main__":
    main()
