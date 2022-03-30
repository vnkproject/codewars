# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
# these multiples is 23.
# # Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    return sum([x for x in range(number) if x and (x % 3 == 0 or x % 5 == 0)]) if number > 0 else 0

# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).


def to_camel_case1(text):
    return text[0] + "".join([s.capitalize() for s in text.replace('-','_').split('_')])[1::] if text else text


def to_camel_case2(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


import re
def to_camel_case3(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)


# Write a function that takes an integer as input, and returns the number of bits that are equal
# to one in the binary representation of that number. You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits1(n):
    return len([l for l in bin(n) if l == '1'])

def count_bits2(n):
    return bin(n).count("1")


# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your
# most secret question is still correct. However, since someone could look over your shoulder, you don't want
# that shown on your screen. Instead, we mask it.
# Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(cc):
    return "#"*len(cc[:-4]) + cc[-4:] if len(cc) > 4 else cc



if __name__ == "__main__":
    print(solution(10))

    print(to_camel_case1('the_stealth_warrior'))
    print(to_camel_case2('The-Stealth-Warrior'))
    print(to_camel_case2('A-B-C'))

    print(count_bits1(1234))
    print(count_bits2(1234))

    print(maskify("64607935616"))
    print(maskify("4556364607935616"))