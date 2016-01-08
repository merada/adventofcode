import sys
import re

def main():
    ''' Use Santa's lighting instructions to decorate your house, and determine
        the total brightness of the lit lights.
    '''

    grid = [[0 for x in range(1000)] for x in range(1000)]
    pattern = re.compile(r"""
                            (?P<instruction>([a-z]+[\sa-z]*))
                            (?P<x0>[0-9]+),(?P<y0>[0-9]+)
                            \sthrough\s
                            (?P<x1>[0-9]+),(?P<y1>[0-9]+)
                            """, re.VERBOSE)

    for line in sys.stdin.readlines():
        match = pattern.match(line)

        instruction = match.group("instruction").strip()
        start = [int(match.group("x0")), int(match.group("y0"))]
        end = [int(match.group("x1")), int(match.group("y1"))]

        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                if instruction == "turn on":
                    grid[x][y] += 1
                elif instruction == "turn off":
                    grid[x][y] -= 1
                    if grid[x][y] < 0:
                        grid[x][y] = 0
                elif instruction == "toggle":
                    grid[x][y] += 2

    print sum([sum(x) for x in grid])

if __name__ == "__main__":
    main()
