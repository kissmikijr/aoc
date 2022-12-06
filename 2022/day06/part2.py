def main():
    input_text = open('input.txt', 'r')
    stream = input_text.read()
    result = 0
    for i, _ in enumerate(stream[14:]):
        potential_marker = stream[i:i+14]
        if len(set(potential_marker)) == 14:
            result = i+14
            break
    print(result)

main()