from logging import exception

import psycopg2
from psycopg2 import connect

def add_student(name,surname,course,age):
    insert_query: str = '''
                        INSERT INTO students (name, surname, course, age)
                        VALUES (%s, %s, %s, %s);
                    '''

    cursor.execute(insert_query, (name, surname, course, age))  # Выполнение запроса с параметрами
    connection.commit()  # Подтверждение изменений
    print("Данные успешно вставлены в таблицу 'students'")

def update_data(student_id):
    try:
        course = int(input('Введите курс студента: '))
        age = int(input('Введите возраст студента: '))
        update_query = '''
            UPDATE students
            SET course = %s,
            age = %s
            WHERE id = %s;
        '''
        new_data = (course, age, student_id )
        cursor.execute(update_query, new_data)
        connection.commit()
        print('Данные успешно обновлены')
    except ValueError:
        print('Ошибка ввода данных, введите число')

def show_student_data(student_id):
    try:
        select_query = "SELECT * FROM students WHERE id = %s;"
        cursor.execute(select_query, (student_id,))  # Выполнение запроса
        records = cursor.fetchall()  # Извлечение всех записей
        if records:
            print("Данные из таблицы 'students':")
            for row in records:
                print(row)
        else:
            print('Студента с таким id не найдено')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

def delete_data(student_id):
    delete_query = '''
        DELETE FROM students
        WHERE id = %s;
    '''
    cursor.execute(delete_query, (student_id,))
    connection.commit()
    print('Данные студента успешно удалены')

def show_all_students():
    # SQL-запрос для выборки данных
    select_query = 'SELECT * FROM students;'
    cursor.execute(select_query)  # Выполнение запроса
    records = cursor.fetchall()  # Извлечение всех записей
    print("Данные из таблицы 'students':")
    for row in records:
        print(row)

connection = None
try:
    connection = psycopg2.connect(
        user = 'postgres',
        password='0000',
        host='127.0.0.1',
        port='5432',
        database='postgres'
    )
    print('Соединение открыто')

    cursor = connection.cursor()
    # create_table_query = '''
    # CREATE TABLE students (
    #     id SERIAL PRIMARY KEY,
    #     name VARCHAR(30),
    #     surname VARCHAR(30),
    #     course INTEGER,
    #     age INTEGER
    # );
    # '''
    # cursor.execute(create_table_query)
    # connection.commit()
    # print("Таблица 'students' успешно создана")

    def main():
        while True:
            print('1. Добавить студента')
            print('2. Редактировать данные студента')
            print('3. Вывести данные студента')
            print('4. Удалить студента')
            print('5. Вывести всех студентов')
            print('6. Выход')
            choice = input('Выберите действие: ')

            if choice == '1':
                name = input('Введите имя студента: ')
                surname = input('Введите фамилию студента: ')
                try:
                    course = int(input('Введите курс студента: '))
                    age = int(input('Введите возраст студента: '))
                    add_student(name,surname,course,age)
                except ValueError:
                    print('Ошибка ввода данных, введите число')



            elif choice == '2':
                try:
                    student_id = int(input('Введите id студента:'))
                    update_data(student_id)
                except ValueError:
                    print('Ошибка ввода данных')
            elif choice == '3':
                try:
                    student_id = int(input('Введите id студента:'))
                    show_student_data(student_id)
                except ValueError:
                    print('Ошибка ввода данных')
            elif choice == '4':
                try:
                    student_id = int(input('Введите id студента:'))
                    delete_data(student_id)
                except ValueError:
                    print('Ошибка ввода данных')

            elif choice == '5':
                show_all_students()
            elif choice == '6':
                break
            else:
                print('Неправильный формат введенных данных')






    if __name__ == '__main__':
        main()

except Exception as e:
    print(f'Ошибка подключения к базе данных: {e}')
finally:
    if connection:
        connection.close()
        print('Соединение закрыто')


















