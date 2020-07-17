'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# MINE UNDERNEATH


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

# ARTEMS UNDERNEATH


def sliding_window_maxA(nums, k):
    output_arr = []

    for i in range(len(nums) - k + 1):
        current_window = nums[i:i+k]
        current_max = max(current_window)
        output_arr.append(current_max)
    return output_arr

# def sliding_window_max_queue(nums, k):
    # create a queue that stores useful numbers
    # insert the first K elements
    # for each element, we add
    # all smaller numbers in the queue, remove them

    # add the number to the end of the queue

    # process the remaining elements in nums
    # from K to n-1
    # the element at the front of the queue
    # is the largest number of the current window
    # so save that number into our output


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
