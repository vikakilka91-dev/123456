import json
import os

FILE_NAME = "notes_data.json"

def load_data():
    """Загружает данные из файла JSON."""
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_data(notes_list):
    """Сохраняет данные в файл JSON."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(notes_list, file, ensure_ascii=False, indent=4)
      
