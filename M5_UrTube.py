import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'Текущий пользователь: {self.nickname}'

    def __hash__(self):
        return hash(self.password)

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class Urtube:
    current_user = None
    def __init__(self):
        self.users = []
        self.videos = []

    def log_in(self, nickname, password):
        s = []
        for n in self.users:
            if nickname == n.nickname and password.__hash__() == n.password:
                s.append(1)
                self.current_user = n
                print(f'Вы успешно вошли в аккаунт {n.nickname}')
            else:
                s.append(0)
        if 1 not in s:
            print(f'Пользователь {nickname} не найден')

    def register(self, nickname, password, age):
        if self.users == []:
            user_new = User(nickname, hash(password), age)
            self.users.append(user_new)
            self.current_user = user_new
            print(f'Поздравляем! Вы наш первый пользователь и вы вошли в аккаунт {self.current_user.nickname}')
        else:
            nicknames_list =[]
            for n in self.users:
                nicknames_list.append(n.nickname)
            if nickname in nicknames_list:
                print(f'Пользователь "{nickname}" уже существует')
            else:
                user_new = User(nickname, hash(password), age)
                self.users.append(user_new)
                self.current_user = user_new
                print(f'Поздравляем! Теперь вы с нами. Вы вошли в аккаунт {self.current_user.nickname}')

    def log_out(self):
        print(f'{self.current_user} вышел из системы')
        self.current_user = None

    def add(self, *video_new):
        for v in video_new:
            self.videos.append(v)
            print(f'видео "{v.title}", добавлено в видеобиблиотеку')
        return self.videos

    def get_videos(self, word):
        w_l = word.lower()
        s = []
        for vid in self.videos:
            low_v = vid.title.lower()
            if w_l in low_v:
                s.append(vid.title)
        return s

    def watch_video(self, film):
        s = []
        for n in self.videos:
            if film == n.title:
                s.append(1)
            else:
                s.append(0)
        if 1 not in s:
            print(f'Видео с указанным названием не найдено')
        elif self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            for vid in self.videos:
                if film == vid.title:
                    t = vid.time_now+1
                    play_line = []
                    while t < vid.duration+1:
                        play_line.append(t)
                        print(t, end=' ')
                        time.sleep(1)
                        t +=1
            print('Конец видео')
            time.sleep(1)

    def __str__(self):
        return f'Пользователи: {self.users}'

if __name__ == '__main__':

# Создание экземпляра класса "UrTube"
    ur = Urtube()

# Создание экземпляров класса "Video"
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам перень программист?', 10, adult_mode=True)
    v3 = Video('Колобок-футболист - лучший из лучших', 99, time_now=10)

# Добавление видео
    ur.add(v1, v2, v3)

# Проверка поиска по слову
    print(ur.get_videos('луЧШий'))
    print(ur.get_videos('ПРОг'))

# Проверка просмотра видео без входа в систему
    ur.watch_video('Для чего девушкам перень программист?')
# Проверка регистрации нового (первого) пользователя и установка его в качестве текущего пользователя
    ur.register('Моржов', 'Хрен', 15)
# Проверка возрастного ценза при попытке просмотра видео
    ur.watch_video('Для чего девушкам перень программист?')
# Проверка ригистрации нового пользователя и установка его в качестве текущего пользователя
    ur.register('Криворучкин', 'Нэхайтак', 72)
# Проверка выхода из системы
    ur.log_out()
# Проверка входа с ошибочными данными
    ur.log_in('Криворучкин', 'Нэх')
# Проверка входа с верными данными
    ur.log_in('Криворучкин', 'Нэхайтак')
# Проверка просмотра видео при его наличии
    ur.watch_video('Для чего девушкам перень программист?')
# Попытка воспроизведения несуществующего видео
    ur.watch_video('Колобок-футболист - лучший')
# Проверка регистрации существующего пользователя
    ur.register('Криворучкин', 'sadfsdf', 90)
# Проверка вывода с методом __str__
    print(ur.current_user)
# Проверка хэширования пароля
    print(f'{ur.users[0].nickname}, hash-пароль: {ur.users[0].password}')
    print(f'{ur.users[1].nickname}, hash-пароль: {ur.users[1].password}')