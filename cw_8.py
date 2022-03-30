# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return
# true if the string is valid, and false if it's invalid.#
# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}.
# Thanks to @arnedag for the idea!
# # All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
import functools


def valid_braces(string):
    # Проверка на соответствие открывающих и закрывающих скобок по количеству
    # l = [y for x, y in zip('()[]{}', [list(string).count(x) for x in list('()[]{}')])]
    # l1 = [v for k, v in enumerate(l) if k % 2]
    # l2 = [v for k, v in enumerate(l) if not k % 2]
    # return functools.reduce(lambda x, y: x and y, (map(lambda p, q: p == q, l1, l2)), True)

    s1 = ['(', '[', '{']
    s2 = [')', ']', '}']
    l = []

    for s in list(string):
        if s in s2 and len(l) == 0:
            return False
        if s in s1:
            l.append(s)
        else:
            if s1[s2.index(s)] == l[-1]:
                l.pop()
            else:
                return False
    return True if len(l) == 0 else False


#The BEST

# def validBraces(s):
#     while '{}' in s or '()' in s or '[]' in s: s = s.replace('{}', '').replace('[]', '').replace('()', '')
#     return s == ''


# import re
#
# def validBraces(s):
#     while any(pair in s for pair in ("{}", "[]", "()")):
#         s = re.sub(r"{}|\[]|\(\)", "", s)
#     return not stg



if __name__ == "__main__":
    print(valid_braces('([{'))
    print(valid_braces('({{[[]]}})'))
    print(valid_braces('())({}}{()][]['))
    print(valid_braces('))({}}{()][]['))