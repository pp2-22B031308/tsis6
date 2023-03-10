import os


def check_access(path):
    if os.path.exists(path):
        if os.access(path, os.R_OK):
            print("Read access granted.")
        else:
            print("Read access denied.")

        if os.access(path, os.W_OK):
            print("Write access granted.")
        else:
            print("Write access denied.")

        if os.access(path, os.X_OK):
            print("Execute access granted.")
        else:
            print("Execute access denied.")
    else:
        print("The specified path does not exist.")


my_path = "/path/to/directory"
check_access(my_path)