'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    box = []  # make a box
    window = k  # Set the length of the window, k
    # do a for loop for the length of the window through the array by positioning
    slider_stop = len(nums) - 3
    for i in range(0, slider_stop):
        for i in range(nums[i], nums[(i+window)]):
            # within the range of that window, return the max()
            box.append(max(nums))
    return box


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
