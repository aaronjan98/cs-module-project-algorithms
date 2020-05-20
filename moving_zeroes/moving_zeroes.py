'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    new_arr = []
    count = 0
    for i in range(len(arr)):
        print(i, arr[i])
        if arr[i] > 0 or arr[i] < 0:
            print('in', arr[i])
            new_arr.append(arr[i])
        else:
            count += 1
    for i in range(count):
        new_arr.append(0)
    print(new_arr)
    arr = new_arr
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")