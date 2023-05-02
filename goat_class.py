from cow_class import Cow

class Goat(Cow):
    def eat(self):
        super().sound()
        print("goat eats grass")

# goat_instance = goat()
# goat_instance.eat()