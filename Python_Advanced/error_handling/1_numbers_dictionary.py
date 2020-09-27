def adding():
    line = input()
    while line != "Search":
        number_as_string = line
        try:
            number = int(input())
            numbers_dictionary[number_as_string] = number
        except:
            print("The variable number must be an integer")
        line = input()


def searching():
    line = input()
    while line != "Remove":
        searched = line
        try:
            print(numbers_dictionary[searched])
        except:
            print("Number does not exist in dictionary")
        line = input()


def removing():
    line = input()
    while line != "End":
        searched = line
        try:
            del numbers_dictionary[searched]
        except:
            print("Number does not exist in dictionary")
        line = input()


numbers_dictionary = {}
adding()
searching()
removing()
print(numbers_dictionary)
