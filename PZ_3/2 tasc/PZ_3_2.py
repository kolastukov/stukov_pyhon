#Даны координаты поля шахматной доски х, у (целые числа, лежащие в диапазоне 1-8).
#Учитывая, что левое нижнее поле доски (1,1) является черным, проверить истинность высказывания: «Данное поле является белым».
try:
    print("Точка (x, y) на данном поле является белым?")
    print("Введите кординаты для точки")
    x = int(input ("введите число х от 1 до 8:")) # Нужно ввести целое число от 1 до 8
    y = int(input ("введите число у от 1 до 8:")) # Нужно ввести целое число от 1 до 8
    if x % 2 and y // 2:
        print("Да, является")
    else:
        print("Нет, не является")
except ValueError: # Ошибка при написания букв, а не целых чисел
    print("Невозможно преобразовать строку в число.")
print("Программа успешно завершена")  # Конец программы