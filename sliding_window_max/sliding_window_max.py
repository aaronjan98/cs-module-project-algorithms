'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    global max_array
    max_array = []
    window = nums[0:k]
    for i in range(k, len(nums)+1):
        window = nums[i-k: i]
        print(window)
        max = window[0]
        for el in window:
            if el > max:
                max = el
        max_array.append(max)
    return max_array

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
