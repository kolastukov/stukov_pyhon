#В двумерном списке элементы второго столбца возвести в квадрат.

MyList = [[10, 20], [30, 40]]
print("Матрица ", MyList)

column = 2
for i in MyList:
    print(i[column-1])
    i = i[column-1] ** 2
    print("Степень", i)