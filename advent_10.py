import sys

def main():
    ''' Look-and-say:
        Compress a string of digits by prefixing a digit by the number of
        times it occurs. Repeat for a given number of iterations, using the
        output of the previous run as the input for the next.
    '''
    word = sys.argv[1] + 'x'
    iterations = int(sys.argv[2])

    for i in range(iterations):
        count = 1
        prev_c = None
        new_word = ""
        for c in word:
            if c == prev_c:
                count += 1
            elif prev_c is not None:
                new_word += str(count) + prev_c
                count = 1
            prev_c = c
        word = new_word + 'x'

    print("The word is {} characters long after {} iteration(s).".format(len(word[:-1]), iterations))

if __name__ == "__main__":
    main()
