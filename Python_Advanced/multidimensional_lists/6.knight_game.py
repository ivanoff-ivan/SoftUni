def is_valid(coordinates):
    r = coordinates[0]
    c = coordinates[1]
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        if matrix[r][c] == "K":
            return True
        else:
            return False
    else:
        return False


N = int(input())
matrix = []
for _ in range(N):
    row = [x for x in input()]
    matrix.append(row)

counter = 0
while True:
    most_damaging_knight = 0
    most_damaging_knight_coordinates = [0, 0]
    for row in range(N):
        for col in range(N):
            current_damage = 0
            if matrix[row][col] == "K": 
                two_downside_one_backwards = [row + 2, col - 1]
                two_downside_one_forwards =  [row + 2, col + 1]
                one_downside_two_backwards = [row + 1, col - 2]
                one_downside_two_forwards =  [row + 1, col + 2]
                two_upside_one_backwards = [row - 2, col - 1]
                two_upside_one_forwards =  [row - 2, col + 1]
                one_upside_two_backwards = [row - 1, col - 2]
                one_upside_two_forwards =  [row - 1, col + 2]
                if is_valid(two_downside_one_backwards):
                    current_damage += 1
                if is_valid(two_downside_one_forwards):
                    current_damage += 1
                if is_valid(one_downside_two_backwards):
                    current_damage += 1
                if is_valid(one_downside_two_forwards):
                    current_damage += 1
                if is_valid(two_upside_one_backwards):
                    current_damage += 1
                if is_valid(two_upside_one_forwards):
                    current_damage += 1
                if is_valid(one_upside_two_backwards):
                    current_damage += 1
                if is_valid(one_upside_two_forwards):
                    current_damage += 1
                
                if current_damage > most_damaging_knight:
                    most_damaging_knight = current_damage
                    most_damaging_knight_coordinates[0] = row
                    most_damaging_knight_coordinates[1] = col

    if most_damaging_knight > 0:
        the_row = most_damaging_knight_coordinates[0]
        the_col = most_damaging_knight_coordinates[1]
        matrix[the_row][the_col] = "0"
        counter += 1
    else:
        break

print(counter)

            
            


    
