import re
import sys

def main():
    ''' Determine signal values for a set of wires connected to bitwise logic gates,
        as given by an intruction set.

        Instruction examples:
        123 -> x
        x AND y -> d
        x OR y -> e
        x LSHIFT 2 -> f
        NOT x -> h
    '''

    pattern = re.compile(r"""
                            (?P<input1>[0-9a-z]*)\s*
                            (?P<gate>[A-Z]*)\s*
                            (?P<input2>[0-9a-z]*)\s->\s
                            (?P<output>[a-z]+)
                            """, re.VERBOSE)

    instructions = []
    for line in sys.stdin.readlines():
        match = pattern.match(line)
        instructions.append({
                            'input1': match.group("input1"),
                            'input2': match.group("input2"),
                            'gate': match.group("gate"),
                            'output': match.group("output")})

    signals = {}
    max_16bit = 65535
    while len(instructions) > 0:
        print len(instructions)
        for i in instructions:
            l = get_input(i['input1'], signals)
            r = get_input(i['input2'], signals)
            if l is not None and r is not None:
                if i['gate'] == 'AND':
                    signals[i['output']] = l & r
                elif i['gate'] == 'OR':
                    signals[i['output']] = l | r
                elif i['gate'] == 'NOT':
                    signals[i['output']] = (~r) & max_16bit
                elif i['gate'] == 'LSHIFT':
                    signals[i['output']] = l << r
                elif i['gate'] == 'RSHIFT':
                    signals[i['output']] = l >> r
                else: # no gate
                    signals[i['output']] = l
                instructions.remove(i)

    for i in instructions:
        print i

    print signals['a']


def get_input(i, signals):
    if is_number(i):
        return int(i)
    elif i in signals:
        return signals[i]
    elif i == "":
        return i
    else:
        return None


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
