from view import show_message, show_collection
from utils import check_confirm

def add_note(collection: list):
    note = input("Введите текст новой заметки: ").strip()
    if note:
        collection.append(note)
        show_message("Заметка успешно ДОБАВЛЕНА.")
    else:
        show_message("Ошибка: Заметка не может быть пустой.")

def delete_note(collection: list):
    show_collection(collection)
    if not collection: return
    
    try:
        index = int(input("Введите номер заметки для УДАЛЕНИЯ: ")) - 1
        if 0 <= index < len(collection):
            if check_confirm(f"Вы уверены, что хотите удалить '{collection[index]}'?"):
                deleted = collection.pop(index)
                show_message(f"Заметка '{deleted}' УДАЛЕНА.")
            else:
                show_message("Удаление отменено.")
        else:
            show_message("Ошибка: Заметки с таким номером не существует.")
    except ValueError:
        show_message("Ошибка: Введите число.")

def edit_note(collection: list):
    show_collection(collection)
    if not collection: return
    
    try:
        index = int(input("Введите номер заметки для РЕДАКТИРОВАНИЯ: ")) - 1
        if 0 <= index < len(collection):
            new_text = input("Введите новый текст: ").strip()
            if new_text:
                collection[index] = new_text
                show_message("Заметка ИЗМЕНЕНА.")
            else:
                show_message("Ошибка: Текст не может быть пустым.")
        else:
            show_message("Ошибка: Заметки с таким номером не существует.")
    except ValueError:
        show_message("Ошибка: Введите число.")
