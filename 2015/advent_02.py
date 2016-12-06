import sys

def main():
    '''How much wrapping paper and ribbon do Santa's elves need for all the presents?'''

    paper = 0
    ribbon = 0

    for line in sys.stdin.readlines():
        l, w, h = map(int, line.split('x'))

        # part 1
        sides = [l * w, l * h, w * h]
        surface_area = 2 * sum(sides)
        smallest_side = min(sides)
        paper += surface area + smallest_side

        # part 2
        volume = l * w * h
        dimensions = [l, w, h]
        ribbon += (sum(dimensions) - max(dimensions)) * 2 + volume

    print "Wrapping paper: " + str(paper)
    print "Ribbon: " + str(ribbon)

if __name__ == "__main__":
    main()
