#Из предложенного текстового файла (text18-25.txt) вывести на экран его содержимое,
#количество символов, принадлежащих к группе букв. Сформировать новый файл, в
#который поместить текст в стихотворной форме предварительно удалив букву «с» из текста.


def kakoeto_nazvanie():

    with open('text18-25.txt', 'r', encoding='UTF-16') as file:
        lines = file.readlines()

    print("Содержимое файла:")
    for line in lines:
        print(line, end='')

    sum_bykv = 0
    for line in lines:
        for char in line:
            if char.isalpha():
                sum_bykv += 1

    print("")
    print(f"Количество букв в тексте: {sum_bykv}\n")

    new_file_dla_text = []
    for line in lines:
        cleaned_line = line.replace('с', '').replace('С', '')
        new_file_dla_text.append(cleaned_line)

    with open('new_file_dla_text.txt', 'w', encoding='utf-8') as gotovie_fail:
        gotovie_fail.writelines(new_file_dla_text)
        print("Всё успешно сохранено в файле new_file_dla_text.txt")

kakoeto_nazvanie()