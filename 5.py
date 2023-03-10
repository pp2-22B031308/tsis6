my_list = ["fefwd", "bafwddwfnana", "ofwrefawndge", "grfewafewfwpe"]


with open("my_file.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")