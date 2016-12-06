import sys
import re

def main():
    ''' For a given set of strings and encodings, determine:
        1. The number of characters of code for string literals minus the number of
           characters in memory for the values of the strings.
        2. The number of characters for an expanded encoding minus the
           number of characters in the original code.
           
    '''

    code = 0
    characters = 0
    expanded_encoding = 0

    for line in sys.stdin.readlines():
        line = line.strip()
        code += len(line)

        # part 1
        line1 = line[1:-1] # strip outer quotations
        line1 = re.sub(r'\\x[0-9][0-9]', "a", line1)
        line1 = line1.replace("\\\\", "a")
        line1 = line1.replace("\\\"", "a")
        characters += len(line1)
        print "{}  :  {} {}".format(line, line1, len(line1))
        # part 2
        line2 = line.replace("\\", "\\\\")
        line2 = line2.replace("\"", "\\\"")
        expanded_encoding += len(line2) + 2

    print "Code less characters: {}".format(code - characters)
    print "Expanded encoding less original code: {}".format(expanded_encoding - code)

if __name__ == "__main__":
    main()
