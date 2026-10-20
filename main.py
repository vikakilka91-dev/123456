from storage import load_data, save_data
from view import show_collection, show_menu, show_message
from core import add_note, delete_note, edit_note

def main():
    # Загружаем данные при старте
    notes_collection = load_data()
    
    if not notes_collection:
        # Тестовые данные, если файла еще нет
        notes_collection = ["Купить хлеб", "Выучить Python"]

    while True:
        show_collection(notes_collection)
        show_menu()
        
        choice = input("Выберите действие (1-4): ").strip()
        
        match choice:
            case "1":
                add_note(notes_collection)
                save_data(notes_collection) # Сохраняем после изменения
            case "2":
                delete_note(notes_collection)
                save_data(notes_collection)
            case "3":
                edit_note(notes_collection)
                save_data(notes_collection)
            case "4":
                print("\nДо встречи!")
                break
            case _:
                show_message("Ошибка: Неверный пункт меню.")

if __name__ == "__main__":
    main()
