input = ''
rules = {
    'A': 'C', 'B': 'A', 'C': 'B'
}
scores = {
    'A': 1,
    'B': 2,
    'C': 3
}
def get_score(left, right):
    if right == 'X':
        #lose
        return scores[rules[left]] + 0
    elif right == 'Y':
        #draw
        return scores[left] + 3

    elif right == 'Z':
        #win
        return scores[rules[rules[left]]] + 6

def main():
    input_text = open('input2.txt', 'r')
    score = 0
    for line in input_text.read().split('\n'):
        left = line[0]
        right = line[2]
        score += get_score(left, right)

    print(score)
main()