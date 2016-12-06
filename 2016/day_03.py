import sys
import re
from itertools import izip_longest

def main():
    part_1()
    #part_2()


def part_1():
    num_possible_triangles = 0

    for line in sys.stdin.readlines():
        T = map(int, re.findall('\d+', line))
        if is_valid_triangle(T):
            num_possible_triangles += 1

    print ("Part 1: The number of possible triangles is: {}.".format(num_possible_triangles))


def part_2():
    num_possible_triangles = 0
    triangles = []

    for line in sys.stdin.readlines():
        triangles.append(map(int, re.findall('\d+', line)))
    
    for i in range(0, len(triangles), 3): # for all triangles
        for j in range(3): # for each set of three
            T = []
            for k in range(3): # for each side
                T.append(triangles[i+k][j])
            if is_valid_triangle(T):
                num_possible_triangles += 1

    print ("Part 2: The number of possible triangles is: {}.".format(num_possible_triangles))


def is_valid_triangle(T):
    T.sort()
    if T[0] + T[1] > T[2]:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
