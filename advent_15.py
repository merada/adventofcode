import re
import sys

MAX_TSP = 100

def main():
    '''
    '''
    ingredients = {}
    coefficients = {}
    for line in sys.stdin.readlines():
        text = re.split('[:,]+\s', line.strip())
        ingredients[text[0]] = [x.split()[1] for x in text[1:]]
        coefficients[text[0]] = 0

    print ingredients
    print coefficients


if __name__ == "__main__":
    main()
