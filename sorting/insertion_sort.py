"""Implementation of the insertion sort algorithm. Sorting is in ascending order.

"Keep looking to the left and swapping until you see an element that is smaller so you know you are in the correct
position."

The invariants for this algorithm are:
    - everything to the left of the marker is sorted, but may not be in its final position
    - after each loop, the item pointed to by the marker is sorted relative to elements on the left

This algorithm is incremental because when we append a new element to a sorted list, the marker points to the new
element, and the invariant that the elements to the left of the marker are sorted holds true, and then we keep swapping
left until the new element is in the right position, such that after the swaps, the second invariant also holds true.

This algorithm is stable because swaps are only made by consecutive elements, and the strict comparison of '<' is used
so that when elements of the same value are compared they are not swapped.
"""


def insertion_sort(lst: list) -> None:
    """Sorts a list into ascending order.

    @complexity: best - O(n), when list is sorted. worst - O(n^2), when list is in descending order.
    """
    n = len(lst)
    if n == 0 or n == 1:
        return
    for marker in range(1, n):
        k = marker
        while k > 0 and lst[k] < lst[k - 1]:
            swap(lst, k, k - 1)
            k -= 1


def swap(lst: list, index_1: int, index_2: int) -> None:
    """Swaps element of lst at index_1 with element at index_2"""
    lst[index_1], lst[index_2] = lst[index_2], lst[index_1]
