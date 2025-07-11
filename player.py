from multiprocessing.context import SpawnContext


class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives can not be negative")
            self._lives = 0

    lives = property(_get_lives, _set_lives)

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if self._level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("level can not be less than 1")

    level = property(_get_level, _set_level) # So insted of doing this,we can also use decorators as shown below !!!

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)

tim = Player("Tim")
print(tim.name)
print(tim.lives)
tim.lives -= 1
print(tim)
tim.lives -= 1
print(tim)
tim.lives -= 1
print(tim)
tim.lives -= 1
print(tim)

tim.level = 3
print(tim)
tim.score = 600
print(tim)
