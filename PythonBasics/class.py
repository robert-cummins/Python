class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def talk(self):
        print(f"Hi, my name is {self.name}. I'm {self.age} years old and I'm from {self.nationality}")


robert = Person('Robert', 30, "Ireland")
beth = Person('Beth', 30, "New Zealand")
robert.talk()
beth.talk()