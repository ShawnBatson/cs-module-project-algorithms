'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    box = []  # make a box
    windowFirst = 0  # set the window range
    windowLast = windowFirst+(k-1)  # set the window last range end
    while windowLast != len(nums):  # while window last doesn't exceed length
        curMax = nums[windowFirst]  # set a current max
        # iterate through window
        for i in range(windowFirst, windowLast+1):

            if nums[i] > curMax:  # if the iterative is less than max,
                curMax = nums[i]  # make new max
        box.append(curMax)  # append it
        # move the window by 1
        windowFirst += 1  # move the window
        windowLast += 1  # move the window
    return box  # return the box


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
