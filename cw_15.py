# Take the following IPv4 address: 128.32.10.1#
# This address has 4 octets where each octet is a single byte (or 8 bits).#
# 1st octet 128 has the binary representation: 10000000
# 2nd octet 32 has the binary representation: 00100000
# 3rd octet 10 has the binary representation: 00001010
# 4th octet 1 has the binary representation: 00000001
# So 128.32.10.1 == 10000000.00100000.00001010.00000001#
# Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361#
# Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.

# THE BEST
# from ipaddress import IPv4Address
# def int32_to_ip(int32):
#     return str(IPv4Address(int32))


def int32_to_ip(int32):
    return '{}.{}.{}.{}'.format(*int32.to_bytes(4, 'big'))


if __name__ == "__main__":
    int32_to_ip = lambda int32: f'{int32//256**3}.{int32//256**2%256}.{int32//256%256}.{int32%256}'
    print(int32_to_ip(2154959208))
    print(int32_to_ip(0))
    print(int32_to_ip(2149583361))
