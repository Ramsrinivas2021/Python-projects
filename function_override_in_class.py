class MyClass:
    def add (self,a,b):
        print(a * b)

class MySubclass(MyClass):
    def add (self,a,b):
        super().add(a,b)
        print(a + b)
subclass_instance = MySubclass()
subclass_instance.add(12,10)
# MyClass_instance = MyClass()
# MyClass_instance.my_function()

