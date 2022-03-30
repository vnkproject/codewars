
# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for
# a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
def find_outlier1(integers):
    odd = [i for i in integers if i % 2]
    even = [i for i in integers if not i % 2]
    return even[0] if len(odd) > len (even) else odd[0]


def find_outlier2(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]


def find_outlier3(integers):
    even = filter(lambda x: x % 2 == 0, integers)
    return even[0] if len(even) == 1 else list(set(integers) - set(even))[0]



if __name__ == "__main__":
    print(find_outlier1([2, 4, 6, 8, 10, 3]))
    print(find_outlier2([2, 4, 0, 100, 4, 11, 2602, 36]))
    print(find_outlier3([160, 3, 1719, 19, 11, 13, -21]))