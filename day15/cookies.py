import itertools

class Ingredient:
    def __init__(self, capacity, durability, flavor, texture, calories):
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

def cookies(text, targetCalories):
    ingredients = []
    with open(text, 'r') as file:
        for line in file.readlines():
            line = line.split(" ")
            # Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
            ingredients.append(Ingredient(int(line[2][:-1]), int(line[4][:-1]), int(line[6][:-1]), int(line[8][:-1]), int(line[10])))
    maxYumness = 0
    for permutation in itertools.permutations(range(1,100), len(ingredients)):
        if sum(permutation) == 100:
            cookie = Ingredient(0,0,0,0,0)
            for i, ingredient in enumerate(ingredients):
                cookie.capacity += ingredient.capacity * permutation[i]
                cookie.durability += ingredient.durability * permutation[i]
                cookie.flavor += ingredient.flavor * permutation[i]
                cookie.texture += ingredient.texture * permutation[i]
                cookie.calories += ingredient.calories * permutation[i]
            if cookie.capacity > 0 and cookie.durability > 0 and cookie.flavor > 0 and cookie.texture > 0 and cookie.calories == targetCalories:
                yumness = cookie.capacity * cookie.durability * cookie.flavor * cookie.texture
                maxYumness = yumness if yumness > maxYumness else maxYumness
    return maxYumness


if __name__ == "__main__":
    print(cookies("input.txt", 500))