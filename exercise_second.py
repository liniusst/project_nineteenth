# Create a class Smoothie and do the following:
#     Create an instance attribute called ingredients.
#     Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
#     Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.
#     Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.
# Then create two specific smotthies with specific ingredients (new classes) which inherits base Smoothie class and call all methods you implemented.
from typing import Dict

class Smoothie:
    def __init__(self, ingredients: Dict[str, float]) -> None:
        self.ingredients = ingredients

    def get_cost(self):
        """get_cost method which calculates the total cost of the ingredients used to make the smoothie."""
        cost = 0
        for item in self.ingredients:
            cost += my_dict.get(item)
        return cost

    def get_price(self):
        """get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places."""
        price = self.get_cost()
        sum = price + price * 1.5
        return sum

    def get_name(self) -> str:
        order_list = []
        for item in self.ingredients:
            order_list.append(item)
        order_list = sorted(order_list, reverse=False)
        order_list = ' '.join(order_list)
        return order_list
    
class BananaSmothie(Smoothie):
    def __init__(self) -> None:
        BANANA_SMOTHIE = {'banana', 'full-fat milk'}
        super().__init__(ingredients= BANANA_SMOTHIE)

class AppleSmothie(Smoothie):
    def __init__(self) -> None:
        APPLE_SMOTHIE = {'honey', 'milk', 'banana'}
        super().__init__(ingredients= APPLE_SMOTHIE)

my_dict = {'banana': 1, 'blueberries': 2, 'natural yogurt': 1.99, 'full-fat milk': 3, 'honey': 0.59, 'milk': 3.90,}

banana_smothie = BananaSmothie()
apple_smothie = AppleSmothie()

print(banana_smothie.get_cost())
print(banana_smothie.get_price())
print(banana_smothie.get_name())

print(apple_smothie.get_cost())
print(apple_smothie.get_price())
print(apple_smothie.get_name())