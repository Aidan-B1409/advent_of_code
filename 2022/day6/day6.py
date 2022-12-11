import itertools


def main(n: int):
    with open("input.txt") as input:
        buf = [x for x in input.read().strip("\n")]
        print(
            len(
                list(
                    itertools.takewhile(
                        lambda i: len(set(buf[i : i + n])) != n, range(len(buf))
                    )
                )
            )
            + n
        )


if __name__ == "__main__":
    main(14)
