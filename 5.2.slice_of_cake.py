"""
Writer: Ranel Ben Simman Tov, 315967703
"""


def get_recipe_price(prices, optionals=None, **ingredients):
    """
    Calculate the price of a recipe
    :param prices: a dictionary of ingredient prices
    :param optionals: a list of optional ingredients to ignore
    :param ingredients: the ingredients and their amounts
    :return: the total price of the recipe
    """
    total_price = 0.
    for ingredient, amount in ingredients.items():
        if not optionals or ingredient not in optionals:
            price_per_gram = prices.get(ingredient, 0) / 100
            total_price += price_per_gram * amount
    return total_price


# add some tests
def main():
    test1 = get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100)
    print(test1) #44
    test2 = get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)
    print(test2) #54
    test3 = get_recipe_price({})
    print(test3) #0


if __name__ == '__main__':
    main()