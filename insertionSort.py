def sort(arr):
    for i in range(1, len(arr)):
        aux = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > aux:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = aux
    return arr
