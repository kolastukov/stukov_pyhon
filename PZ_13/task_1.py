#В двумерном списке найти сумму элементов второй половины матрицы.

matricha = [
    [1, 2, 3, -4],
    [8, 7, -6, 5],
    [22,-13, 7, 1],
    [12, 14, -5, 21]
]

half = len(matricha) // 2
two_polovina = matricha[half:]

suma_elementov = sum(map(lambda rad_matrichi: sum(rad_matrichi), two_polovina))

print("Начальная матрица:")
for rad_matrichi in matricha:
    print(rad_matrichi)
print(f"Сумма элементов второй половины матрицы (нижней половины): {suma_elementov}")