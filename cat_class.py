from goat_class import Goat

class Cat(Goat):
    def drink(self):
        super().eat()
        print("cat drinks milk")
cat_instance = Cat()
cat_instance.drink()