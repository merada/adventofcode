import math
import sys

def main():
    ''' Santa's elves deliver presents by hand. For an infinite number of elves and an infinite
        row of houses, determine the first house to receive the given number of presents.
    '''
    num_presents = int(sys.stdin.read())
    #part_1(num_presents)
    part_2(num_presents)

def part_1(num_presents):
    ''' Sum of factors '''
    presents = num_presents / 10
    house_number = 0
    factors = []
    while sum(factors) < presents:
        house_number += 1
        factors = get_factors(house_number)

    print "The lowest house number to receive at least {} presents is {}.".format(num_presents, house_number)

def part_2(num_presents):
    ''' Lazy elves that only hand out presents to 50 houses, but they hand out 11 to
        compensate.
    '''
    house_number = 0
    factors = []
    while True:
        house_number += 1
        factors = get_factors(house_number)
        presents = 0
        valid_factors = []
        for f in factors:
            if house_number / f <= 50:
                presents += 11 * f
                valid_factors.append(f)
        if presents >= num_presents:
            break
    
    print "The lowest house number to receive at least {} presents is {}.".format(num_presents, house_number)

def get_factors(n):
    factors = set([1])
    # calculate upper bound so that previous factors are not reconsidered
    # (median factor is never more than the square root of the number)
    upper_bound = int(math.sqrt(n)) + 1
    for i in range(1, upper_bound):
        if n % i == 0:
            factors.add(i)
            factors.add(n / i)
    return factors

if __name__ == "__main__":
    main()
