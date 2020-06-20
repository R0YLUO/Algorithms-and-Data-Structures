"""
Implementation of a selection sort algorithm. Sorting is in ascending order

"Find the max, swap with marker, then increment the marker."

The invariants of this algorithm are:
    - all the elements to the left of the marker are sorted (in their correct positions).
    - all the elements to the left of the marker are smaller or equal to all the elements at the marker and to the
    right of the marker.

We know that this list is sorted after the algorithm when marker points to the last element, because of the
combination of the invariants: all elements to the left of the marker is sorted, and the element pointed to by the
marker is greater or equal to all the elements to the left of the marker. When marker is pointing to the last
element, there is no more elements to the right of the marker, and hence the whole list is therefore sorted, since
the invariant tells us the element at the marker is also at the right position.

This sorting algorithm is not incremental, as the invariant states that all the elements to the left of the marker
are sorted, and all elements to the right of the marker should be greater or equal to all the elements to the left
of the marker. If we append a new element to the end of our list, and this element is less than an element that is
on the left of the marker, the invariant is broken, and hence we will need to run the whole algorithm again in order
to sort the list.

This sorting algorithm is not stable, as swaps are not made by consecutive elements, resulting in elements of the
same value being moved over one another, and hence breaking their relative order.
"""


def selection_sort(lst: list) -> None:
    """Sorts a list of comparable objects in ascending order using the selection sort algorithm.

    :param lst: the list we are sorting.
    @complexity: best and worst - O(n^2), where n is length of the list. No functionality to make it algorithm stop
    early. Will take a marker to go through the list, and in each position of the marker, loops through the list again
    to find the max.
    """
    n = len(lst)
    if n == 0 or n == 1:  # dealing with already sorted lists
        return
    for marker in range(n - 1):
        index_of_min = find_min_index(lst, marker)
        swap(lst, marker, index_of_min)


def find_min_index(lst: list, marker: int) -> int:
    """Gets index of min element in the list to the right of the marker, including element marker is pointing to."""
    index_of_min = marker
    for i in range(marker + 1, len(lst)):
        if lst[i] < lst[index_of_min]:
            index_of_min = i
    return index_of_min


def swap(lst: list, index_1: int, index_2: int) -> None:
    """Swaps the element at index_1 with the element of index_2."""
    lst[index_1], lst[index_2] = lst[index_2], lst[index_1]
