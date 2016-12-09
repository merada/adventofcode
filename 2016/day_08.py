import re
import sys

DISPLAY_WIDTH = 50
DISPLAY_HEIGHT = 6

def main():
    screen = [[0 for x in range(DISPLAY_WIDTH)] for x in range(DISPLAY_HEIGHT)]
    pattern = re.compile('(?P<orientation>(row|column)) [xy]=(?P<index>[0-9]+) by (?P<distance>[0-9]+)')

    for line in sys.stdin.readlines():
        instruction, args = line.split(' ', 1)

        if instruction == 'rect':
            X, Y = [int(x) for x in args.split('x')]
            for y in range(Y):
                for x in range(X):
                    screen[y][x] = 1
        elif instruction == 'rotate':
            match = pattern.match(args)
            index = int(match.group('index'))
            distance = int(match.group('distance'))
            orientation = match.group('orientation')

            if orientation == 'column':
                temp = [x[index] for x in screen]
                for i in range(DISPLAY_HEIGHT):
                    y = i + distance
                    if y >= DISPLAY_HEIGHT:
                        y -= DISPLAY_HEIGHT
                    screen[y][index] = temp[i]

            elif orientation == 'row':
                temp = [0 for x in range(DISPLAY_WIDTH)]
                for i in range(DISPLAY_WIDTH):
                    x = i + distance
                    if x >= DISPLAY_WIDTH:
                        x -= DISPLAY_WIDTH
                    temp[x] = screen[index][i]
                screen[index] = temp

            else:
                print ("Unknown instruction: {}.".format())
        else:
            print ("Unknown instruction: {}.".format(instruction))

    print "The number of lit pixels is {}.".format(count_pixels(screen))
    pretty_print(screen)


def print_screen(screen):
    for row in screen:
        print "".join(str(x) for x in row)


def pretty_print(screen):
    for row in screen:
        for i, val in enumerate(row):
            if (i + 1) % 5 == 0:
                print " ",
            elif val == 1:
                print '#',
            elif val == 0:
                print ' ',
        print ""


def count_pixels(screen):
    return sum(sum(x) for x in screen)


if __name__ == "__main__":
    main()
