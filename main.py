class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to_floor(self, new_floor):
        if new_floor != int(new_floor) or not (1 <= new_floor <= self.number_of_floors):
            print("Такого этажа не существует")
        else:
            print(new_floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return 'Некорректные данные'

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return 'Некорректные данные'

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return 'Некорректные данные'

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return 'Некорректные данные'

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return 'Некорректные данные'

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return 'Некорректные данные'

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return 'Некорректные данные'

    def __radd__(self, value):
        return self.__add__(value)


    def __iadd__(self, value):
        return self.__add__(value)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__