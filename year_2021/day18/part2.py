import re
import math


def add(left, right):
    return f"[{left},{right}]"


def add_to_left_regular_number(number, num_to_add, span):
    left_sub_string = number[:span[0]]
    right_sub_string = number[span[0]:]

    r = re.finditer(r"([0-9]+)", left_sub_string)
    last_from_left = None
    for i in r:
        last_from_left = i
    if last_from_left:
        new_number = int(last_from_left.group(1)) + num_to_add
        start, end = last_from_left.span()[0], last_from_left.span()[1]
        left_sub_string = left_sub_string[:start] + str(
            new_number) + left_sub_string[end:]

        return left_sub_string + right_sub_string

    return number


def add_to_right_regular_number(number, num_to_add, span):
    left_sub_string = number[:span[1] + 1]
    right_sub_string = number[span[1] + 1:]

    r = re.search(r"([0-9]+)", right_sub_string)
    if r:
        new_number = int(r.group(1)) + num_to_add

        start, end = r.span()[0], r.span()[1]
        right_sub_string = right_sub_string[:start] + str(
            new_number) + right_sub_string[end:]

        return left_sub_string + right_sub_string

    return number


def get_exploded_values(number):
    r = re.search(r"\[(\d+),(\d+)\]", number)
    if r:
        return r.group(1), r.group(2), r.group(0), r.span()


def explode(number):
    depth = 0
    is_explode = False
    for i, c in enumerate(number):
        if depth == 5:
            l, r, explode_string, span = get_exploded_values(number[i - 1:])

            number = add_to_left_regular_number(
                number, int(l), (i - 1 + span[0], i - 1 + span[1]))
            number = add_to_right_regular_number(
                number, int(r), (i - 1 + span[0], i - 1 + span[1]))

            r_number = number[i - 1:].replace(explode_string, '0', 1)
            l_number = number[:i - 1]
            number = l_number + r_number
            is_explode = True
            break

        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
    return number, is_explode


def split_left_most_regular_greater_than_10(number):
    r = re.search(r"([1-9]\d+)", number)
    if r:
        new_pattern = f"[{int(int(r.group(1)) / 2)},{math.ceil(int(r.group(1)) / 2)}]"
        pattern = r.group(0)
        pattern = pattern.replace(r.group(1), new_pattern, 1)
        new_string = re.sub(re.escape(r.group(0)), pattern, number, 1)

        return new_string, True
    return number, False


def reduce(number):
    is_explode = True
    is_split = True
    while is_explode or is_split:
        number, is_explode = explode(number)
        if is_explode:
            continue
        number, is_split = split_left_most_regular_greater_than_10(number)

    return number


def get_magnitude(number):
    r = re.finditer(r"\[(\d+),(\d+)\]", number)
    is_match = False
    for match in r:
        is_match = True
        new_number = int(match.group(1)) * 3 + int(match.group(2)) * 2
        number = re.sub(re.escape(match.group(0)), str(new_number), number, 1)
    return number, is_match


def main():
    matrix = []
    with open('input.txt') as matrix:
        matrix = [y for y in matrix.read().split("\n")]

    result = matrix[0]
    magnitudes = []
    for i in range(len(matrix) - 1):

        for j in range(len(matrix) - 1):
            if i == j:
                continue
            added = add(matrix[i], matrix[j])
            result = reduce(added)
            is_match = True
            while is_match:
                result, is_match = get_magnitude(result)
            magnitudes.append(int(result))
    print(max(magnitudes))


if __name__ == "__main__":
    main()