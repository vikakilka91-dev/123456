import os

def clear_screen():
    """Очищает консоль."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_message(message: str):
    """Показывает системное сообщение."""
    print(f"\n[СИСТЕМА]: {message}")
    input("Нажмите Enter, чтобы продолжить...")

def show_collection(collection: list):
    """Форматированно выводит список заметок."""
    clear_screen()
    print("=" * 40)
    print("        СПИСОК ВАШИХ ЗАМЕТОК")
    print("=" * 40)
    
    if not collection:
        print("  У вас пока нет заметок.")
    else:
        for index, note in enumerate(collection, start=1):
            print(f" {index}. {note}")
            
    print("=" * 40)

def show_menu():
    """Выводит главное меню."""
    print("\nМЕНЮ:")
    print("1. Добавить заметку")
    print("2. Удалить заметку")
    print("3. Редактировать заметку")
    print("4. Выход")
