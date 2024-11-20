def sort(arr):
    for i in range(len(arr)):
        posicao_menor = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[posicao_menor]:
                posicao_menor = j
        arr[i], arr[posicao_menor] = arr[posicao_menor], arr[i]
    return arr
