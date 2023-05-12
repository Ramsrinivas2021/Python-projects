class Animal():
     def __init__(self) -> None:
         pass

class Dog(Animal):
    def __init__(self, my_food):
        self.food = my_food
    def serve_my_food(self):
        print("Dog can eat",self.food)

instance = Dog("Chicken")
instance1 = Dog("mutton")
instance2 = Dog("bisuits")
instance3 = Dog("some bones")
instance4 = Dog("rice")

# instance.serve_my_food()
# instance1.serve_my_food()
# instance2.serve_my_food()
# instance3.serve_my_food()
# instance4.serve_my_food()