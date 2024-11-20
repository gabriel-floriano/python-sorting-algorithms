def merge(left, right):
    result = []
    index_left, index_right = 0, 0
    while index_left < len(left) and index_right < len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
    result.extend(left[index_left:])
    result.extend(right[index_right:])
    return result

def sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])
    return merge(left, right)
