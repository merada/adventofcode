import itertools
import sys

def main():
    ''' The elves ordered too many litres of eggnog! Given a list of container sizes
        available, determine how many combinations of containers can fit exactly 150
        litres. Then determine the minimum number of containers required, as well as
        how many combinations fulfill the minimum requirement.
    '''
    containers = []
    for line in sys.stdin.readlines():
        containers.append(int(line.strip()))

    # Part 1
    num_combinations = 0
    for i in range(len(containers)):
        combinations = itertools.combinations(containers, i)
        for c in combinations:
            if sum(c) == 150:
                num_combinations += 1

    print "The number of valid combinations is {}.".format(num_combinations)

    # Part 2
    for i in range(len(containers)):
        min_containers = 0
        num_combinations = 0
        combinations = itertools.combinations(containers, i)
        for c in combinations:
            if sum(c) == 150:
                min_containers = i
                num_combinations +=1
        if min_containers > 0:
            break

    print "The minimum number of containers is {}, which can be used {} times.".format(min_containers, num_combinations)


if __name__ == "__main__":
    main()
