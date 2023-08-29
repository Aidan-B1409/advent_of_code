from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# TODO - is there a soltion that doesn't involve globals?
head = Point(0, 0)
tail = Point(0, 0)
# Moves should be processed sequentially
# Move function should increase or decrease Point value based on coordinate and direction
# Assosciate dictionary of move functions with L R U D values (first column)
# Recursively process move within each function
# Parent function with a move type function as a parameter? 
# After each move, call checkTail function
# If x or y delta is greater than 2, move tail accordingly

moveset = {
        'R': stepRight,
        'L': stepLeft,
        'D': stepDown,
        'U': stepUp
        }

def stepUp(p: Point):
    p.y += 1


def stepDown(p: Point):
    p.y -=1


def stepRight(p: Point):
    p.x +=1


def stepLeft(p: Point):
    p.x -=1 


def makeStep(direction: str):
    moveset[direction](head)

# TODO - keep track of every unique position for tail move
# TODO - refactor for nicer solution that's not ugly if-else block
# ---- is boundary checking a good use case for pattern matching?
def updateTail():
    if head.x - tail.x > 2:
        pass
    # elif head.y: #...
    #     pass

# Should have [Direction, Steps]
def processMove(moves: List[str]):
    for step in range(int(moves[1])):
        makeStep(direction=moves[0])
        updateTail()
        # TODO - Refactor for nicer solution
        


def main():
    with open('input') as input:
        for line in input:
            processMove(line.split())


if __name__ == '__main__':
    main()
