import sys

def main():
    '''From a list of directions, determine how many unique houses Santa and his helper,
       RoboSanta, visit in a night, if the two Santas follow alternate directions.
    '''

    #current position of the two santas: pos[0] is Santa, and pos[1] is RoboSanta   
    pos = [[0, 0], [0, 0]]
    # locations visited
    visited = {(0, 0): 1}

    for i, d in enumerate(sys.stdin.read().strip()):
        santa = i % 2
        pos[santa] = move(d, pos[santa])
        visited[tuple(pos[santa])] = 1

    print len(visited)

def move(d, pos):
    '''Increment grid coordinate as per direction given.'''

    x, y = pos

    if d == '^':
        y += 1
    elif d == '>':
        x += 1
    elif d == 'v':
        y -= 1
    elif d == '<':
        x -= 1

    return x, y

if __name__ == "__main__":
    main()
