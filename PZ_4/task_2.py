#Дано целое число N (>0). Если оно является степенью числа 3, то вывести TRUE,
#если не является — вывести FALSE.
try:
  def kola(a):#Функция
      if a == 1:#Если число = 1, то это число в 0 степени
          return 'TRUE'
      if a < 1 or a % 3 != 0:
          return 'FALSE'
      return kola(a // 3)

  a = int(input('Введите целое число, что больше 0: '))#Ввод числа
  print(kola(a))
except ValueError:# Ошибка при написании букв, а не целых чисел
    print("Невозможно преобразовать строку в число.")
print("Программа завершена")# Конец программы!


