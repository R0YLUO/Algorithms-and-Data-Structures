"""Implementation of the quick sort algorithm. List is sorted in ascending order."""


def quick_sort(lst: list) -> None:
    """Sort list in ascending order

    @complexity: best - O(n*log(n)), when partition is the good (median). worst - O(n^2), when partition is bad (lowest
    or highest value in the list)
    """

    if len(lst) == 0 or len(lst) == 1:
        return
    quick_sort_aux(lst, 0, len(lst) - 1)


def quick_sort_aux(lst: list, start: int, end: int) -> None:
    if start < end:
        index_of_partition = partition(lst, start, end)
        quick_sort_aux(lst, start, index_of_partition - 1)
        quick_sort_aux(lst, index_of_partition + 1, end)


def partition(lst: list, start: int, end: int) -> int:
    """Partition list, using element in the middle as the pivot."""
    median_index = (start + end) // 2
    pivot = lst[median_index]
    lst[start], lst[median_index] = lst[median_index], lst[start]
    boundary = start + 1  # everything to the left of boundary should be less or equal to boundary
    for i in range(boundary, end + 1):
        if lst[i] < pivot:
            lst[i], lst[boundary] = lst[boundary], lst[i]
            boundary += 1
    lst[start], lst[boundary - 1] = lst[boundary - 1], lst[start]
    return boundary - 1
