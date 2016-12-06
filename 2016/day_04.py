import re
import sys
from operator import itemgetter

ROOM_NAME = 'northpole object storage'

def main():
    pattern = re.compile('''
                            (?P<name>[a-z-]+)-
                            (?P<sector_id>[0-9]+)
                            \[(?P<checksum>[a-z]+)\]
                         ''', re.VERBOSE)

    sum_sector_ids = 0
    for line in sys.stdin.readlines():
        match = pattern.match(line)

        room = { 'name': match.group('name'),
                 'sector_id': int(match.group('sector_id')),
                 'checksum': match.group('checksum') }

        if is_real(room):
            sum_sector_ids += room['sector_id']

        if is_equal_decrypted(ROOM_NAME, room):
            print ("The North Pole objects are stored in sector {}".format(room['sector_id']))

    print ("The sum of the sector IDs for all real rooms is {}.".format(sum_sector_ids))


def is_real(room):
    tallies = {}
    for c in room['name']:
        if c in tallies:
            tallies[c] += 1
        elif c is not '-':
            tallies[c] = 1

    sorted_tallies = []
    for t in tallies:
        sorted_tallies.append((t, tallies[t]))
    sorted_tallies.sort(key=lambda k: (-k[1], k[0]))

    valid_checksum = []
    for i in range(min(5, len(sorted_tallies))):
        valid_checksum.append(sorted_tallies[i][0])

    return ''.join(valid_checksum) == room['checksum']


def is_equal_decrypted(string, room):
    string = string.split(" ")
    secret = room['name'].split('-')
    N = len(string) # number of words

    # check if same number of words
    if N != len(secret):
        return False

    # check if each word is the same length
    for i in range(N):
        if len(string[i]) != len(secret[i]):
            return False

    # check for character equality
    for i in range(N):
        if string[i] != decrypt(secret[i], room['sector_id']):
            return False

    return True


def decrypt(secret, rotation):
    plaintext = []

    for c in secret:
        decrypted_c = ord(c) + rotation % 26
        if decrypted_c > ord('z'):
            decrypted_c = decrypted_c - ord('z') + ord('a') - 1
        plaintext.append(chr(decrypted_c))

    return "".join(plaintext)


if __name__ == "__main__":
    main()
