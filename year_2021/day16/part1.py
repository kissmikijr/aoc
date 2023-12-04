def main():
    matrix = []
    with open('input.txt') as matrix:
        matrix = matrix.read()
    print(matrix)

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
    print(bit)
    version_sum = 0
    while True:
        version, type_id, next_packet = handle_packet(bit)
        print(version, next_packet)
        if next_packet == "":
            break
        version_sum += version
        bit = next_packet

    print(version_sum)


def handle_packet(bit_string):
    print("Packet: ", bit_string)
    only_zeros = sum([int(x) for x in bit_string])
    if len(bit_string) < 6 or only_zeros == 0:
        return 0, 0, ""
    version = int(bit_string[:3], 2)
    type_id = int(bit_string[3:6], 2)
    print("version: ", version, "type_id: ", type_id)
    if type_id == 4:
        value = bit_string[6:]
        step = 0
        while True:
            bits = value[step:step + 5]
            if bits[0] == "0":
                break
            step += 5
        return version, type_id, bit_string[6 + step + 5:]
    else:
        length_type_id = bit_string[6]
        print("length type id: ", length_type_id)
        if length_type_id == "0":
            sub_packet_length = int(bit_string[7:22], 2)
            print("sub packet length: ", sub_packet_length)
            length = 0
            sub_packet = bit_string[22:]
            prev_sub_packet = sub_packet
            while length != sub_packet_length:
                v, _, sub_packet = handle_packet(sub_packet)
                length += len(prev_sub_packet) - len(sub_packet)
                version += v
                prev_sub_packet = sub_packet

            return version, type_id, sub_packet
        elif length_type_id == "1":
            number_of_subpackets = int(bit_string[7:18], 2)

            sub_packet = bit_string[18:]
            for _ in range(number_of_subpackets):
                v, _, sub_packet = handle_packet(sub_packet)
                version += v

            return version, type_id, sub_packet


if __name__ == "__main__":
    main()