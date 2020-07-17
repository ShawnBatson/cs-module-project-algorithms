import math

radius = 3
area = math.pi * radius * radius

print(f'The area of the circle is {area:.3f}')
# return the area with max three decimal plaes.


# write a function to determine if a number divides itself (huh?)
# 128 divides itself, since 1, 2, and 8, divide into 128 evenly
# 0 does not divide into anything evenly.
# input questions
# output questions : boolean
def divide_self(num):
    # make an original copy of num
    original = num
    # loop over each digit in num (while loop)
    #   get the right most digit of num by num % 10
    #       If the digit is 0, return false right away.
    #   take that digit and get remainder of original num / digit
    #   if remainder is 0, carry on
    #   if remainder is NOT 0, return false
    #   128 // 10 = 12 (removed last digit from number using integer division)

    # return True
    pass


print(divide_self(128))  # -> true
print(divide_self(12))  # -> true
print(divide_self(120))  # - false
