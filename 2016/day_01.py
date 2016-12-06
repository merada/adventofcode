import re
import sys

def main():
    ''' Santa's stars were stolen by the Easter Bunny!
        Find Easter Bunny HQ by following the instructions, given
        as input [direction][number_of_steps].
    '''

    pattern = re.compile(r"""
                            (?P<direction>[A-Z])(?P<steps>[0-9]+)
                          """, re.VERBOSE)
    instructions = sys.stdin.read()
    instructions = re.findall(pattern, instructions)
    instructions = map(lambda x: (x[0], int(x[1])), instructions)

    part_1(instructions)
    part_2(instructions)


def part_1(instructions):
    directions = [0,0,0,0] # North,East,South,West
    current_direction = 0 # North

    for i in instructions:
        current_direction = turn(i[0], current_direction)
        directions[current_direction] += i[1]

    # calculate distance from start using: abs(North - South) + abs(East - West)
    distance = abs(directions[0] - directions[2]) + abs(directions[1] - directions[3])

    print("PART_1: The Easter Bunny Headquarters are {} block(s) away.".format(distance))


def part_2(instructions):
    current_direction = 0 # North
    current_position = (0, 0)
    visited = set([current_position])

    for i in instructions:
        current_direction = turn(i[0], current_direction)

        for step in move(current_direction, i[1], current_position):
            if step in visited:
                print("PART_2: The real Easter Bunny Headquarters are {} block(s) away.".format(abs(step[0]) + abs(step[1])))
                return
            else:
                visited.add(step)
                current_position = step


def turn(direction, current_direction):
    if direction == "L":
        current_direction -= 1
        if current_direction < 0:
            current_direction += 4
    elif direction == "R":
        current_direction += 1
        if current_direction > 3:
            current_direction -= 4
    else:
        print("Error: direction " + d + " not valid")
        return -1
    return current_direction


def move(direction, distance, position):
    ''' Return step by step position
    '''
    for i in range(distance):
        if direction == 0: # North
            step = (0, 1)
        elif direction == 1: # East
            step = (1, 0)
        elif direction == 2: # South
            step = (0, -1)
        elif direction == 3: # West
            step = (-1, 0)
        else:
            step = (0, 0)

        position = tuple(sum(x) for x in zip(position, step))

        yield position


if __name__ == "__main__":
    main()
