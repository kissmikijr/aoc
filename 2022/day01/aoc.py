def main():
    input_text = open('input.txt', 'r')
    max_calories = []
    rolling_sum = 0
    for l in input_text.read().split('\n'):
        if l == '':
            max_calories.append(rolling_sum)
            rolling_sum = 0
        else:
            rolling_sum += int(l)
    print(sum(sorted(max_calories, reverse=True)[:3]))
main()