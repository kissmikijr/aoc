from collections import defaultdict
def main():
    rows = []
    with open('input.txt') as matrix:
        rows = [y for y in matrix.read().split("\n")]
    print(rows)

    input = 99999999999999
    input_index = 0
    variables = {}
    while True:
        if "z" in variables:
            if variables['z'] == 0:
                print(input)
                break

        variables = {}
        for row in rows:
            if row.startswith("inp"):
                _, var = row.split(" ")
                print(str(input), input_index)
                variables[var] = str(input)[input_index]
                input_index += 1
                continue
            instr, v1, v2 = row.split(" ")
            match instr:
                case 'add':
                    if v2 in variables:
                        variables[v1] += variables[v2]
                    else:
                        variables[v1] += int(v2)
                case 'mul':
                    if v2 in variables:
                        variables[v1] *= variables[v2]
                    else:
                        variables[v1] *= int(v2)
                case 'div':
                    if v2 in variables:
                        variables[v1] //= variables[v2]
                    else:
                        variables[v1] //= int(v2)
                case 'mod':
                    if v2 in variables:
                        variables[v1] %= variables[v2]
                    else:
                        variables[v1] %= int(v2)
                case 'eql':
                    if v2 in variables:
                        variables[v1] = 1 if variables[v2] == variables[v1] else 0
                    else:
                        variables[v1] = 1 if int(v2) == variables[v1] else 0
    input -= 1
    input_index = 0

    print(variables)



main()