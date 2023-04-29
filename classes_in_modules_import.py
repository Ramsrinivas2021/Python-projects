from classes_in_modules import MyClass

class MySubclass(MyClass):
    def add (self,a,b):
        super().add(a,b) 
        print(a + b)
subclass_instance = MySubclass()
subclass_instance .add(12,10)