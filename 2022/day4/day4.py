from typing import Callable
import numpy as np


def str_to_range(s: str) -> tuple[np.ndarray, np.ndarray]:
    return tuple(
        map(
            lambda x: np.array(list(map(lambda y: int(y), x.split("-")))),
            s.strip("\n").split(","),
        )
    )


def boundary_check(x: int) -> int:
    if x < 2 and x > -2:
        return 1
    return 0


def range_diff(x: tuple[np.ndarray, np.ndarray]) -> int:
    return boundary_check(np.sum(np.sign(x[1] - x[0])))


def is_overlap(x: tuple[np.ndarray, np.ndarray]) -> int:
    if set(range(x[0][0], x[0][1] + 1)).intersection(range(x[1][0], x[1][1] + 1)):
        return 1
    return 0


def main(part: Callable) -> None:
    with open("input.txt") as input:
        print(
            sum(
                map(
                    part,
                    map(str_to_range, input.readlines()),
                )
            )
        )


if __name__ == "__main__":
    main(is_overlap)
