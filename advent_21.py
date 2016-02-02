import itertools
import math
import sys

def main():
    ''' In preparation for a boss fight, determine the minimum cost of items you can buy
        and still win, as well as the maximum cost you can buy and still lose.
    '''
    shop = {'weapons': [], 'armour': [], 'rings': []}
    boss = {}
    for line in sys.stdin.readlines():
        text = line.split(',')
        item_type = text[0]
        if item_type == 'Boss':
            boss = get_attributes(text[2:])
        else:
            shop[item_type].append(get_attributes(text[2:]))

    # set up shop - all valid combinations of items, including the option of no item
    shop['armour'].append(empty_item()) # 0-1 armour
    ring_combinations = itertools.combinations(shop['rings'], 2) # 0-2 rings
    for r in ring_combinations:
        shop['rings'].append(list(r))
    shop['rings'].append(empty_item())
    combinations = itertools.product(shop['weapons'], shop['armour'], shop['rings'])

    min_cost = math.inf
    max_cost = 0
    for c in combinations:
        player = calculate_player_attributes(empty_item(), c)
        player['hitpoints'] = 100
        boss['hitpoints'] = 100 
        if player_wins_fight(player, boss):
            if player['cost'] < min_cost:
                min_cost = player['cost']
        else:
            if player['cost'] > max_cost:
                max_cost = player['cost']

    print("Min cost of winning is {} gold.".format(min_cost))
    print("Max cost of losing is {} gold.".format(max_cost))

def get_attributes(attribute_list):
    attributes = {}
    for a in attribute_list:
        a = a.split(':')
        attributes[a[0].strip()] = int(a[1])
    return attributes

def empty_item():
    return {'damage': 0, 'armour': 0, 'cost': 0}

def calculate_player_attributes(player, configuration):
    for item in configuration:
        if isinstance(item, list):
            player = calculate_player_attributes(player, item)
        else:
            player['damage'] += item['damage']
            player['armour'] += item['armour']
            player['cost'] += item['cost']
    return player

def player_wins_fight(player, boss):
    ''' Returns true if the player wins, false otherwise '''
    while True:
        # player move
        boss['hitpoints'] -= max(1, player['damage'] - boss['armour'])
        if boss['hitpoints'] <= 0:
            return True
        # boss move
        player['hitpoints'] -= max(1, boss['damage'] - player['armour'])
        if player['hitpoints'] <= 0:
            return False

if __name__ == "__main__":
    main()
