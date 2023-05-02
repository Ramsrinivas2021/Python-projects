from animal_class1 import Animal
from  dog_class1 import Dog
from cow_class1 import Cow
from goat_class1 import Goat


class Cat():
    def make_sound(self,sound):
        print("cat sounds like",sound)
cat_instance = Cat()
cat_instance.make_sound("meow meow")

animal_instance = Animal()
animal_instance.make_sound("no animal no sound")

dog_instance = Dog()
dog_instance.make_sound("bow bow")

cow_instance = Cow()
cow_instance.make_sound("Amba Amba")

goat_instance = Goat()
goat_instance.make_sound("mee mee")