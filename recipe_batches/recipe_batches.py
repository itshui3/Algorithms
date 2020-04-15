#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    rec_batches = []
    # if ingredients don't exist, return 0 
    # if ingredient count doesn't satisfy recipe restrictions, return 0
    # if ingredient both exists & satisfy the quantity value generate a batch count

    for key, item in recipe.items():
        if(ingredients.get(key, False) and ingredients[key] >= recipe[key]):
            rec_batches.append(ingredients[key] // recipe[key])
        else:
            return 0

    lowestDenom = rec_batches[0]

    for i in rec_batches:
        if(i < lowestDenom):
            lowestDenom = i

    return lowestDenom


recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 58, 'flour': 51 }

print(recipe_batches(recipe, ingredients))
if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))