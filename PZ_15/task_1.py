#Приложение  ПЛАТНАЯ ПОЛИКЛИНИКА для некоторой организации.
#БД должна содержать таблицу  Пациент со следующей структурой записи:
#ФИО  пациента, ФИО врача, диагноз, стоимость лечение.

import sqlite3 as sq

def bolnicha():
    with sq.connect('polyclinic.db') as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Пациент (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       ФИО_пациента TEXT NOT NULL,
                       ФИО_врача TEXT NOT NULL,
                       диагноз TEXT,
                       стоимость_лечения REAL NOT NULL
                       )""")

def new_patient(patient_name: str, doctor_name: str, diagnosis: str, cost: float):
    with sq.connect('polyclinic.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO Пациент (ФИО_пациента, ФИО_врача, диагноз, стоимость_лечения) VALUES (?, ?, ?, ?)",
                    (patient_name, doctor_name, diagnosis, cost))

def get_all_patients():
    with sq.connect('polyclinic.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Пациент")
        return cur.fetchall()

def main():
    bolnicha()
    new_patient("Стуков Николай Николаевич", "Мазманов А.В.", "Шиза", 5000.0)
    new_patient("Стуков Никина Николаевич", "Иванов И.И.", "Рак мозга", 450000.0)
    new_patient("Вадим Спартаков Викторович", "Петров П.П.", "Перелом руки и ноги", 15000.0)

    print("Список всех пациентов:")
    for patient in get_all_patients():
        print(patient)

if __name__ == "__main__":
    main()