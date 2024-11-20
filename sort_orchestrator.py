import random
import time
from countingSort import sort as counting_sort
from bucketSort import bucket_sort
from heapSort import sort as heap_sort
from insertionSort import sort as insertion_sort
from mergeSort import sort as merge_sort
from quickSort import sort as quick_sort
from radixSort import sort as radix_sort
from selectionSort import sort as selection_sort
from shellSort import sort as shell_sort
from bubbleSort import sort as bubble_sort
from bubbleSortMelhorado import sort as bubble_sort_melhorado

def generate_random_array(size, min_val=0, max_val=100000, float_values=False):
    if float_values:
        return [random.uniform(min_val, max_val) for _ in range(size)]
    return [random.randint(min_val, max_val) for _ in range(size)]

def test_sorting_algorithm(algorithm, arrays):
    results = []
    for arr in arrays:
        times = []
        print(f"Executando {algorithm.__name__} com array de tamanho {len(arr)}...")
        for i in range(10):  # Executar 10 vezes
            try:
                test_array = arr.copy()
                start_time = time.time()
                algorithm(test_array)
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"  Execução {i + 1}: {elapsed_time:.5f} segundos")
                times.append(elapsed_time)
            except Exception as e:
                print(f"  Erro na execução {i + 1}: {e}")
                times.append(None)  # Marca erro com None
        # Calcula a média ignorando erros
        valid_times = [t for t in times if t is not None]
        avg_time = sum(valid_times) / len(valid_times) if valid_times else None
        results.append(avg_time)
    return results

def main():
    sizes = [10000, 50000, 100000]
    arrays_for_general = [generate_random_array(size) for size in sizes]
    arrays_for_float = [generate_random_array(size, min_val=0, max_val=1, float_values=True) for size in sizes]

    algorithms = {
        "bubbleSort": (bubble_sort, arrays_for_general),
        "bubbleSortMelhorado": (bubble_sort_melhorado, arrays_for_general),
        "bucketSort": (bucket_sort, arrays_for_float),
        "countingSort": (counting_sort, arrays_for_general),
        "heapSort": (heap_sort, arrays_for_general),
        "insertionSort": (insertion_sort, arrays_for_general),
        "mergeSort": (merge_sort, arrays_for_general),
        "quickSort": (quick_sort, arrays_for_general),
        "radixSort": (radix_sort, arrays_for_general),
        "selectionSort": (selection_sort, arrays_for_general),
        "shellSort": (shell_sort, arrays_for_general),
    }

    print("Resultados (tempo médio em segundos):\n")
    for name, (algorithm, arrays) in algorithms.items():
        print(f"{name}:")
        times = test_sorting_algorithm(algorithm, arrays)
        for size, time_taken in zip(sizes, times):
            if time_taken is not None:
                print(f"  Array de tamanho {size}: média de {time_taken:.5f} segundos")
            else:
                print(f"  Array de tamanho {size}: erro durante as execuções")
        print()

if __name__ == "__main__":
    main()
