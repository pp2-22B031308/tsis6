import os


def test_path(path):
    if os.path.exists(path):
        dirname, filename = os.path.split(path)
        print("Path exists.")
        print("Directory:", dirname)
        print("Filename:", filename)
    else:
        print("Path does not exist.")


my_path = "/path/to/myfile.txt"
test_path(my_path)