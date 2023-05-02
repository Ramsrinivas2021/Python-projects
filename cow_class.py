from dog_class import Dog

class Cow(Dog):
    def sound(self):
        super().sound()
        print("cow sounds 'Ambaa'")
