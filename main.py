import json
import uuid

# Константа для имени файла, где будут храниться данные о книгах
DATABASE_FILE = "library.json"

# Загружает данные из JSON-файла. Если файл отсутствует, возвращает пустой список.
def load_data() -> list[dict]:
    try:
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)  
    except FileNotFoundError:
        return []  

# Сохраняет данные в JSON-файл.
def save_data(data: list[dict]) -> None:
    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file, indent=4)  

# Добавляет новую книгу в библиотеку.
def add_book(title: str, author: str, year: int) -> None:
    books = load_data()  
    new_book = {
        "id": str(uuid.uuid4()), 
        "title": title,
        "author": author,
        "year": year,
        "status": "в наличии" 
    }
    books.append(new_book)
    save_data(books)  
    print(f"Книга '{title}' успешно добавлена!") 

# Удаляет книгу по её ID.
def delete_book(book_id: str) -> None:
    books = load_data()  
    updated_books = [book for book in books if book["id"] != book_id] 
    if len(books) == len(updated_books): 
        print("Книга с таким ID не найдена.")
    else:
        save_data(updated_books)  
        print("Книга успешно удалена.")  

# Ищет книги по названию, автору или году.
def search_books(query: str) -> list[dict]:
    books = load_data()  
    results = []  
    for book in books:
        # Проверяем, содержится ли запрос в названии, авторе или году книги
        if (query.lower() in book["title"].lower() or
            query.lower() in book["author"].lower() or
            query == str(book["year"])):
            results.append(book)  
    return results 

# Обновляет статус книги (например, 'в наличии' или 'выдана').
def update_status(book_id: str, status: str) -> None:
    if status not in ["в наличии", "выдана"]:  
        print("Ошибка: Некорректный статус!")
        return

    books = load_data() 
    for book in books:
        if book["id"] == book_id:  
            book["status"] = status  
            save_data(books) 
            print("Статус книги обновлён.")
            return
    print("Книга с таким ID не найдена.")

# Выводит список всех книг в библиотеке.
def list_books() -> None:
    books = load_data()
    if not books:  
        print("Библиотека пуста.")
    else:
        for book in books:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, "
                  f"Год: {book['year']}, Статус: {book['status']}")

# Основное меню программы.
def main() -> None:
    while True:
        # Выводим меню
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите действие: ")  

        if choice == "1":
            # Добавление книги
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                year = int(input("Введите год издания: "))  
                add_book(title, author, year) 
            except ValueError:
                print("Ошибка: Год издания должен быть числом.")
                # Удаление книги 
        elif choice == "2":
            book_id = input("Введите ID книги: ")
            delete_book(book_id)
            # Поиск книги
        elif choice == "3":
            
            query = input("Введите название, автора или год книги: ")
            results = search_books(query)
            if results:
                for book in results:
                    print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, "
                          f"Год: {book['year']}, Статус: {book['status']}")
            else:
                print("Книги не найдены.")  
            # Отображение всех книг
        elif choice == "4":
            list_books()
            # Изменение статуса книги
        elif choice == "5":
            book_id = input("Введите ID книги: ")
            status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            update_status(book_id, status)
            # Завершение программы
        elif choice == "6":
            print("Спасибо за использование программы. До свидания!")
            break
        else:
            print("Ошибка: Неверный выбор. Попробуйте снова.")  

# Запуск программы
if __name__ == "__main__":
    main()
