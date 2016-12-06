import sys

def main():
    tallies = []

    for line in sys.stdin.readlines():
        line = line.strip()
        if len(tallies) == 0:
            for c in line:
                tallies.append({ c: 1 })
        else:
            for i, c in enumerate(line):
                if c in tallies[i]:
                    tallies[i][c] += 1
                else:
                    tallies[i][c] = 1

    max_repetitions = []
    min_repetitions = []

    for i in range(len(tallies)):
        max_repetitions.append((0,0))
        min_repetitions.append((0,sys.maxint))

        while tallies[i]:
            key, val = tallies[i].popitem()
            if val > max_repetitions[i][1]:
                max_repetitions[i] = (key, val)
            if val < min_repetitions[i][1]:
                min_repetitions[i] = (key, val)

    print ("The error-corrected version of the code with max-repetition is '{}'.".format("".join(x[0] for x in max_repetitions)))
    print ("The error-corrected version of the code with min-repetition is '{}'.".format("".join(x[0] for x in min_repetitions)))


if __name__ == "__main__":
    main()
