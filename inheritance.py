class animal:
    def __inti__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hi(self):
        print("hi")

    def __str__(self):
        return "Animal"

class cat(animal):
    def __init__(self, name, age, sound):
        animal.__init__(name, age)
        # super().__init__(name, age)
        self.sound = sound
    
    def say_sound(self):
        print(self.sound)
    
    def __str__(self):
        return "cat:" + self.name

cat = cat("Someone on the internet", 5, "meow")
cat.say_hi()
cat.say_sound()
print(cat)