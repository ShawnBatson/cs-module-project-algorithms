'''
Input: an integer
Returns: an integer
'''
import functools

# THIS IS MINE UNDERNEATH V
# def eating_cookies(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# THIS IS ARTEMS AH UNDERNEATH


# def eating_cookies(n):
#     # base case
#     # get to the base case
#     number_of_ways = 1
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1

#     # how can we get back to the base case? (n-1) = eaing one cookie, (n-2) is eating two at once, and (n-3) is eating 3 at a time

#     # what if I ate just one cookie
#     number_of_ways = eating_cookies(
#         n-1) + eating_cookies(n-2) + eating_cookies(n-3)

#     return number_of_ways

# DYNAMIC VERSIO


def eating_cookies(n, cache):
    number_of_ways = 1
    if n < 0:
        return 0
    if n == 0:
        return 1

    # before we try to solve the problem,
    # lets see if the answer is already stored in cache
    if cache[n] > 0:
        # this must have been precomputed
        return cache[n]

    number_of_ways = eating_cookies(
        n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    cache[n] = number_of_ways

    return number_of_ways


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
