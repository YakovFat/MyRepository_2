import datetime
import time


class DaTi:

    def __enter__(self):
        now = datetime.datetime.now().time()
        start_time = time.time()
        self.start_time = start_time
        self.now = now
        print(now)

    def __exit__(self, type, value, traceback):
        old = datetime.datetime.now().time()
        self.old = old
        print(old)
        print(time.time() - self.start_time)


with DaTi() as c:
    class Animal:
        feed = 'Не покормлен'

        def __init__(self, name, weight, voice):
            self.name = name
            self.weight = weight
            self.voice = voice

        def feeds(self):
            self.feed = 'Покормлен'

        def collect_stuff(self):
            pass


    class Bird(Animal):
        collect = 'Не собраны'

        def collect_stuff(self):
            super().collect_stuff()
            self.collect = 'Собраны'


    class Dairy_cattle(Animal):
        milk = 'Не подоена'

        def collect_stuff(self):
            super().collect_stuff()
            self.milk = 'Подоена'


    class Wool(Animal):
        cut = 'Не подстрижена'

        def collect_stuff(self):
            super().collect_stuff()
            self.cut = 'Подстрижена'


    goose_1 = Bird('Серый', 12, 'гагага')
    goose_2 = Bird('Белый', 8, 'гагага')
    duck = Bird('Кряква', 3, 'кряяя')
    chicken_1 = Bird('Ко-Ко', 3.1, 'кококо')
    chicken_2 = Bird('Кукареку', 2.5, 'кококо')
    cow = Dairy_cattle('Манька', 512, 'мууу')
    goat_1 = Dairy_cattle('Рога', 50, 'меее')
    goat_2 = Dairy_cattle('Копыта', 45, 'меее')
    sheep_1 = Wool('Барашек', 90, 'беее')
    sheep_2 = Wool('Кудрявый', 92, 'беее')

    paddock = []
    paddock.append(goose_1)
    paddock.append(goose_2)
    paddock.append(duck)
    paddock.append(chicken_1)
    paddock.append(chicken_2)
    paddock.append(cow)
    paddock.append(goat_1)
    paddock.append(goat_2)
    paddock.append(sheep_1)
    paddock.append(sheep_2)

    tmp = 0
    for animal in paddock:
        tmp += animal.weight
    print("Общий вес животных:", tmp)

    maximum = 0
    max_name = 0
    for animal in paddock:
        if animal.weight >= maximum:
            maximum = animal.weight
            max_name = animal.name
    print("Самое большое по весу животное:", max_name)

    for padd in paddock:
        padd.collect_stuff()

    print(goose_1.collect)
    print(cow.milk)
    print(sheep_2.cut)
