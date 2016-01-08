import sys

def main():
    '''Using a set of rules, determine which strings are naughty and which are nice.'''
    nice = 0

    for line in sys.stdin.readlines():
        x = line[0]
        y = line[1]
        doubles = {(x + y): 0}
        double = False
        trio = False
        for i, z in enumerate(line[2:]):
            if y + z in doubles:
                if doubles[y + z] != i:
                    double = True
            else:
                doubles[y + z] = i + 1
            if x == z:
                trio = True
            x = y
            y = z

        if double and trio:
            nice += 1

    print nice

if __name__ == "__main__":
    main()
