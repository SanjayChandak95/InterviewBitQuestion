'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


def find_police(arr, key, max_range):
    l, r = 0, len(arr) - 1
    ans = -1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] > max_range:
            r = mid-1
        elif arr[mid] >= key:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans


def thief_caught_helper(road):
    thief_caught = 0
    police_arr = []
    thief_arr = []
    offset = 0
    for index, person in enumerate(road):
        if person == 'P':
            police_arr.append(index)
        else:
            thief_arr.append(index)
    for thief_index in thief_arr:
        police_index = find_police(police_arr[offset:], thief_index - k, thief_index+k)
        if police_index != -1:
            thief_caught += 1
        offset = offset + police_index + 1
    return thief_caught


def get_thief(arr, n, k):
    thief_caught = 0
    if n <= k:
        for road in arr:
            police_count = 0
            thief_count = 0
            for person in road:
                if person == 'P':
                    police_count += 1
                else:
                    thief_count += 1
            thief_caught += min(thief_count, police_count)

    else:
        for line, road in enumerate(arr):
            temp = thief_caught_helper(road)
            thief_caught += temp
    return thief_caught


# Write your code here
if __name__ == '__main__':
    # for _ in range(int(input())):
    #     n, k = map(int, input().split())
    #
    #     arr = [list(input().split()) for i in range(n)]
    #     print(get_thief(arr, n, k))
    n, k = 12, 2
    arr = ['T T T P P P P P P P P P'.split(),
           'P P P P P P P P P P P P'.split(),
           'P P P P P P P P P P P P'.split(),
           'P P P P P P P P P P P P'.split(),
           'P P P P P P P P P P P P'.split(),
           'P P P P P P P P P P P P'.split(),
           'P P P P P P P P P P P P'.split(),
           'P P P P P P P P P P P P'.split(),
           'P P P P P P P P P P P P'.split(),
           'P P P P P P P P P P P P'.split(),
           'P P P P P P P P P P P P'.split(),
           'P P P P P P P P P P P P'.split()]
    print(get_thief(arr, n, k))
