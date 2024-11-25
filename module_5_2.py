class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        if 1 < new_floor <= self.number_of_floors:
            for floor in range(new_floor):
                print(floor + 1)
        else:
            print('Такого этажа не сущесвует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

h1 = House('ЖК Эльбрус', 10)
h2 = House('Акация', 20)

print(str(h1))
print(str(h2))

print(len(h1))
print(len(h2))