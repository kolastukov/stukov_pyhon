#Даны два целых числа A и B (A < B). Вывести в порядке возрастания все целые числа,
#расположенные между A и B (включая сами числа A и B), а также количество N этих чисел.
try:
    print("Введите два числа, но чтобы они придерживались правила (A < B)")
    A = int(input("Введите число A: "))#Ввод первого числа
    B = int(input("Введите число B: "))#Ввод второго числа

    count = 0

    if A < B:
        print("Числа стоящие от первого числа (включительно) и до второго числа (включительно):")
        for tolchok in range(A, B + 1):
            print(tolchok)
            count+=1
        print(f"Колличество чисел стоящих от первого числа и до второго числа, считая сами же числа: {count}")
    else:
        print("Числа не выполняют требование (A < B)")
except ValueError:# Ошибка при написании букв, а не целых чисел
    print("Невозможно преобразовать строку в число.")
print("Программа успешно завершена")# Конец программы!


