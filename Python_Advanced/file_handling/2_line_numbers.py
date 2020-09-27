with open("text.txt", 'r') as file:
    for index,line in enumerate(file):
        letter_counter = len([x for x in line if x.isalpha()])
        char_counter = 0
        for ch in line:
            if ch in "-.,'!?\"":
                char_counter += 1
        with open("output.txt", 'a') as f:
            pattern = f"Line {index+1}: {line} ({letter_counter})({char_counter})\n"
            f.write(pattern)
        
                
        



