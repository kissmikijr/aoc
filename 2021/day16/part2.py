from functools import reduce
import operator


def main():
    matrix = []
    with open('input.txt') as matrix:
        matrix = matrix.read()

    hex_to_bits = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    bit = "".join([hex_to_bits[x] for x in matrix])
    _, result = handle_packet(bit)

    print("RESULT: ", result)


def handle_packet(bit_string):
    only_zeros = sum([int(x) for x in bit_string])
    if len(bit_string) < 6 or only_zeros == 0:
        return "", 0
    type_id = int(bit_string[3:6], 2)
    if type_id == 4:
        value = bit_string[6:]
        step = 0
        literal_value = ""
        while True:
            bits = value[step:step + 5]
            literal_value += bits[1:]
            if bits[0] == "0":
                break
            step += 5
        return bit_string[6 + step + 5:], int(literal_value, 2)

    else:
        bts, res = handle_sub_packet(bit_string)
        if type_id == 0:
            return bts, sum(res)
        elif type_id == 1:
            return bts, reduce(operator.mul, res)
        elif type_id == 2:
            return bts, min(res)
        elif type_id == 3:
            return bts, max(res)
        elif type_id == 5:
            return bts, 1 if res[0] > res[1] else 0
        elif type_id == 6:
            return bts, 1 if res[0] < res[1] else 0
        elif type_id == 7:
            return bts, 1 if res[0] == res[1] else 0


def handle_sub_packet(bit_string):
    length_type_id = bit_string[6]
    if length_type_id == "0":
        sub_packet_length = int(bit_string[7:22], 2)
        length = 0
        sub_packet = bit_string[22:]
        prev_sub_packet = sub_packet
        res = []
        while length != sub_packet_length:
            sub_packet, lv = handle_packet(sub_packet)
            length += len(prev_sub_packet) - len(sub_packet)
            res.append(lv)
            prev_sub_packet = sub_packet

        return sub_packet, res
    elif length_type_id == "1":
        number_of_subpackets = int(bit_string[7:18], 2)

        sub_packet = bit_string[18:]
        res = []
        for _ in range(number_of_subpackets):
            sub_packet, lv = handle_packet(sub_packet)
            res.append(lv)

        return sub_packet, res


if __name__ == "__main__":
    main()