import sys
from operator import add

def main():
    #part_1()
    part_2()


def part_1():
    directions = {'U':-3, 'D':3, 'L':-1, 'R':1}
    position = 5
    code = []
    for line in sys.stdin.readlines():
        for i in line.strip():
            if is_on_keypad(position, directions[i]):
                position += directions[i]
        code.append(position) 

    print("The code is {}.".format(''.join(str(x) for x in code)))

fancy_keypad = [['X', 'X', '1', 'X', 'X'],
                ['X', '2', '3', '4', 'X'],
                ['5', '6', '7', '8', '9'],
                ['X', 'A', 'B', 'C', 'X'],
                ['X', 'X', 'D', 'X', 'X']]

def part_2():
    directions = {'U':[-1, 0], 'D':[1, 0],
                  'L':[0, -1], 'R':[0, 1]}
    position = [2,0] # corresponds to value 5
    code = []
    for line in sys.stdin.readlines():
        for i in line.strip():
            new_position = map(add, position, directions[i])
            if is_on_fancy_keypad(new_position):
                position = new_position
        code.append(fancy_keypad[position[0]][position[1]])

    print("The code is {}.".format(''.join(code)))


def is_on_keypad(position, direction):
    ''' Movements are valid only if they fall within a keypad of the form
        123
        456
        789
        I.e. transition from 3 to 4 and vice versa is illegal.
    '''
    new_position = position + direction
    if new_position < 1 or new_position > 9:
        return False
    elif position in [1,4,7] and direction == -1:
        return False
    elif position in [3,6,9] and direction == 1:
        return False
    else:
        return True


def is_on_fancy_keypad(position):
    ''' Movements are valid only if they fall within the fancy keypad
            1
          2 3 4
        5 6 7 8 9 
          A B C
            D
        Using a 2D array, moves are valid if the resulting position has valid coordinates
        in both row and column, and does not contain the value 'X'
    '''
    if position[0] < 0 or position[0] > 4:
        return False
    elif position[1] < 0 or position[1] > 4:
        return False
    elif fancy_keypad[position[0]][position[1]] == 'X':
        return False
    else:
        return True


if __name__ == "__main__":
    main()
