import re
import sys

def main():
    ''' Reindeer races! Which reindeer is in the lead after a given number
        of seconds? Each reindeer can run at a different speed for some seconds, after
        which it has to rest.
    '''
    pattern = re.compile('''
                            (?P<name>[A-Za-z]+)[\sa-z]+
                            (?P<speed>[0-9]+)[\s/a-z]+
                            (?P<duration>[0-9]+)[\s,a-z]+
                            (?P<rest>[0-9]+)[\sa-z]+.
                            ''', re.VERBOSE)
    reindeer = {}
    for line in sys.stdin.readlines():
        match = pattern.match(line)

        reindeer[match.group('name')] = {'speed': int(match.group('speed')),
                                         'duration': int(match.group('duration')),
                                         'rest': int(match.group('rest')),
                                         'distance': 0}

    time = input("Please enter a time in seconds: ")
    find_winning_distance(reindeer, time)
    find_winning_points(reindeer, time)


def find_winning_distance(reindeer, time):
    ''' Determine the distance travelled by the winning reindeer, without
        taking leader bonuses into account.
    '''
    distances = []
    for name, r in reindeer.items():
        distance = 0
        time_r = 0 # cumulative time of reindeer's travel
        while time_r < time:
            time_r += r['duration']
            if time_r > time:
                distance += (time_r - time) * r['speed']
            else:
                distance += r['duration'] * r['speed']
            time_r += r['rest']
        distances.append(distance)

    print("The distance travelled by the winning reindeer is {} km.".format(max(distances)))


def find_winning_points(reindeer, time):
    ''' Determine the points accumulated by the winning reindeer, giving a
        bonus point to the current leading reindeer(s) for every second.
    '''
    max_distance = 0
    points = {name: 0 for name in reindeer}
    for t in range(time):
        # calculate distances
        for name, r in reindeer.items():
            is_moving = True if t % (r['duration'] + r['rest']) < r['duration'] else False
            if is_moving:
                r['distance'] += r['speed']
                if r['distance'] > max_distance:
                    max_distance = r['distance']

        # award points
        for name, r in reindeer.items():
            if r['distance'] == max_distance:
                points[name] += 1

    max_points = points[max(points, key=points.get)]
    print("The points accumulated by the winning reindeer is {}.".format(max_points))


if __name__ == "__main__":
    main()
