def sort(arr):
    n = len(arr)
    while n > 1:
        nova_posicao_limite = 0
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                nova_posicao_limite = j + 1
        n = nova_posicao_limite
    return arr
