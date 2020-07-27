import random

for i in range(3):
    random.random()

for i in range(3):
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return dice1, dice2


dice = Dice()
print(dice.roll())