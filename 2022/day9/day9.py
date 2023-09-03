from dataclasses import dataclass
from typing import List
import numpy as np


@dataclass
class Point:
    x: int
    y: int

    def move(self, dir: str):
        match dir:
            case "R":
                self._stepRight()
            case "L":
                self._stepLeft()
            case "D":
                self._stepDown()
            case "U":
                self._stepUp()

    def _stepUp(self):
        self.y += 1

    def _stepDown(self):
        self.y -= 1

    def _stepRight(self):
        self.x += 1

    def _stepLeft(self):
        self.x -= 1

         
# TODO - is there a soltion that doesn't involve globals?
# head = Point(0, 0)
# tail = Point(0, 0)
tailPos = {"0_0": 1}


def makeStep(direction: str, node: Point):
    node.move(direction)

# TODO - keep track of every unique position for tail move
def updateTail():
    delta_x = head.x - tail.x
    delta_y = head.y - tail.y

    if abs(delta_x) < 2 and abs(delta_y) < 2:
        return
    else:
        tail.y += np.sign(delta_y)
        tail.x += np.sign(delta_x)
    tailPos[f"{tail.x}_{tail.y}"] = 1

# Should have [Direction, Steps]
def processMove(moves: List[str], nodes: List[Point]):
    for step in range(int(moves[1])):
        makeStep(moves[0], nodes[0])
        updateTail()


def main():
    nodes = [Point(0, 0) for _ in range(0, 2)]
    print(len(nodes))
    with open("input") as input:
        for line in input:
            processMove(line.split(), nodes)
    print(len(tailPos.keys()))


if __name__ == "__main__":
    main()
