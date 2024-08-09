from sqlite3 import *


connection = connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER,
major TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Courses (
course_id INTEGER PRIMARY KEY,
course_name  TEXT NOT NULL,
instructor  TEXT NOT NULL
)
''')

sql = '''
SELECT Users.major, Courses.course_name
FROM Users
LEFT JOIN Courses ON Users.major = Courses.course_name     
'''   
cursor.execute(sql)   

connection.commit()

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        name = input("Введіть їм'я студента.")
        age = int(input("Введіть кількість років."))
        major = input("На який курс ходить студент?")
        cursor.execute('INSERT INTO Users (name, age, major) VALUES (?, ?, ?)', (name, age, major))
        connection.commit()
        
        # Додавання нового студента

    elif choice == "2":
        name = input("Введіть назву курса.")
        major = input("Хто його викладає?")
        cursor.execute('INSERT INTO Users (course_name, instructor) VALUES (?, ?)', (name, major))
        connection.commit()
    # Додавання нового курсу

    elif choice == "3":
        cursor.execute("SELECT * FROM Users")
        users = cursor.fetchall()
        for user in users:
            print(user)
                
        # Показати список студентів
     
    elif choice == "4":
        cursor.execute("SELECT * FROM Courses")
        courses = cursor.fetchall()
        for course in courses:
            print(course)
        # Показати список курсів

    elif choice == "5":
        pass
        # Зареєструвати студента на курс

    elif choice == "6":
        pass
        # Показати студентів на конкретному курсі
       
    elif choice == "7":
        break

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")


connection.close()