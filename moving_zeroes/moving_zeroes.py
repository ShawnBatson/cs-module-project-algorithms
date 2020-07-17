'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # make a container to return with the new array
    box = []
    # make a for loop for a list and check if each number is a 0 or not
    for x in arr:
        if x == 0:  # if the number is not a 0, add it to the array in the end position
            box.append(x)
        # if the numbee is a 0, add it to the new array in the [0] position
        else:
            box.insert(0, x)
    return box
    # return the array


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
