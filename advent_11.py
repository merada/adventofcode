import sys

FORBIDDEN_CHARS = [ord('i'), ord('o'), ord('l')]

def main():
    ''' Find a new password for Santa!
        Valid passwords are 8 characters long, don't contain any of the letters
        'i', 'o' and 'l', contain at least two double characters, and at least
        one incrementing sequence.
        
    '''
    password = [ord(c) for c in sys.argv[1]][::-1]
    while True:
        increment(password)
        if is_valid(password):
            break

    print "The next valid password is: {}".format(''.join(map(chr, password[::-1])))

def increment(word):
    for i, c in enumerate(word):
        if c == ord('z'):
            word[i] = ord('a')
        else:
            word[i] = c + 1
            # skip invalid series to avoid unnecessary computation
            if word[i] in FORBIDDEN_CHARS:
                word[i] += 1
            break

def is_valid(word):
    prev_c = None
    doubles = 0
    sequence = False
    for i, c in enumerate(word):
        # forbidden chars
        if c in FORBIDDEN_CHARS:
            return False
        # double chars
        if c == prev_c:
            doubles += 1
            prev_c = None # to stop overlapping
        else:
            prev_c = c
        # sequential chars (remember the word is backwards)
        if i > 1 and word[i-2] == word[i] + 2 and word[i-1] == word[i] + 1:
            sequence = True

    return sequence if doubles > 1 else False

if __name__ == "__main__":
    main()
