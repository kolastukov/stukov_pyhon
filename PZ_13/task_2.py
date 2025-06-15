#В двумерном списке элементы второго столбца возвести в квадрат.

matricha = [
    [1, 2, 3, -4],
    [8, 7, -6, 5],
    [22,-13, 7, 1],
    [12, 14, -5, 21]
]

matricha_v_kvadrate = [
    [rad_matrichi[i] ** 2 if i == 1 else rad_matrichi[i] for i in range(len(rad_matrichi))]
    for rad_matrichi in matricha
]

print("\nМатрица после возведения второго столбца в квадрат:")
for rad_matrichi in matricha_v_kvadrate:
    print(rad_matrichi)