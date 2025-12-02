import os
import sys
import shutil

if len(sys.argv) < 2:
    print("Потрібно вказати шлях до папки")
    sys.exit(1)

source_folder = sys.argv[1]
destination_folder = sys.argv[2] if len(sys.argv) > 2 else "dist"

# Головна рекурсивна функція для обходу папок
def process_folder(folder_path):
    try:
        for item in os.listdir(folder_path):
            full_path = os.path.join(folder_path, item)
            if os.path.isdir(full_path):
                process_folder(full_path)
            else:
                copy_file(full_path)
    except PermissionError:
        print(f"Немає доступу до папки: {folder_path}")

# Функція для копіювання файлу в потрібну папку
def copy_file(file_path):
    extension = os.path.splitext(file_path)[1]
    
    if extension:  
        folder_name = extension[1:]
    else:
        folder_name = "без_розширення"
    
    destination_path = os.path.join(destination_folder, folder_name)
    os.makedirs(destination_path, exist_ok=True)
    
    try:
        shutil.copy2(file_path, destination_path)
        print(f"Копійовано: {file_path}")
    except Exception as e:
        print(f"Помилка: {file_path} - {e}")

if __name__ == "__main__":
    if not os.path.exists(source_folder):
        print("Папка не існує")
        sys.exit(1)
    
    print(f"Сортуємо файли з {source_folder} в {destination_folder}")
    process_folder(source_folder)
    print("Сортування завершено")