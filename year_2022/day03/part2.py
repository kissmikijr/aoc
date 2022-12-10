import string

def main():
    input_text = open('input.txt', 'r')
    shared_items = []
    score = 0
    rucksacks = input_text.read().split('\n')
    i = 0
    while i +2 < len(rucksacks):
        r1 = rucksacks[i]
        r2 = rucksacks[i+1]
        r3 = rucksacks[i+2]
        for item in r1:
            if item in r2:
                if item in r3:
                    shared_items.append(item)
                    break
        i += 3
    for char in shared_items:
        if char.islower():
            s = string.ascii_lowercase.index(char) + 1
        else:
            s =  string.ascii_lowercase.index(char.lower()) + 1 + 26
        score += s

    print(score)


main()