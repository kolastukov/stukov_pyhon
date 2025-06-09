#Создайте класс "Автомобиль", который содержит информацию о марке, модели и
#годе выпуска. Создайте класс "Грузовик", который наследуется от класса
#"Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
#"Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
#информацию о количестве пассажиров.

class Car:
    def __init__(self, brand, model, year_of_manufacture):
        self.brand = brand
        self.model = model
        self.year_of_manufacture = year_of_manufacture

    def info(self):
        print(f'Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year_of_manufacture}')

bmw = Car('bmw', 'bmw x7', '2019')
bmw.info()

class Passenger(Car):
    def __init__(self, brand, model, year_of_manufacture, capacity):
        super().__init__(brand, model, year_of_manufacture)
        self.capacity = capacity

    def info3(self):
        print(f'Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year_of_manufacture}, Вместительность: {self.capacity}')

passenger = Passenger('bmw', 'bmw x7', '2019', '8 человек')
passenger.info3()

class Truck(Car):
    def __init__(self, brand, model, year_of_manufacture, load_capacity):
        super().__init__(brand, model, year_of_manufacture)
        self.load_capacity = load_capacity

    def info2(self):
        print(f'Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year_of_manufacture}, Грузоподьёмность: {self.load_capacity}')

truck = Truck('bmw', 'bmw x7', '2019', '12 тонны')
truck.info2()
