import os

path = "/path/to/directory"

print("Directories:")
for entry in os.listdir(path):
    if os.path.isdir(os.path.join(path, entry)):
        print(entry)

print("\nFiles:")
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        print(entry)

print("\nAll directories and files:")
for entry in os.listdir(path):
    print(entry)
