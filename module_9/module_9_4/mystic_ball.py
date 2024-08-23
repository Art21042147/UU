from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Ну да', 'Да нет', 'Почти', 'Иногда')
print(first_ball())
print(first_ball())
print(first_ball())
