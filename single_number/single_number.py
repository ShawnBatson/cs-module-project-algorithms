'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    for i in range(len(arr)):   # set the length of the array for use
        j = 0   # set a second hand pointer
        while (j < len(arr)):  # while the second hand pointer is still within range of the length of the array
            if (i != j and arr[i] == arr[j]):  # if the loop I == J pointer
                break  # move along
            j += 1  # Add another count to the secondary pointer and go through the list
        if (j == len(arr)):  # if the second pointer is at the end, that means the end is the only non-repeated
            return arr[i]  # return the non-repeated


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
