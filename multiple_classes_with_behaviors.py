class animal():
    def sound(self):
        print("animal sounds as you mentioned")
class dog(animal):
    def func(self):
        print("dog food")
    def sound(self,sound):
        print("dog sounds",sound) 
    def eats(self,myfood):
        self.dog_food = myfood
        print("dog eats",self.dog_food)
        # print(self.dog_food)
    def my_food(self):
        print(self.dog_food)

class cow(dog):
    def sound(self,sound):
        print("cow sounds",sound)
    def eats(self,eats):
       print("cow eats",eats)  
class goat(cow):
    def eat(self,eats):
        print("goat eats",eats)
    def sound(self,sound):
       print("goast sounds",sound) 
class cat(goat):
    def sound(self,sound):
        print("cat sounds",sound)
    def drinks(self,drinks):
        print("cat drinks",drinks)

# dog_instance = dog()
# dog_instance.eats('chicken')
dog_instance2 = dog()
print(dog_instance2.eats('chicken'))
dog_instance2.my_food()
# dog_instance.eats("mutton too")

# cow_instance = cow()
# cow_instance.eats("grass")
# cow_instance.sound("Amba Amba")
# cow_instance.eats("rice too")


# goat_instance =goat()
# goat_instance.eat("grass")
# goat_instance.sound("me me")

# cat_instance =cat()
# cat_instance.drinks("milk")
# cat_instance.sound("meow meow")

