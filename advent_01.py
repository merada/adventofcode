import sys

def main():
    '''From the given instructions, determine on which floor Santa ends and at which
       instruction he first goes below ground level.'''

    instructions = sys.stdin.read().strip()

    for i in instructions:
        index += 1
        if i == '(':
            floor += 1
        elif i == ')':
            floor -= 1

        # part 2
        if floor < 0:
            print "Santa goes underground at instruction index {}".format(index)

    # part 1
    print "Santa ends on floor {}.".format(floor)

if __name__ == "__main__":
    main()
