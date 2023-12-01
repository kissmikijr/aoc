def main():
    input_text = open('input.txt', 'r')
    stream = input_text.read()
    result = 0
    for i, char in enumerate(stream[4:]):
        potential_marker = stream[i:i+4]
        if len(set(potential_marker)) == 4:
            print(potential_marker)
            result = i+4
            break
    print(result)

main()