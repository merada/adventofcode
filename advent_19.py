from collections import defaultdict
import re
import sys

def main():
    ''' Determine the number of distinct molecules that can be created with one
        substitution, as well as how many substitutions are required to create the
        given molecule, starting at value 'e'.
    '''
    substitutions = defaultdict(list)
    for line in sys.stdin.readlines():
        line = line.strip().split(" => ")
        if len(line) == 2:
            substitutions[line[0]].append(line[1])
        else:
            molecule = line[0]

    num_distinct_molecules = count_distinct_molecules(substitutions, molecule)

    print("{} distinct molecules can be created.".format(num_distinct_molecules))

def count_distinct_molecules(substitutions, molecule):
    distinct_molecules = set()
    for old_chemical in substitutions:
        for new_chemical in substitutions[old_chemical]:
            regex = "(?={})".format(old_chemical)
            for match in re.finditer(regex, molecule):
                i = match.start()
                new_molecule = molecule[:i] + new_chemical + molecule[i+len(old_chemical):] 
                distinct_molecules.add(new_molecule)

    return sum(distinct_molecules)

if __name__ == "__main__":
    main()
