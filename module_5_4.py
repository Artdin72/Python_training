class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        if args[0] not in cls.houses_history:
            cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __del__(self):
        return print(f'"{self.name}" снесён, но он останется в истории')

h1 = House('Мечта', 15)
print(House.houses_history)
h2 = House('Простоквашино', 3)
print(House.houses_history)
h3 = House('Мир', 25)
print(House.houses_history)
h4 = House('Небо', 16)

print(House.houses_history) # Список "История строительства". Атрибут класса "House"

del h2 # удаление объекта "Простоквашино"

print(House.houses_history) # Список "История строительства". Атрибут класса "House"