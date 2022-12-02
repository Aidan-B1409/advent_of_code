import pandas as pd

element_scores = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3

}
#             Rock Paper Scissors
# Rock         4     1      7    
# Paper        8     5      2
# Scissors     3     9      6
ruleset = pd.DataFrame.from_dict({
    'i': ['X', 'Y', 'Z'],
    'A': [4, 8, 3],
    'B': [1, 5, 9],
    'C': [7, 2, 6]
}).set_index('i')


# A = 65
# B = 66
# C = 67

# A - B
round_scores = {
    'Lose': 0,
    'Draw': 3,
    'Win': 6
}

encryption = {
    'Rock': ('A', 'X'),
    'Paper': ('B', 'Y'),
    'Scissors': ('C', 'Z')
}

def main():
    sum = 0
    print(ruleset)
    with open('input.txt') as strategy_guide:
        for line in strategy_guide.readlines():
           l2 = line.strip('\n').split()
           sum += ruleset[l2[0]][l2[1]]
    print(sum)


if __name__ == '__main__':
    main()
