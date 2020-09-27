def func_executor(*args):
    result = []
    for element in args:
        func = element[0]
        data = element[1]
        result.append(func(*data)) #ънпаква данните от тюпъла за всяка функция и ги добавя в списък
    return result

