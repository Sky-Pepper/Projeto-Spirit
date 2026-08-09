import os
import shutil
from datetime import datetime
from tkinter import Tk, filedialog

def create_deafault_extensions_map():
    return {
        "Imagens": [".jpg", ".png", ".jpeg", ".gif"],
        "Documentos": [".pdf", "-doc", ".docx", ".txt", ".ppt", "pptx", ".xls", ".xlsx"],
        "Músicas": [".mp3", ".wav"],
        "Arquivos":[".zip", ".rar", ".7z", ".html"],
        "Código": [".py", ".html", ".js", ".css"],
        "Outros": [],
    }

def get_folder_for_extensions(extension, extension_map):
    for folder, extensions in extension_map.items():
        if extension in extensions:
            return folder
        else:
            return "Outros"

def move_file(file_path, folder_name, directory):
    folder_path = os.path.join(directory, folder_name)

    os.makedirs(folder_path, exists_ok = True)

    new_path = shutil.move(file_path, folder_path)

    print(f"Movido {os.path.basename(file_path)} para {folder_path}")
    return new_path

def organize_by_extension(directory):
    extensions_map = create_deafault_extensions_map()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            extension = os.path.splitext(file_path)[1].lower()
            folder_name = get_folder_for_extensions(extension, extensions_map)
            move_file(file_path, folder_name, directory)

def organize_by_date(directory):
    for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                created_at = datetime.fromtimestamp(os.path.getctime(file_path))
                folder_name = created_at.strftime("%Y-%M-%D")
                move_file(file_path, folder_name, directory)

def main():
    root = Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title = "Selecionar diretório")
    if not directory:
        print("O diretório selecionado não existe")
        return
    
    while True:
        print("\nFile.org - Escolha uma opção:")
        print("1- Organizar por tipo de arquivo")
        print("2- Organizar por data")
        print("3- Sair")

        choice = input("Digite sua escolha (1-3): ")

        if choice == "1":
            organize_by_extension(directory)
        elif choice == "2":
            organize_by_date(directory)
        elif choice == "3":
            break
        else:
            print("Opção inválida, por favor tente novamente.")

if __name__ == "__main__":
    main()



