import re

def ints(input: str):
    return [int(x) for x in re.findall(r'-?\d+', input)]

def parse_to_grid(input,delimeter="\n"):
    return [[x for x in y] for y in input.split(delimeter)]
    
symbols = ['-', '*', '%', '=', '&', '+', '$', '@', '#', '/']

def touched_by_symbol(grid, x, y):
    if grid[y][x] == '.':
        return False
    # left
    if x-1 >= 0:
        if grid[y][x - 1] in symbols:
            return True 
    # right
    if x + 1 <= len(grid[0]) - 1:
        if grid[y][x + 1] in symbols:
            return True
    # top
    if y - 1 >= 0:
        if grid[y-1][x] in symbols:
            return True
    # bottom
    if y + 1 <= len(grid) - 1:
        if grid[y+1][x] in symbols:
            return True
    # topright
    if x + 1 <= len(grid[0]) - 1 and y - 1 >= 0:
        if grid[y-1][x+1] in symbols:
            return True
    # topleft
    if x - 1 >= 0 and y - 1 >= 0:
        if grid[y-1][x-1] in symbols:
            return True
    # bottomleft
    if x - 1 >= 0 and y + 1 <= len(grid) -1:
        if grid[y+1][x-1] in symbols:
            return True
    # bottomright
    if x + 1 <= len(grid[0]) - 1 and y + 1 <= len(grid) -1:
        if grid[y+1][x+1] in symbols:
            return True

    

def main():
    input_text = open('input.txt', 'r')
    score = 0

    grid = parse_to_grid(input_text.read())
    touched = []
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if touched_by_symbol(grid, x, y):
                if len(touched) == 0:
                    touched.append((y, x))
                elif touched_by_symbol(grid, x-1, y):
                    continue
                else:
                    touched.append((y, x))

    for y, x in touched:
        if grid[y][max(x-1, 0)].isdigit() and grid[y][min(x+1, len(grid[y])-1)].isdigit():
            current_score = ints(''.join(grid[y][x-1:x+1+1]))
        elif grid[y][max(x-1, 0)].isdigit():
            if grid[y][max(x-2, 0)].isdigit():
                current_score = ints(''.join(grid[y][max(x-2, 0):x+1]))
            else:
                current_score = ints(''.join(grid[y][max(x-1, 0):x+1]))

        elif grid[y][min(x+1, len(grid[y])-1)].isdigit():
            if grid[y][min(x+2, len(grid[y])-1)].isdigit():
                current_score = ints(''.join(grid[y][x:min(x+2, len(grid[y])-1)+1]))
            else:
                current_score = ints(''.join(grid[y][x:min(x+1, len(grid[y])-1)+1]))

        else:
            current_score = ints(grid[y][x])

        score += current_score[0]

    print('result:',score)


def adjacent_to_star(grid, x, y):
    if grid[y][x] != '*':
        return []
    
    adjacent_number_coords = []
    # left
    if x-1 >= 0:
        if grid[y][x - 1].isdigit():
            adjacent_number_coords.append((y, x-1))
    # right
    if x + 1 <= len(grid[0]) - 1:
        if grid[y][x + 1].isdigit():
            adjacent_number_coords.append((y, x + 1))
    # top
    if y - 1 >= 0:
        if grid[y-1][x].isdigit():
            adjacent_number_coords.append((y-1, x))
    # bottom
    if y + 1 <= len(grid) - 1:
        if grid[y+1][x].isdigit():
            adjacent_number_coords.append((y+1, x))
    # topright
    if x + 1 <= len(grid[0]) - 1 and y - 1 >= 0:
        if grid[y-1][x+1].isdigit():
            adjacent_number_coords.append((y-1, x+1))
    # topleft
    if x - 1 >= 0 and y - 1 >= 0:
        if grid[y-1][x-1].isdigit():
            adjacent_number_coords.append((y-1, x-1))
    # bottomleft
    if x - 1 >= 0 and y + 1 <= len(grid) -1:
        if grid[y+1][x-1].isdigit():
            adjacent_number_coords.append((y+1, x-1))
    # bottomright
    if x + 1 <= len(grid[0]) - 1 and y + 1 <= len(grid) -1:
        if grid[y+1][x+1].isdigit():
            adjacent_number_coords.append((y+1, x+1))
    return adjacent_number_coords

def main2():
    input_text = open('input.txt', 'r')
    score = 0
    potential_gears = []
    grid = parse_to_grid(input_text.read()) 
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            potential_gears.append(adjacent_to_star(grid, x,y))

    for potential_gear_coords in potential_gears:
        if len(potential_gear_coords) > 6:
            continue

        already_used_to_create_number = set()
        adjacent_numbers = []
        for coords in potential_gear_coords:
            y, x = coords
            if (y, x) in already_used_to_create_number:
                continue

            already_used_to_create_number.add((y, x))
            if grid[y][max(x-1, 0)].isdigit() and grid[y][min(x+1, len(grid[y])-1)].isdigit():
                current_score = ints(''.join(grid[y][x-1:x+1+1]))

                already_used_to_create_number.add((y, x-1))
                already_used_to_create_number.add((y, x+1))

            elif grid[y][max(x-1, 0)].isdigit():
                if grid[y][max(x-2, 0)].isdigit():
                    current_score = ints(''.join(grid[y][max(x-2, 0):x+1]))

                    already_used_to_create_number.add((y, x-1))
                    already_used_to_create_number.add((y, x-2))
                else:
                    current_score = ints(''.join(grid[y][max(x-1, 0):x+1]))
                    already_used_to_create_number.add((y, x-1))

            elif grid[y][min(x+1, len(grid[y])-1)].isdigit():
                if grid[y][min(x+2, len(grid[y])-1)].isdigit():
                    current_score = ints(''.join(grid[y][x:min(x+2, len(grid[y])-1)+1]))

                    already_used_to_create_number.add((y,min(x+1, len(grid[y])-1)))
                    already_used_to_create_number.add((y, min(x+2, len(grid[y])-1)))
                else:
                    current_score = ints(''.join(grid[y][x:min(x+1, len(grid[y])-1)+1]))

                    already_used_to_create_number.add((y,min(x+1, len(grid[y])-1)))

            else:
                current_score = ints(grid[y][x])

            adjacent_numbers.append(current_score[0])
        if len(adjacent_numbers) == 2:
            score += adjacent_numbers[0]*adjacent_numbers[1]

    print('part2:', score)

main2()
main()