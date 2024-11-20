def bucket_sort(array):
    # Verifica se o array está vazio
    if not array:
        return array

    # Cria buckets
    num_buckets = len(array)
    max_value = max(array)
    buckets = [[] for _ in range(num_buckets)]

    # Distribui os elementos nos buckets
    for num in array:
        # Calcula o índice do bucket para o elemento
        index = int(num * num_buckets / (max_value + 1))
        buckets[index].append(num)

    # Ordena cada bucket e combina os resultados
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array
