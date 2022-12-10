def nord(s: str) -> int:
    if s.islower():
        return ord(s) - 96
    return ord(s) - 38


def part1():
    with open("input.txt") as input:
        print(
            sum(
                map(
                    nord,
                    map(
                        lambda y: "".join(
                            set(y[: (int(len(y) / 2))]).intersection(
                                y[(int(len(y) / 2)) :]
                            )
                        ),
                        map(lambda x: x.strip("\n"), input.readlines()),
                    ),
                )
            )
        )


def part2():

    with open("input.txt") as input:
        n = len(input.readlines())
        input.seek(0)
        print(
            sum(
                map(
                    nord,
                    map(
                        lambda y: "".join(set(y[0]).intersection(*y[0:])),
                        map(
                            list,
                            it.divide(
                                int(n / 3),
                                map(lambda x: x.strip("\n"), input.readlines()),
                            ),
                        ),
                    ),
                )
            )
        )


if __name__ == "__main__":
    part2()
