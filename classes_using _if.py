class Animal():
    def __init__(self, my_food, my_food1, my_food2):
        self.food = my_food
        self.food1 = my_food1
        self.food2 = my_food2

class Dog(Animal):
    def eats(self, food_choice):
        if food_choice == "food":
            print("dog eats", self.food)
        elif food_choice == "food1":
            print("dog eats", self.food1)
        elif food_choice == "food2":
            print("dog eats", self.food2)
        else:
            print("Invalid food choice")

dog_instance = Dog("chicken", "biscuits", "mutton")
dog_instance.eats("food")
