def main():
    input_text = open('input.txt', 'r')
    moves = input_text.read().split(
        '\n'
    )
    stacks = {
        '1': ['F', 'C', 'P', 'G','Q', 'R'],
        '2': ['W', 'T', 'C', 'P'],
        '3': ['B', 'H', 'P', 'M', 'C'],
        '4': ['L', 'T', 'Q', 'S', 'M', 'P', 'R'],
        '5': ['P', 'H', 'J', 'Z', 'V', 'G', 'N'],
        '6' :['D', 'P', 'J'],
        '7' :['L', 'G', 'P', 'Z', 'F', 'J', 'T', 'R'],
        '8' :['N', 'L', 'H', 'C', 'F', 'P', 'T', 'J'],
        '9' :['G', 'V', 'Z', 'Q', 'H', 'T', 'C', 'W'],
    }
    for move in moves:
        # 2,2,8
        amount_to_move, from_where, to = move.split(',')
        atm = int(amount_to_move)
        stacks[from_where], stacks[to] = stacks[from_where][:atm * -1], stacks[to] + stacks[from_where][len(stacks[from_where]) - atm:]

    r = ''
    for i in range(1,10):
        r += stacks[str(i)][-1]
    print(r)

main()