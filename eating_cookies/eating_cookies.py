'''
Input: an integer
Returns: an integer
'''
import functools


def eating_cookies(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


cache = {}


# def eating_cookies(n, cache):
#     if n == 0:
#         cache[0] = 1
#         return 1
#     if n == 1:
#         cache[1] = 1
#         return 1
#     if n == 2:
#         cache[2] = 2
#         return 2
#     if n == 3:
#         cache[3] = 4
#         return 4
#     if n in cache:
#         return cache[n]
#     return eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
