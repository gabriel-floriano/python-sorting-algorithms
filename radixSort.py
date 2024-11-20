def get_index(item, exp):
    return (item // exp) % 10

def sort(arr):
    if not arr:
        return arr
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = get_index(arr[i], exp)
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            index = get_index(arr[i], exp)
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        arr[:] = output
        exp *= 10
    return arr
