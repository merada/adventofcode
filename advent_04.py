import sys
import hashlib

def main():
    '''Find the first MD5 hash for a secret key starting with a given number of zeros (6).'''

    secret_key = sys.stdin.read().strip()
    number = 0

    while True:
        secret = hashlib.md5()
        secret.update(secret_key + str(number))
        h = secret.hexdigest()

        if h.startswith("000000"):
            print number
            break
        else:
            number += 1

if __name__ == "__main__":
    main()
