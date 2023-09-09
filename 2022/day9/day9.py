from typing import List
from dataclasses import dataclass
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


tailPos = {}


def makeStep(direction: str, nodes: List[Point]):
    nodes[0].move(direction)
    for i in range(1, len(nodes)):
        updateTail(head=nodes[i - 1], tail=nodes[i])
    tailPos[f"{nodes[-1].x}_{nodes[-1].y}"] = 1


def updateTail(head: Point, tail: Point):
    delta_x = head.x - tail.x
    delta_y = head.y - tail.y

    if abs(delta_x) < 2 and abs(delta_y) < 2:
        return
    else:
        tail.y += np.sign(delta_y)
        tail.x += np.sign(delta_x)


# moves should have [Direction, Steps]
def processMove(moves: List[str], nodes: List[Point]):
    for _ in range(int(moves[1])):
        makeStep(moves[0], nodes)


def main():
    nodes = [Point(0, 0) for _ in range(0, 10)]
    with open("input") as input:
        for line in input:
            processMove(line.split(), nodes)
    print(len(tailPos.keys()))


if __name__ == "__main__":
    main()
