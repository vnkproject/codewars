# Your task is to make a function that can take any non-negative integer as an argument and return it with its
# digits in descending order. Essentially, rearrange the digits to create the highest possible number.
def Descending_Order1(num):
    return int("".join(sorted(str(num), reverse=True)))

Descending_Order2 = lambda n: int(''.join(reversed(sorted(str(n)))))

if __name__ == "__main__":
    print(Descending_Order1(123456789))
    print(Descending_Order2(123456789))