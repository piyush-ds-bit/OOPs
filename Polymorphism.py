class Wings:

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Mazzaa Ni !! life")
        elif self.ratio == 1:
            print("yee, bach gya CM")
        else:
            print("Jisko jo bhi milta hai..sabko sab nahi milta")


class Duck:

    def __init__(self):
        self._wing = Wings(1.8)

    def walk(self):
        print("Wadle, Wadle Wadle")

    def swim(self):
        print("Come on in ,the water is lovely here")

    def quack(self):
        print("Quack! Quack! Quack")

    def fly(self):
        self._wing.fly()


class Penguin:


    def walk(self):
        print("Wadle, Wadle, I Wadle too")

    def swim(self):
        print("Come on in ,but the water is bit chilly here")

    def quack(self):
        print("I don't quack, 'm a Penguin")


def test_duck(duck):
    duck.swim()
    duck.walk()
    duck.quack()

if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)
    donald.fly()

    poko = Penguin()
    test_duck(poko)
