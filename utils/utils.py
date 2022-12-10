import re

def ints(input: str):
    return re.findall(r'\d+', input)

def parse_to_grid(input,delimeter="\n"):
    return [[x for x in y] for y in input.split(delimeter)]

def empty_grid_x_by_y(filler, x, y):
    r = []
    for _ in range(x):
        t = []
        for _ in range(y):
            t.append(filler)
        r.append(t)
    return r