import re
import itertools
import functools
from collections import defaultdict
from typing import Callable


def normalize_line(line: str) -> list[str]:
    line = re.sub("    ", "--- ", line)
    line = re.sub("]-", "] -", line)
    return line.strip("\n").split()


def get_ship_manifest(lines: list[str]) -> defaultdict:
    crates = defaultdict(list)
    any(
        map(functools.partial(update_crates, crates=crates), map(normalize_line, lines))
    )
    any(map(lambda x: crates[x].reverse(), crates.keys()))
    return crates


def update_crates(line: list[str], crates: defaultdict) -> None:
    any(map(functools.partial(check_crate, crates=crates), enumerate(line)))


def check_crate(crate: tuple[int, str], crates: defaultdict) -> None:
    if "-" not in crate[1]:
        crates[crate[0] + 1].append(crate[1])


def lift_9000(crates: defaultdict, f: int, to: int, n: int):
    for i in range(n):
        crates[to].append(crates[f].pop())


def lift_9001(crates: defaultdict, f: int, to: int, n: int):
    tmp = [crates[f].pop() for _ in range(n)]
    tmp.reverse()
    crates[to] += tmp


def file_head_generator(file):
    while True:
        line = file.readline()
        if "[" in line:
            yield line
            continue
        break


def main(pop: Callable) -> None:
    with open("input.txt") as input:
        crates = get_ship_manifest(file_head_generator(input))
        for line in input.readlines()[1:]:
            line = list(map(int, re.sub(r"[^0-9]", " ", line).split()))
            pop(crates, line[1], line[2], line[0])
        sorted_crates = [crates[x] for x in sorted(crates.keys())]
        print("".join([x.pop()[1] for x in sorted_crates]))


if __name__ == "__main__":
    main(lift_9001)
