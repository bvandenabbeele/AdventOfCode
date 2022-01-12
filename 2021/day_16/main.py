def read_file(fp):
    with open(fp) as f:
        data = f.read()

    return data


HEX_DICT = {
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
    "F": "1111"
}


def hex_to_binary(string):
    binary = ""
    for s in string:
        binary += _hex_to_binary(s)

    return binary


def _hex_to_binary(s):
    return HEX_DICT[s]


def binary_to_decimal(s):
    l = len(s)
    d = 0
    for i in range(l):
        d += int(s[i]) * 2**(l - i - 1)

    return d


class Packet:
    def __init__(self, binary) -> None:
        self.binary = binary

        self.version = self.get_version()
        self.packet_type_id = self.get_packet_type_id()

        if self.packet_type_id == 4:
            self.value = self.get_literal_value()
            self.subpackets = None

        else:
            self.subpackets = self.get_subpackets()
            self.value = self.compute_value()

        assert isinstance(self.value, int), "value is not of type int"

    def get_version(self):
        return binary_to_decimal(self.binary[:3])

    def get_packet_type_id(self):
        return binary_to_decimal(self.binary[3:6])

    def get_literal_value(self):
        assert self.packet_type_id == 4, "Packet does not contain literal value"

        length = 5
        lead = 1
        i = 0
        number = ""
        while lead != "0":
            lead = self.binary[6 + i*length]
            number += self.binary[6 + i*length + 1:6 + (i + 1)*length]

            i += 1

        self.binary = self.binary[:6 + i*length]
        return binary_to_decimal(number)

    def get_length_type_id(self):
        assert self.packet_type_id != 4, "Packet does not contain subpackets"

        return int(self.binary[6])

    def get_length_bits(self, length_type_id):
        assert self.packet_type_id != 4, "Packet does not contain subpackets"

        if length_type_id == 1:
            return 11
        else:
            return 15

    def get_subpacket_length(self, length_bits):
        assert self.packet_type_id != 4, "Packet does not contain subpackets"

        return binary_to_decimal(self.binary[7:7 + length_bits])

    def get_subpackets(self):
        assert self.packet_type_id != 4, "Packet does not contain subpackets"

        length_type_id = self.get_length_type_id()
        length_bits = self.get_length_bits(length_type_id)

        subpacket_string = self.binary[6 + 1 + length_bits::]
        self.binary = self.binary[:6 + 1 + length_bits]

        if length_type_id == 1:
            return self._subpackets_by_number(subpacket_string, self.get_subpacket_length(length_bits))

        else:
            return self._subpackets_by_length(subpacket_string, self.get_subpacket_length(length_bits))

    def _subpackets_by_length(self, subpackets_string, subpackets_length):
        subpackets = list()
        length = 0
        while length < subpackets_length:
            packet = Packet(subpackets_string[length::])
            length += len(packet)
            subpackets.append(packet)

        return subpackets

    def _subpackets_by_number(self, subpackets_string, subpackets_number):
        subpackets = list()
        length = 0
        while len(subpackets) < subpackets_number:
            packet = Packet(subpackets_string[length::])
            length += len(packet)
            subpackets.append(packet)

        return subpackets

    def __len__(self):
        length = len(self.binary)
        if self.subpackets is not None:
            length += sum([len(p) for p in self.subpackets])

        return length

    def compute_value(self):
        if self.packet_type_id == 0:
            return self._sum()

        elif self.packet_type_id == 1:
            return self._multiply()

        elif self.packet_type_id == 2:
            return self._min()

        elif self.packet_type_id == 3:
            return self._max()

        elif self.packet_type_id == 5:
            return self._gt()

        elif self.packet_type_id == 6:
            return self._lt()

        elif self.packet_type_id == 7:
            return self._eq()

    def _sum(self):
        x = 0
        for packet in self.subpackets:
            x += packet.value

        return x

    def _multiply(self):
        x = 1
        for packet in self.subpackets:
            x *= packet.value

        return x

    def _max(self):
        return max(self.subpackets).value

    def _min(self):
        return min(self.subpackets).value

    def _gt(self):
        return 1 if self.subpackets[0] > self.subpackets[1] else 0

    def _lt(self):
        return 1 if self.subpackets[0] < self.subpackets[1] else 0

    def _eq(self):
        return 1 if self.subpackets[0] == self.subpackets[1] else 0

    def _print(self, indent=0):
        print(f"{indent*' '}{self.packet_type_id}: {self.value}")
        if self.subpackets is not None:
            for p in self.subpackets:
                p._print(indent+2)

    def __repr__(self):
        return f"Packet {self.binary}"

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        try:
            return self.value == other.value

        except AttributeError:
            return self.value == other


def sum_versions(packet):
    total = packet.version
    if packet.subpackets:
        for p in packet.subpackets:
            total += sum_versions(p)

    return total


if __name__ == "__main__":
    hex = read_file("input.txt")

    packet = Packet(hex_to_binary(hex))
    print(sum_versions(packet))
    print(packet.value)
