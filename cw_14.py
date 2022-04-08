# Problem Context
# The Fibonacci sequence is traditionally used to explain tree recursion.
#
# def fibonacci(n):
#     if n in [0, 1]:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

# This algorithm serves welll its educative purpose but it's tremendously inefficient, not only because of recursion,
# but because we invoke the fibonacci function twice, and the right branch of recursion (i.e. fibonacci(n-2))
# recalculates all the Fibonacci numbers already calculated by the left branch (i.e. fibonacci(n-1)).#
# This algorithm is so inefficient that the time to calculate any Fibonacci number over 50 is simply too much.
# You may go for a cup of coffee or go take a nap while you wait for the answer. But if you try it here in Code Wars
# you will most likely get a code timeout before any answers.#
# For this particular Kata we want to implement the memoization solution. This will be cool because it will let us
# keep using the tree recursion algorithm while still keeping it sufficiently optimized to get an answer very rapidly.#
# The trick of the memoized version is that we will keep a cache data structure (most likely an associative array)
# where we will store the Fibonacci numbers as we calculate them. When a Fibonacci number is calculated, we first look
# it up in the cache, if it's not there, we calculate it and put it in the cache, otherwise we returned the cached
# number.
# Refactor the function into a recursive Fibonacci function that using a memoized data structure avoids the deficiencies
# of tree recursion Can you make it so the memoization cache is private to this function?


# Улучшенная классика
# def fib(n):
#     if n == 0:
#         return (0, 1)
#     if n == 1:
#         return (1, 1)
#     num_fib = fib(n-1)
#     return (num_fib[1], num_fib[0] + num_fib[1])
#
# def fibonacci(n):
#     return fib(n-1)[1]


# Мемоизация мое решение (словарь определяется вне функции)
_fib = {0: 0, 1: 1}
def fibonacci(n):
    result = _fib.get(n)
    if result is None:
        _fib[n] = fibonacci(n-1) + fibonacci(n-2)
    return _fib[n]


# Мемоизация на списке
# def fibonacci(n):
#   fib = [0,1]
#   for i in range(2, n+1):
#     fib.append(fib[i-1] + fib[i-2])
#   return fib[n]


# Мемоизация на словаре (словарь определяется внутри функции)
# def fibonacci(m):
#     cache = {0: 0, 1: 1}
#     def fib(n):
#         if n not in cache:
#             cache[n] = fib(n-1)+fib(n-2)
#         return cache[n]
#     return fib(m)


# Используем декоратор из functool
# from functools import lru_cache
# @lru_cache(None)
# def fibonacci(n):
#     if n in [0, 1]:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)


# Итерация
# def fib(n):
#     a, b = 0, 1
#     while n > 0:
#         a, b = b, a + b
#         n -= 1
#     return a


# Замыкание
# def fibonacci(n):
#      f = outer()
#      for i in range(n-1):
#          num = f()
#      return num
#
# def outer():
#     x1, x2 = 0, 1
#     def inner():
#         nonlocal x1, x2
#         x1, x2 = x2, x1 + x2
#         return x2
#     return inner


# Генератор
# def fib():
#     fib1, fib2 = 0, 1
#     while True:
#         fib1, fib2 = fib2, fib1 + fib2
#         yield fib1
#
# def fibonacci(n):
#     f = fib()
#     for _ in range(n):
#         fib_num  = next(f)
#     return fib_num


if __name__ == "__main__":
    print(fibonacci(10))
