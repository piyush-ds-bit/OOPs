import random

class Enemy:


    def __init__(self, name="Piyush",lives=3,hit_points=3):
        self._name = name
        self._lives = lives
        self._hit_points = hit_points
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points>=0:
            self._hit_points = remaining_points
            print("I took {} points damage and {} is left ".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} is dead".format(self))
                self._alive = False

    def __str__(self):
        return f"Name: {self._name}, Lives: {self._lives}, Hit Points: {self._hit_points}"





class Troll(Enemy):


    def __init__(self, name):
        super().__init__(name= name, lives= 1, hit_points=23)

    def grunt(self):
        print("Me {0._name}, {0._name} stomp you".format(self))

class Vampyre(Enemy):


    def __init__(self, name):
        super().__init__(name= name, lives= 3, hit_points= 12)

    def dodges(self):
        if random.randint(1, 3)==3:
            print("***** {0._name} dodges *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)

class VampyreKing(Vampyre):


    def __init__(self, name):
        super().__init__(name)
        
    def take_damage(self, damage):
        super().take_damage(damage // 4)

dracula = VampyreKing("Dracula")
while dracula._alive:
    dracula.take_damage(12)
    print(dracula)
