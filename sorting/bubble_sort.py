"""Implementation of the bubble sort algorithm.

"Loop through the list n - 1 times, and each time you are moving the largest unsorted element to its final position."

Invariants:
    - After each iteration, the largest unsorted element get put into its final position

This algorithm is stable, because only consecutive elements are swapped using the strict comparison '<' to ensure
elements of the same value will not swap places with one another to maintain relative order.

This algorithm is incremental given that new elements are appended to the front of the list, so that it takes one
iteration of swaps to move that new element to its correct position.
"""


def bubble_sort(lst: list) -> None:
    """Sorts a list in ascending order using bubble sort algorithm.

    @complexity: best - O(n), when list is sorted. worst - O(n^2), when list is in decending order.
    """
    n = len(lst)
    if n == 0 or n == 1:
        return
    for boundary in range(n, 1, -1):
        swapped = False
        for i in range(1, boundary):
            if lst[i - 1] > lst[i]:
                swap(lst, i - 1, i)
                swapped = True
        if not swapped:  # if list is now sorted
            return


def swap(lst: list, index_1: int, index_2: int) -> None:
    """Swap element at index_1 with element at index_2"""
    lst[index_1], lst[index_2] = lst[index_2], lst[index_1]
