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

    directions = [0,0,0,0] # North,East,South,West
    current_direction = 0 # North
    current_position = (0,0)
    coordinates = set([current_position])
    real_distance = -1

    for i in instructions:
        current_direction = turn(i[0], current_direction)
        directions[current_direction] += i[1]
        current_position = move(directions)
        if current_position in coordinates:
            real_distance = calculate_distance(directions)
        else:
            coordinates.add(current_position)
            print(coordinates)
            print("\n\n\n")

    print("PART_1: The Easter Bunny Headquarters are {} block(s) away.".format(calculate_distance(directions)))
    if real_distance >= 0:
        print("PART_2: The real Easter Bunny Headquarters are {} block(s) away.".format(real_distance))
    else:
        print("PART_2: We haven't found the real Easter Bunny Headquarters yet!")


def calculate_distance(directions):
    ''' abs(North - South) + abs(East - West)
    '''
    return abs(directions[0] - directions[2]) + abs(directions[1] - directions[3])


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

def move(directions):
    ''' Return position calculated as [North - South, East - West]
    '''
    return ((directions[0] - directions[2]), (directions[1] - directions[3]))


if __name__ == "__main__":
    main()
