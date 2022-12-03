import string

def main():
    input_text = open('input.txt', 'r')
    shared_items = []
    score = 0

    for rucksack in input_text.read().split('\n'):
        comp1 = rucksack[:len(rucksack)//2]
        comp2 = rucksack[len(rucksack)//2:]
        for i1 in comp1:
            if i1 in comp2:
                shared_items.append(i1)
                break
    for char in shared_items:
        if char.islower():
            s = string.ascii_lowercase.index(char) + 1
        else:
            s =  string.ascii_lowercase.index(char.lower()) + 1 + 26
        score += s

    print(score)


main()