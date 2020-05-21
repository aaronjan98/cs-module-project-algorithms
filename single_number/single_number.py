'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set( x for x in arr if x in seen or seen_add(x))
    seen_all = set(arr)
    seen_all.difference_update(seen_twice)
    # turn the set into a list (as requested)
    return list(seen_all)[0]
    
'''
# old attempted solution
    temp = []
    temp.append(arr[0])

    print(temp)

    if not arr[1]:
        return temp[0]

    for el in range(1, len(arr), 1):
        # print('el')
        if temp[0]:
            for i in range(0, len(temp)):
                # print(arr[el], temp[i])
                if arr[el] == temp[i]:
                    # print(i)
                    temp.pop(i)
                    # if the next value in arr does exist append it to temp
                    if arr[el+1]:
                        temp.append(arr[el+1])
                else:
                    temp.append(arr[el])
    print(temp)
    return temp[0]
'''

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 9, 11, 12, 11]

    print(f"The odd-number-out is {single_number(arr)}")