import os


def delete_file(path):
    if not os.path.exists(path):
        print(f"File '{path}' does not exist")
        return False

    if not os.access(path, os.W_OK):
        print(f"You do not have permission to delete file '{path}'")
        return False

    os.remove(path)
    print(f"File '{path}' has been deleted")
    return True


path = "my_file.txt"
delete_file(path)