import numpy as np
import math
import re
import sys

MAX_TSP = 100

def main():
    ''' Determine the highest valued cookie you can make with the given ingredients.
        The sum of ingredients should add to 100 teaspoons, and the cookie must have
        exactly 500 calories.
    '''

    ingredients = []
    calories = []
    for line in sys.stdin.readlines():
        text = re.split('[:,]+\s', line.strip())
        ingredients.append(np.array([int(x.split()[1]) for x in text[1:-1]]))
        calories.append(int(text[-1].split()[1]))
    calories = np.array(calories)

    # Assuming 4 ingredients, coefficients must add to 100 teaspoons
    coefficients = []
    for i in range(100):
        for j in range(100):
            if i + j > 100:
                # no valid coefficients, cut unnecessary loops
                break
            for k in range(100):
                if i + j + k > 100:
                    break
                l = 100 - i - j - k
                if i + j + k + l == 100:
                    c = np.array([i, j, k, l])
                    cals = np.multiply(c, calories)
                    if np.sum(cals) == 500:
                        coefficients.append(c)

    highest_score = 0
    for c in coefficients:
        score_arr = [0 for x in range(len(ingredients[0]))]
        for i, ingredient in enumerate(ingredients):
            # ingredient value = coefficient * property
            ingredient_value =  c[i] * ingredient
            score_arr = np.add(score_arr, ingredient_value)
        score_arr = np.clip(score_arr, 0, math.inf)
        score = np.prod(score_arr)
        if score > highest_score:
            highest_score = score

    print("The highest score is {}".format(highest_score))        

if __name__ == "__main__":
    main()
