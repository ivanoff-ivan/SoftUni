import os

while True:
    tokens = input().split("-")
    if tokens[0] == "End":
        break
    command = tokens[0]
    file_name = tokens[1]
    if command == "Create":
        file = open(file_name, 'w')
        file.close()
    elif command == "Add":
        with open(file_name, 'a') as file:
            file.write(f"{tokens[2]}\n")
    elif command == "Replace":
        try:
            with open(file_name, 'r') as file:
                old_string = tokens[2]
                new_string = tokens[3]
                text = file.read()
            text = text.replace(old_string,new_string)
            with open(file_name, 'w') as f:
                f.write(output)
        except:
            print("An error occurred")
    elif command == "Delete":
        try:
            os.remove(file_name)
        except:
            print("An error occurred")

    
    

    