import sys

def main():
    args = sys.stdin.read().split()
    data = args[0]
    disk_length = int(args[1])

    while len(data) < disk_length:
        data = dragon(data)

    checksum = data[:disk_length]
    while len(checksum) % 2 == 0:
        checksum = check(checksum)

    print "The checksum is ", "".join(checksum)


def dragon(string):
    a = string
    b = map(lambda x: '1' if x == '0' else '0', string[::-1])

    return a + "0" + "".join(b)   


def check(string):
    checksum = []

    for i in range(0, len(string) - 1, 2):
        if string[i] == string[i+1]:
            checksum.append('1')
        else:
            checksum.append('0')

    return checksum


if __name__ == "__main__":
    main()
