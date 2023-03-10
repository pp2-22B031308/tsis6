file_to_read = "text.txt"
write_to_file = "reason.txt"

file = open(file_to_read, "r")
data = file.read()
file.close()

with open(write_to_file, "a") as file:
    file.write(data)

print('done    ')