import pandas as pd
import numpy as np


def main():
    with open("input.txt") as input:
        inventory = input.readlines()
    inventory = pd.to_numeric(pd.Series(inventory), errors="coerce", downcast="integer")
    # from https://stackoverflow.com/a/20088195/12146263
    mask = inventory.isnull()
    pos = np.where(mask)[0]
    pos -= np.arange(len(pos))
    inventory = [s.reset_index(drop=True) for s in np.split(inventory[~mask], pos)]
    sums = list(map(np.sum, inventory))
    # from https://stackoverflow.com/a/11530835/12146263
    # part 1 solution
    print(max((x, i) for i, x in enumerate(sums)))
    # part 2 solution
    print(np.sum(pd.Series(sums).nlargest(3)))


if __name__ == "__main__":
    main()
