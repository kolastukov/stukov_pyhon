#В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
#Посчитать количество полученных элементов.

import re

def moi_file(filename):

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            pattern = r'(?:(роман|повесть|рассказ|поэма|пьеса|комедия|трагедия)\s*[«"](.+?)[»"]|«(.+?)»)'
            matches = re.findall(pattern, text)

            works = []
            for match in matches:
                work = next(item for item in match if item)
                works.append(work)

            unique_works = list(set(works))

            return unique_works, len(unique_works)

    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        return [], 0
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return [], 0


if __name__ == "__main__":
    input_file = "Dostoevsky.txt"
    output_file = "Dostoevsky_works.txt"

    works, count = moi_file(input_file)

    print(f"Произведений: {count}")
    print("Список произведений Достоевского:")
    for i, work in enumerate(works, 1):
        print(f"{i}. {work}")

    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"Всего найдено произведений: {count}\n\n")
            file.write("Список произведений:\n")
            for i, work in enumerate(works, 1):
                file.write(f"{i}. {work}\n")
        print(f"\nВсе произведения былы отправленны в файл: {output_file}")
    except Exception as e:
        print(f"Ошибка: {e}")