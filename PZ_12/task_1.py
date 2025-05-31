#Дана последовательность целых чисел. Поменять местами ее первую и последнюю трети.
#Составить генератор (yield), который выводит из строки только цифры.

def swap_elements(list_to_swap, index1, index2):

    if index1 < 0 or index1 >= len(list_to_swap) or index2 < 0 or index2 >= len(list_to_swap):
        return list_to_swap

    new_list = list_to_swap[:]
    new_list[index1], new_list[index2] = new_list[index2], new_list[index1]
    return new_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
swapped_list = swap_elements(my_list, 0, 8)
print(my_list)
print(swapped_list)
