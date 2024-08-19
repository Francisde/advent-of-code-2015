from itertools import combinations_with_replacement


class Ingredient:

    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories


def get_max_score(recipes):
    max_score = 0
    for recipe in recipes:
        score = 0
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        calories = 0
        for ingredient_ in recipe:
            capacity += ingredients_dict[ingredient_].capacity
            durability += ingredients_dict[ingredient_].durability
            flavor += ingredients_dict[ingredient_].flavor
            texture += ingredients_dict[ingredient_].texture
            calories += ingredients_dict[ingredient_].calories
        capacity = max(0, capacity)
        durability = max(0, durability)
        flavor = max(0, flavor)
        texture = max(0, texture)
        score = capacity * durability * flavor * texture
        if calories == 500:
            max_score = max(max_score, score)
    return max_score

file1 = open('puzzle15.txt', 'r')
Lines = file1.readlines()

count = 0
ingredients = []
ingredients_dict = {}

for line in Lines:
    input_line= line.strip()
    input_line = input_line.replace(":", "")
    input_line = input_line.replace(",", "")
    print("Line {}: {}".format(count, input_line))
    count += 1
    string_split = input_line.split(" ")
    ingredient = Ingredient(string_split[0], int(string_split[2]), int(string_split[4]), int(string_split[6]), int(string_split[8]), int(string_split[10]))
    ingredients.append(ingredient.name)
    ingredients_dict[ingredient.name] = ingredient

print(ingredients)

all_possible_recies = list(combinations_with_replacement(ingredients, 100))
print(len(all_possible_recies))

max_score_of_all = get_max_score(all_possible_recies)
print("TASK 1 - max score: {}".format(max_score_of_all))

print("TASK 2 - ")