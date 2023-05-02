class MyClass():
    def add(self,a,b):
        self.total = a + b
        # print(self.total)

instance = MyClass()
instance.add(12,10)
print(instance.total)  # print total variable using instance
