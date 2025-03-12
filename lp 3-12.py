class Budget:
    def __init__(self, food, clothing, entertainment, rent):
        self.food = food
        self.clothing = clothing
        self.entertainment =entertainment
        self.rent = rent
        self.budget = 0
        self._perments = [0]*4

    def _get_percent(self, number):
        return round(number/self, number) * 100,2
    
    def calculate(self):
        self.budget = self.food + self.clothing + self.entertainment + self.rent
        self._perments[0] = self._percent(self.food)
        self._perments[1] = self._percent(self.clothing)
        self._perments[2] = self._percent(self.entertainment)
        self._perments[3] = self._percent(self.rent)

    def display(self):
        print("category\t\tBudget")
        print(f"food {self._get_percent[0]}")
        print(f"clothing {self._get_percent[0]}")
        print(f"Entertainment {self._get_percent[0]}")
        print(f"rent {self._get_percent[0]}")
        print(f"food' {self._get_percent[0]}")

def main():
    print("Enter the number spent last month")
    food = float(input("food:"))
    clothing = float(input("clothing"))
    entertainment = float(input("entertainment:"))
    rent = float(input("rent:"))
    print()
    
    spending = Budget(food, clothing, entertainment, rent)
    spending.calculate()
    spending.display()
    pass
