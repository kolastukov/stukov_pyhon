#Дан целочисленный список размера N. Проверить, чередуются ли в нем четные и
#нечетные числа. Если чередуются, то вывести 0, если нет, то вывести порядковый
#номер первого элемента, нарушающего закономерность.

try:
    from random import randint #Подключаю рандомайзер

    n = int(input("Введите какого размера будет список: ")) #Вводим размер списка
    a = [0] * n #Делаем так что бы список запомнил какого он размера
    z = 1
    for i in range (0, n):
        a[i] = randint(1,10) #Вводятся рандомные числа в список, с начала и до его конца
    print(a)
    i = 0 #Даём новое значение
    z = 0 #Даём новое значение
    while i < n-1:
        if (a[i] % 2 == 0) == (a[i+1] % 2 == 0):
            z = i + 1
            break
        else:
            i += 1
    print("ВНИМАНИЕ: Нумерация списка начинается с 0.")
    if z == 0:
        print(z)
    else:
        print("Номер первого числа что сбило список", z)
except ValueError:# Ошибка при написании букв, а не целых чисел
    print("Невозможно преобразовать строку или не чётное число в чётное число.")
print("Программа успешно завершена")# Конец программы!