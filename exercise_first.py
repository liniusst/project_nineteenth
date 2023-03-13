from typing import List

class Person:
    """Check if Sam likes the food"""
    def __init__(self, name: str, foods_like: List[str], foods_hate: List[str] ) -> None:
        self.name = name
        self.foods_like = foods_like
        self.foods_hate = foods_hate

    def taste(self, food: str) -> None:
        """checking in which list it is and print is he like it or hate"""
        if isinstance(food, str) == True:
            if food in self.foods_like:
                print(f'{self.name} eats the {food} and loves it!')
            elif food in self.foods_hate:
                print(f'{self.name} eats the {food} and hates it!')
            else:
                print(f'{self.name} eats the {food}!')
        else:
            print("Given food is not string")

if __name__ == "__main__":
    p1 = Person("Sam", ["ice cream"], ["carrots"])
    p1.taste("ice cream")
    p1.taste("cheese")
    p1.taste("carrots")