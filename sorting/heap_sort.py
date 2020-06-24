from data_structures.heap import MaxHeap


def heap_sort(lst: list) -> list:
    heap = MaxHeap(lst)
    sorted_list = []
    while not heap.is_empty():
        sorted_list.append(heap.get_max())
    return sorted_list
