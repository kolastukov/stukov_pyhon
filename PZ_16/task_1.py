#Создайте класс "Машина" с атрибутами "марка", "модель" и "год выпуска".
#Напишите метод, который выводит информацию о машине в формате
#"Марка:марка, Модель: модель, Год выпуска: год".
class Car:
    def __init__(self, brand, model, year_of_manufacture):
        self.brand = brand
        self.model = model
        self.year_of_manufacture = year_of_manufacture

    def info(self):
        print(f'Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year_of_manufacture}')

bmw = Car('bmw', 'bmw x7', '2019')
bmw.info()



