import re
import sys

MYSTERY_SUE = {'children': 3,
               'cats': 7,
               'samoyeds': 2,
               'pomeranians': 3,
               'akitas': 0,
               'vizslas': 0,
               'goldfish': 5,
               'trees': 3,
               'cars': 2,
               'perfumes': 1}

def main():
    ''' Determine which of your 500 Aunt Sues sent you the gift!
    '''
    sue = {}
    for line in sys.stdin.readlines():
        text = re.split('[:,]+\s', line.strip())
        sue[text[0]] = {}
        compounds = text[1::2]
        values = text[2::2]
        for i, c in enumerate(compounds):
            sue[text[0]][c] = int(values[i])
            
    for s in sue:
        valid = True
        for compound in sue[s]:
            s1 = sue[s][compound]
            s2 = MYSTERY_SUE[compound]
            if is_valid(compound, s1, s2):
                pass
            else:
                valid = False
                break
        if valid:
             print s

def is_valid(compound, s1, s2):
    if (compound == "cats" or compound == "trees"):
        if s1 <= s2:
            return False
    elif (compound == "pomeranians" or compound == "goldfish"):
        if s1 >= s2:
            return False
    elif s1 != s2:
        return False

    return True

if __name__ == "__main__":
    main()
