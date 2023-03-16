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

