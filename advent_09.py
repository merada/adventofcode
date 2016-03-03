import itertools
import sys
import re

def main():
    ''' Find the shortest and longest distance Santa can travel given a list of
        distances between cities, if he has to visit each city once, and
        only once.
    '''
    cities, distances = build_distance_matrix()
    possible_routes = itertools.permutations(cities.keys())
    shortest_distance = 65535
    longest_distance = 0

    for route in possible_routes:
        distance = 0
        for i in range(1, len(route)):
            start = cities[route[i-1]]
            end = cities[route[i]]
            distance += distances[start][end]
        if distance < shortest_distance:
            shortest_distance = distance
        if distance > longest_distance:
            longest_distance = distance

    print ("Santa's shortest distance is {}, and his longest distance is {}.".format(shortest_distance, longest_distance))

def build_distance_matrix():
    pattern = re.compile(r"""
                            (?P<start>[A-Za-z]+)\sto\s
                            (?P<end>[A-Za-z]+)\s=\s
                            (?P<distance>[0-9]+)
                            """, re.VERBOSE)
    cities = {}
    index = 0
    locations = {}
    for line in sys.stdin.readlines():
        match = pattern.match(line)

        start = match.group('start')
        end = match.group('end')
        distance = match.group('distance')

        if start not in cities:
            cities[start] = index
            index += 1
        if end not in cities:
            cities[end] = index
            index += 1
        locations[start, end] = int(distance)

    distance_matrix = [[0 for x in cities] for x in cities]
    for start, end in locations:
        distance = locations[start, end]
        start_index = cities[start]
        end_index = cities[end]
        distance_matrix[start_index][end_index] = distance
        distance_matrix[end_index][start_index] = distance

    return cities, distance_matrix

if __name__ == "__main__":
    main()
