import re
import sys

PATTERN = re.compile("\((?P<characters>[0-9]+)x(?P<frequency>[0-9]+)\)(?P<line>.*)")

def main():
    line = sys.stdin.read().strip()

    print ("Part 1: The length of the file using simple decompression is {}.".format(decompress_1(line)))
    print ("Part 2: The length of the file using recursive decompression is {}.".format(decompress_2(line)))


def decompress_1(string):
    decompressed = []

    while len(string) > 0:
        if string[0] == '(':
            match = PATTERN.match(string)
            frequency = int(match.group('frequency'))
            chars = int(match.group('characters'))
            line = match.group('line')
            repeated_chars = line[:chars]
            for f in range(frequency):
                decompressed.append(repeated_chars)
            string = line[chars:]
        else:
            decompressed.append(string[0])
            string = string[1:]

    return len("".join(decompressed))


def decompress_2(string):
    match = PATTERN.match(string)
    if match:
        frequency = int(match.group('frequency'))
        chars = int(match.group('characters'))
        line = match.group('line')
        return frequency * decompress_2(line[:chars]) + decompress_2(line[chars:])
    else:
        return len(string)


if __name__ == "__main__":
    main()
