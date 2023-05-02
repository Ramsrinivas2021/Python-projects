class animal():
    def sound(self):
        print("animal sounds as you mentioned")
class dog(animal):
    def sound(self):
        print("dog sounds 'bow bow'") 
class cow(dog):
    def sound(self):
        print("cow sounds 'Ambaa'")
class goat(cow):
    def eat(self):
        print("goat eats grass")
class cat(goat):
    def drink(self):
        print("cat drinks milk")

dog_instance = dog()
dog_instance.sound()

cow_instance = cow()
cow_instance.sound()

goat_instance =goat()
goat_instance.eat()

cat_instance =cat()
cat_instance.drink()

