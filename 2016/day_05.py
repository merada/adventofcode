import sys
import hashlib

def main():
    args = sys.stdin.read().split(' ')

    door_id = args[0]
    N = int(args[1]) # number of starting 0's
    zero_string = "".join('0' for x in range(N))
    index = 0
    password_1 = [] # for part 1
    password_2 = ['X'] * 8 # for part 2
    password_2_count = 0

    while password_2_count < 8:
        secret = hashlib.md5()
        secret.update(door_id + str(index))
        h = secret.hexdigest()

        if h[0:N] == zero_string:
            if len(password_1) < 8:
                password_1.append(h[5])
            if h[5].isdigit():
                i = int(h[5])
                if i < 8 and  password_2[i] == 'X':
                    password_2[i] = h[6]
                    password_2_count += 1

        index += 1

    print ("Part 1: The password is {}".format("".join(password_1)))
    print ("Part 2: The more secure password is {}".format("".join(password_2)))


if __name__ == "__main__":
    main()
