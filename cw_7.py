# Define a function that takes one integer argument and returns logical value true or false depending on if the
# integer is a prime.
# # Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other
# than 1 and itself.

def is_prime(num):
    if num > 1:
        i, j = 2, 0
        while (i*i <= num) and (j != 1):
            j = 1 if num % i == 0 else 0
            i += 1
        return False if j == 1 else True
    else:
        return False

# The BEST
# def is_prime(n):
#     return lambda n: n > 1 and not any(i for i in range(2, int(n**.5)+1) if not n % i)


if __name__ == "__main__":
    print(is_prime(5))
    print(is_prime(7))
    print(is_prime(8))
    print(is_prime(11))
    print(is_prime(27))