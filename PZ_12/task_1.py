#Дана последовательность целых чисел. Поменять местами ее первую и последнюю трети.
#Составить генератор (yield), который выводит из строки только цифры.

#Задание 1
spisok = list((1, 2, 3, 4, 5, 6, 7, 8, 9))
print(spisok)

def rasdelenie(spisok):
    n = len(spisok)
    treti = n // 3
    tret_1 = spisok[:treti]
    tret_2 = spisok[treti:treti * 2]
    tret_3 = spisok[treti * 2:]
    return tret_3 + tret_2 + tret_1

delen = rasdelenie(spisok)
print(delen)

#Задание 2
text = "1а, 2б, 3в, 4г, 5д, 6е, 7ё, 8ж, 9з"
def generator(text):
    for symbol in text:
        if symbol.isdigit():
            yield symbol
start_generator = generator(text)
for digit in start_generator:
    print(digit)












