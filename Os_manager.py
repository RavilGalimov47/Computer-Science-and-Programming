import os
import shutil

class FileManager:
    def __init__(self):
        self.current_directory = os.getcwd()

    def list_directory(self):
        files = os.listdir(self.current_directory)
        for file in files:
            print(file)

    def create_directory(self, directory_name):
        new_directory_path = os.path.join(self.current_directory, directory_name)
        os.mkdir(new_directory_path)
        print(f"Directory '{directory_name}' created")

    def delete_item(self, item_name):
        item_path = os.path.join(self.current_directory, item_name)
        if os.path.exists(item_path):
            if os.path.isfile(item_path):
                os.remove(item_path)
                print(f"File '{item_name}' deleted")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Directory '{item_name}' deleted")

    def copy_item(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        if os.path.exists(source_path):
            if os.path.isfile(source_path):
                shutil.copyfile(source_path, destination_path)
                print(f"File '{source}' copied to '{destination}'")
            elif os.path.isdir(source_path):
                shutil.copytree(source_path, destination_path)
                print(f"Directory '{source}' copied to '{destination}'")

    def move_item(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
            print(f"Item '{source}' moved to '{destination}'")

    def search_file(self, file_name):
        for root, dirs, files in os.walk(self.current_directory):
            if file_name in files:
                print(f"File '{file_name}' found at: {os.path.join(root, file_name)}")

    def change_permissions(self, item_name, mode):
        item_path = os.path.join(self.current_directory, item_name)
        if os.path.exists(item_path):
            os.chmod(item_path, mode)
            print(f"Permissions for '{item_name}' changed to {oct(mode)}")

file_manager = FileManager()

file_manager.list_directory()
file_manager.create_directory("new_directory")
file_manager.delete_item("file.txt")
file_manager.copy_item("source.txt", "destination.txt")
file_manager.move_item("source.txt", "new_directory/source.txt")
file_manager.search_file("file.txt")
file_manager.change_permissions("file.txt", 0o777)