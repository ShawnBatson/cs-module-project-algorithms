# dynamic programming
# - instead of repeat the same steps and same results, we can Cache results we've already done

import time
import functools


@functools.lru_cache()  # decorator for creating a memoized cahce automatically
def fibonacci(n):
    # base case
    if (n == 0):
        return 0
    if (n == 1):
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

# memoization = cache the results of your function calls.
# {
# input_to_function: result_given_that_input
# 1: mem_fibbonaci(1) == 1
# 2: mem_fibbonaci(2) == 1
# 3: mem_fibbonaci(3) == 2
# 4: mem_fibbonaci(4) == 3
# }


cache = {}  # memo cache for function calls. This is global, there is another method that keeps it local.  The method is in coments near what needs to be changed


def mem_fibonacci(n):
    # or mem_fibonnacci(n, cache)
    # base case
    if (n == 0):
        cache[0] = 0
        return 0
    if (n == 1):
        cache[1] = 1
        return 1

    # I want to get the answer for fibonacci at n
    # let me check if I already have that value in my cahce
    if n in cache:
        return cache[n]

    result_n_1 = mem_fibonacci(n-1)  # pass the cache around as in (n-1, cache)
    result_n_2 = mem_fibonacci(n-2)  # pass the cache around as in (n-1, cache)
    result_at_n = result_n_1 + result_n_2

    cache[n] = result_at_n

    return result_at_n

# tabulation example.  Start to 0 and go UP to (n)


def tab_fibonacci(n):

    # start at n=0 and n=1, loop until we reach n, and keep adding two prev numbers.
    # [0, 0, 0, 0, 0, 0] length <- N
    # [0, 1, 1, 2, 3 .....]
    # this makes an array of a bunch of zeros
    solution_table = [0 for _ in range(0, n+1)]
    solution_table[0] = 0
    solution_table[1] = 1

    for i in range(2, n+1):
        solution_table[i] = solution_table[i-1] + solution_table[i-2]

    return solution_table[n]


tab_fibonacci(7)


start = time.time()
print(f'{fibonacci(7)}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n------------------------------------\n')

start = time.time()
print(f'{fibonacci(35)}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n------------------------------------\n')

start = time.time()
# or mem_fibonacci(35, {})}') to keep the cache from being a global variable.
print(f'{mem_fibonacci(35)}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n------------------------------------\n')

# to get memoization to work, you need a memo-cache, which is a dictionary where the keys are your input to the function. The value is the result of the function call
