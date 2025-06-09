#В двумерном списке найти сумму элементов второй половины матрицы.

def sum_elements(MyList, n):
    suma = 0
    polovina = n // 2
    polovina_2 = MyList[polovina:polovina * 2]
    print("Вторая половина матрици ", polovina_2)

    for row in polovina_2:
        suma += sum(row)
    print("Сумма чисел во второй половине матрицы ", suma)

MyList = [[10, 20], [30, 40]]
print("Матрица ", MyList)
n = len(MyList)
sum_elements(MyList, n)