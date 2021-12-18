import unittest

from main import Packet, sum_versions, hex_to_binary


class ParserTest(unittest.TestCase):
    t_1 = "D2FE28"
    t_2 = "38006F45291200"
    t_3 = "EE00D40C823060"
    t_4 = "8A004A801A8002F478"
    t_5 = "620080001611562C8802118E34"
    t_6 = "C0015000016115A2E0802F182340"
    t_7 = "A0016C880162017C3686B18A3D4780"
    t_8 = "C200B40A82"
    t_9 = "04005AC33890"
    t_10 = "880086C3E88112"
    t_11 = "CE00C43D881120"
    t_12 = "D8005AC2A8F0"
    t_13 = "F600BC2D8F"
    t_14 = "9C005AC2F8F0"
    t_15 = "9C0141080250320F1802104A08"

    def _test(self, string, **kwargs):
        packet = Packet(hex_to_binary(string))

        for key, value in kwargs.items():
            self.assertEqual(getattr(packet, key), value)

        return packet

    def test_1(self):
        self._test(self.t_1, version=6, packet_type_id=4, value=2021)

    def test_2(self):
        packet = self._test(self.t_2, version=1, packet_type_id=6)
        self.assertEqual(len(packet.subpackets), 2)

    def test_3(self):
        packet = self._test(self.t_3, version=7, packet_type_id=3)
        self.assertEqual(len(packet.subpackets), 3)

    def test_4(self):
        packet = self._test(self.t_4)
        self.assertEqual(sum_versions(packet), 16)

    def test_5(self):
        packet = self._test(self.t_5)
        self.assertEqual(sum_versions(packet), 12)

    def test_6(self):
        packet = self._test(self.t_6)
        self.assertEqual(sum_versions(packet), 23)

    def test_7(self):
        packet = self._test(self.t_7)
        self.assertEqual(sum_versions(packet), 31)

    def test_8(self):
        self._test(self.t_8, value=3)

    def test_9(self):
        self._test(self.t_9, value=54)

    def test_10(self):
        self._test(self.t_10, value=7)

    def test_11(self):
        self._test(self.t_11, value=9)

    def test_12(self):
        self._test(self.t_12, value=1)

    def test_13(self):
        self._test(self.t_13, value=0)

    def test_14(self):
        self._test(self.t_14, value=0)

    def test_15(self):
        self._test(self.t_15, value=1)


if __name__ == "__main__":
    unittest.main()