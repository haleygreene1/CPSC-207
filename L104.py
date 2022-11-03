#the authors' name are: Holly, Haley and Anna

red_velvet_cake = {"flour": 2.5, "sugar": 1.5, "baking soda": 1, "salt":1, "cocoa powder": 1, "vegetable oil": 1.5, "buttermilk": 1, "eggs":2,"red food coloring": 2, "vinegar":1, "vanilla": 1, "cream cheese": 3 }

lemon_cake= {"flour": 1.5, "baking powder": 1.5, "lemon zest":1, "salt": 0.5, "butter": 0.5, "sugar": 1, "eggs": 2, "vanilla": 1, "lemon juice": 2, "buttermilk": 0.5}

def similar_ingredients (recipe1, recipe2):
    match= []
    for ingredient in recipe1:
        if ingredient in recipe2:
            match.append(ingredient)
    print("These ingredients are in both recipes: \n", match)

similar_ingredients (red_velvet_cake, lemon_cake)
