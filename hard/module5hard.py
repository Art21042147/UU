import time


class User:

    def __init__(self, nickname, password, age):
        if not isinstance(nickname, str):
            raise ValueError("Nickname must be a string")
        self.nickname = nickname

        if not isinstance(password, str):
            raise ValueError("Password must be a string")
        self.password = password

        if not isinstance(age, int):
            raise ValueError("Age must be an integer")
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password

    def __hash__(self):
        return hash((self.nickname, self.password))


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        self.title = title
        if not isinstance(duration, int):
            raise ValueError("Duration must be an integer")
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return
        print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *new_videos):
        for video in new_videos:
            if all(v.title != video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print("Видео не найдено")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for second in range(1, video.duration + 1):
            print(second, end=' ')
            time.sleep(1)
        print("Конец видео")
        video.time_now = 0


# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 5)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2025 года')
