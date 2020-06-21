"""Implementation of the merge sort algorithm. The list is sorted in ascending order."""


def merge_sort(lst: list) -> None:
    """Sorts list in ascending order using the merge sort algorithm.

    @complexity: best and worst - O(n*log(n))
    """
    if len(lst) == 0 or len(lst) == 1:
        return
    merge_sort_aux(lst, 0, len(lst) - 1)


def merge_sort_aux(lst: list, start: int, end: int) -> None:
    if start < end:
        mid = (end + start) // 2
        merge_sort_aux(lst, start, mid)
        merge_sort_aux(lst, mid + 1, end)
        merge(lst, start, mid, end)


def merge(lst: list, start: int, mid: int, end: int) -> None:
    a = start
    b = mid + 1
    merged_list = []

    while a <= mid and b <= end:
        if lst[a] < lst[b]:
            merged_list.append(lst[a])
            a += 1
        else:
            merged_list.append(lst[b])
            b += 1

    if a <= mid:
        for i in range(a, mid + 1):
            merged_list.append(lst[i])
    elif b <= end:
        for i in range(b, end + 1):
            merged_list.append(lst[i])

    for i in range(len(merged_list)):
        lst[start] = merged_list[i]
        start += 1
