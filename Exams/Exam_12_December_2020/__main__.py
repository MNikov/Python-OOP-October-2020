from project.factory.chocolate_factory import ChocolateFactory
recipe_name = 'mlechen'
recipe = {'kakao': 10, 'mlqko': 5}
cf = ChocolateFactory('fabrika', 100)
cf.add_recipe(recipe_name, recipe)
print(cf.recipes)
cf.make_chocolate(recipe_name)
print(cf.products)