with open('my_file.txt', 'r') as file:
    line_count = 0

    for line in file:
        line_count += 1

print("Number of lines in file:", line_count)