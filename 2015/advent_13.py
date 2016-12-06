import itertools
import re
import sys

def main():
    ''' Find the optimal seating arrangement for a dinner party in which
        not everyone likes each other. Don't forget to include yourself.
    '''
    pattern = re.compile('''
                            (?P<first>[A-Za-z]+)[\sa-z]+
                            (?P<operator>lose|gain)\s
                            (?P<value>[0-9]+)[\sa-z]+
                            (?P<second>[A-Za-z]+).
                            ''', re.VERBOSE)

    guests = {}
    for line in sys.stdin.readlines():
        match = pattern.match(line)

        first = match.group('first')
        second = match.group('second')
        value = int(match.group('value'))
        if match.group('operator') == 'lose':
            value *= -1

        if first in guests:
            guests[first][second] = value
        else:
            guests[first] = {second: value}

    #Add myself
    name = "Merada"
    guests[name] = {}
    for g in guests:
        if g is not name:
            guests[g][name] = 0
            guests[name][g] = 0

    highest_happiness = 0
    for permutation in itertools.permutations(guests):
        happiness = 0
        for i, first in enumerate(permutation):
            if i == len(permutation) - 1:
                second = permutation[0]
            else:
                second = permutation[i + 1]
            happiness += guests[first][second] + guests[second][first]

        if happiness > highest_happiness:
            highest_happiness = happiness

    print "Highest happiness is {}.".format(highest_happiness)

if __name__ == "__main__":
    main()
