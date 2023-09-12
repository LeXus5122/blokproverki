import csv
import datetime
import os

def add_note():
    file_exists = os.path.isfile('notes.csv')
    id = 1
    if file_exists:
        with open('notes.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            id = sum(1 for row in reader)
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('notes.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        if not file_exists:
            writer.writerow(["ID", "Date", "Title", "Body"])
        writer.writerow([id, date, title, body])
    print("Заметка успешно сохранена")

def view_notes():
    with open('notes.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row)

def edit_note():
    id = input("Введите ID заметки для редактирования: ")
    title = input("Введите новый заголовок заметки: ")
    body = input("Введите новое тело заметки: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes = []
    with open('notes.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[0] == id:
                notes.append([id, date, title, body])
            else:
                notes.append(row)
    with open('notes.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(notes)
    print("Заметка успешно отредактирована")

def delete_note():
    id = input("Введите ID заметки для удаления: ")
    notes = []
    with open('notes.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[0] != id:
                notes.append(row)
    with open('notes.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(notes)
    print("Заметка успешно удалена")

def main():
    while True:
        command = input("Введите команду (add/view/edit/delete/exit): ")
        if command == 'add':
            add_note()
        elif command == 'view':
            view_notes()
        elif command == 'edit':
            edit_note()
        elif command == 'delete':
            delete_note()
        elif command == 'exit':
            break
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()
