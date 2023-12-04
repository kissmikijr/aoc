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
        current_score = max(ints(''.join(grid[y][max(x-2, 0):min(len(grid[y])-1, x+3)])))
        print('Adding:', current_score)
        score += current_score


    print('result:',score)


main()