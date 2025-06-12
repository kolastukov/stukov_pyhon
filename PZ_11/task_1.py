#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:

#Элементы первого и второго файлов:
#Элементы после сортировки:
#Количество элементов:
#Минимальный элемент кратный 2:
#Максимальный элемент кратный 5:


def rabota_s_failami():

    with open('file1.txt', 'w') as f1:
        f1.write("-20 -15 -10 -5 0 5 10 15 20")

    with open('file2.txt', 'w') as f2:
        f2.write("-8 -6 -4 -2 0 2 4 6 8")

    with open('file1.txt') as f1, open('file2.txt') as f2:
        nums1 = list(map(int, f1.read().split()))
        nums2 = list(map(int, f2.read().split()))

    soidenenie = nums1 + nums2

    sortiruem = sorted(soidenenie)

    dva = min(x for x in soidenenie if x % 2 == 0)

    pat = max(x for x in soidenenie if x % 5 == 0)

    with open('vtoroi_fail.txt', 'w') as f:
        f.write("Элементы находящийся в первом и втором файле:\n")
        f.write(f"Элементы первого файла: {' '.join(map(str, nums1))}\n")
        f.write(f"Элементы второго файла: {' '.join(map(str, nums2))}\n\n")

        f.write("Все элементы после сортировки:\n")
        f.write(f"{' '.join(map(str, sortiruem))}\n\n")

        f.write(f"Количество элементов: {len(soidenenie)}\n")
        f.write(f"Минимальный элемент кратный 2: {dva}\n")
        f.write(f"Максимальный элемент кратный 5: {pat}\n")


rabota_s_failami()








