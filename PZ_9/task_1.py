#Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
#отражающая продажи продукции по дням в кг. Преобразовать информацию из
#строки в словари, с использованием функции найти среднее значение продаж по
#каждому виду продукции, результаты вывести на экран.
shop = {}
dano = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
inf = dano.split()
shop['Первая продукция'] = inf[0]
shop['количество проданных кг в понедельник'] = inf[1]
shop['количество проданных кг во вторник'] = inf[2]
shop['количество проданных кг в среду'] = inf[3]
shop['количество проданных кг в четверг'] = inf[4]
shop['количество проданных кг в пятницу'] = inf[5]
shop['Вторая продукция'] = inf[6]
shop['другое количество проданных кг в понедельник'] = inf[7]
shop['другое количество проданных кг во вторник'] = inf[8]
shop['другое количество проданных кг в среду'] = inf[9]
shop['другое количество проданных кг в четверг'] = inf[10]
shop['другое количество проданных кг в пятницу'] = inf[11]
print(shop)
