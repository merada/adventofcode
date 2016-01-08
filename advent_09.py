import sys
import re

def main():
    pattern = re.compile(r"""
                            (?P<start>[A-Za-z]+)\sto\s
                            (?P<end>[A-Za-z]+)\s=\s
                            (?P<distance>[0-9]+)
                            """, re.VERBOSE)

    locations = {}
    for line in sys.stdin.readlines():
        match = pattern.match(line)

        start = match.group('start')
        end = match.group('end')
        distance = match.group('distance')

        locations[start, end] = int(distance)

    # for each city as start node, find shortest path to any other city
    # take shortest distance

if __name__ == "__main__":
    main()
