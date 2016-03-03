import json
from pprint import pprint
import sys

def main():
    ''' The elves need help with their accounting. Balance their books (given as
        JSON input), by summing all the numbers but ignoring objects (dicts) that
        contain the value 'red', as these have been incorrectly counted twice.
    '''
    filename = sys.stdin.read().strip()
    with open(filename) as f:
        data = json.load(f)
    total = calculate_sum(data, dict)

    print ("The sum is {}.".format(total))


def calculate_sum(entry, entry_type):
    total = 0
    for value in entry:
        if entry_type is dict:
            value = entry[value]
        value_type = type(value)

        if value_type is int:
            total += value 
        elif value == 'red' and entry_type is dict:
            return 0
        elif value_type is dict:
            total += calculate_sum(value, value_type)
        elif value_type is list:
            total += calculate_sum(value, value_type)

    return total 


if __name__ == "__main__":
    main()
