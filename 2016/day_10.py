import re
import sys

bots_input = {}
bots_input_stack = []
bots_output = {}

def main():
    pattern_input = re.compile("value (?P<value>[0-9]+) goes to (?P<bot>[a-z]+ [0-9]+)")
    pattern_output = re.compile("(?P<bot>[a-z]+ [0-9]+) gives low to (?P<low>[a-z]+ [0-9]+) and high to (?P<high>[a-z]+ [0-9]+)")

    for line in sys.stdin.readlines():
        match = pattern_input.match(line)
        if match:
            add_bot(match.group('bot'), int(match.group('value')))
            continue

        match = pattern_output.match(line)
        if match:
            bot = match.group('bot')
            if bot not in bots_output:
                bots_output[bot] = {
                    'low': match.group('low'),
                    'high': match.group('high')
                }

    while bots_input_stack:
        bot, values = bots_input_stack.pop()
        add_bot(bots_output[bot]['low'], values[0])
        add_bot(bots_output[bot]['high'], values[1])

    part_2 = 1
    for bot in bots_input:
        if bots_input[bot]['input'] == [17, 61]:
            print "Part 1: The bot responsible for comparing chips with value-17 and value-61 is {}.".format(bot)
        if bot == 'output 0' or bot == 'output 1' or bot == 'output 2':
            part_2 *= bots_input[bot]['input'][0]

    print "Part 2: The product of the values for outputs 0-2 is {}.".format(part_2)


def add_bot(bot, val):
    if bot in bots_input:
        bots_input[bot]['input'].append(val)
        bots_input_stack.append((bot, sorted(bots_input[bot]['input'])))
    else:
        bots_input[bot] = { 'input': [val] }


if __name__ == "__main__":
    main()
