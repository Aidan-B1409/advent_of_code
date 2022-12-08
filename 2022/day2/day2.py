import pandas as pd

#             Rock Paper Scissors
# Rock         4     1      7
# Paper        8     5      2
# Scissors     3     9      6

#            Lose   Tie   Win
# Rock        3      4     8
# Paper       1      5     9
# Scissors    2      6     7
ruleset = pd.DataFrame.from_dict(
    {"i": ["X", "Y", "Z"], "A": [4, 8, 3], "B": [1, 5, 9], "C": [7, 2, 6]}
).set_index("i")

# part 2
winset = pd.DataFrame.from_dict(
    {"i": ["X", "Y", "Z"], "A": [3, 4, 8], "B": [1, 5, 9], "C": [2, 6, 7]}
).set_index("i")


def main():

    with open("input.txt") as input:
        print(
            sum(
                map(
                    lambda x: winset[x[0]][x[1]],
                    map(lambda x: x.strip("\n").split(), input.readlines()),
                )
            )
        )


if __name__ == "__main__":
    main()
