def binarySearch(arr, target):
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right)// 2 
        if arr[mid] ==  target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
A = [0, 2, 4, 6, 8, 10]
print(binarySearch(A, 2))

        