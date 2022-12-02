input = ''
rules = {
    'A': 'C', 'B': 'A', 'C': 'B', 'X':'C', 'Y': 'A', 'Z': 'B'
}
scores = {
    'A': 1,
    'B': 2,
    'C': 3
}
def get_score(left, right):
    if left == right:
        # draw
        return scores[right] +3
    elif rules[right] == left:
        #win
        return scores[right] + 6
    else:
        # lose
        return scores[right] + 0
def main():
    input_text = open('input.txt', 'r')
    score = 0
    for line in input_text.read().split('\n'):
        left = line[0]
        right = line[2]
        score += get_score(left, right)

    print(score)
main()