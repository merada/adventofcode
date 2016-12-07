import re
import sys

def main():
    count_1 = 0 # for part 1
    count_2 = 0 # for part 2

    for line in sys.stdin.readlines():
        segments = re.split(r"[\[\]]", line.strip()) # even indices are supernet, odd indices are hypernet
        abba_supernet = False
        abba_hypernet = False
        aba_hypernet = False
        aba_set = set()

        # process supernet segments
        for segment in segments[::2]:
            N = len(segment)
            for i in range(N):
                if i <= (N - 4) and is_palindrome(segment[i:i+4]):
                    abba_supernet = True
                if i <= (N - 3) and is_palindrome(segment[i:i+3]):
                    aba_set.add((segment[i], segment[i+1]))

        # process hypernet segments
        for segment in segments[1::2]:
            N = len(segment)
            for i in range(N):
                if i <= (N - 4) and is_palindrome(segment[i:i+4]):
                    abba_hypernet = True
                if i <= (N - 3) and is_palindrome(segment[i:i+3]):
                    if (segment[i+1], segment[i]) in aba_set:
                        aba_hypernet = True

        if abba_supernet and not abba_hypernet:
            count_1 += 1
        if aba_hypernet:
            count_2 += 1

    print ("The number of IPs that support TLS is {}.".format(count_1))
    print ("The number of IPs that support SSL is {}.".format(count_2))


def is_palindrome(s):
    ''' A string is a palindrome if the second half of its characters
        is a mirror image of the first.
        Duplicate characters are not allowed.
    '''
    mid = len(s) / 2
    i = (len(s) % 2) - 1 # even strings include the midpoint

    is_palindrome = s[:mid] == s[:mid+i:-1] 
    has_unique_chars = len(s[:mid+i+1]) == len(set(s[:mid+i+1]))

    return is_palindrome and has_unique_chars


if __name__ == "__main__":
    main()
