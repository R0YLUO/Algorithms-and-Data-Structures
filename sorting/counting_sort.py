"""Stable counting sort algorithms""" 

def counting_sort(lst: list) -> list: 
    """Sorts a given list of positive integers into ascending order
    
    @complexity: O(N+U), where N is length of list, and U is size of largest value
    """
    if not check_all_integers(lst) or not check_positive_inputs(lst): 
        raise Exception("List elements must be positive integers")
    n = len(lst) 
    largest_value = find_max(lst)
    sorted_list = [None]*n
    count_list = [0]*largest_value 
    position_list = [0]*largest_value
    # setting up count_list
    for item in lst: 
        index = item - 1
        count_list[index] += 1 
    # setting up position_list 
    for i in range(1, len(position_list)): 
        position_list[i] = count_list[i - 1] + position_list[i - 1]
    # inserting to output 
    for item in lst: 
        index = item - 1 
        sorted_list[position_list[index]] = item 
        position_list[index] += 1 
    return sorted_list


def find_max(lst: list) -> int: 
    if len(lst) == 0: 
        raise Exception("List is empty")
    max = lst[0] 
    for item in lst: 
        if item > max: 
            max = item
    return max

def check_positive_inputs(lst: list) -> bool: 
    """Checks for any non-positive numbers in a list"""
    for item in lst: 
        if item <= 0: 
            return False 
    return True

def check_all_integers(lst: list) -> bool: 
    """Checks if list is a list of integers""" 
    for item in lst: 
        if not isinstance(item, int): 
            return False 
    return True

def counting_sort_tuples(lst: list) -> list: 
    """Sorts a list of tuples, where the first item represents the sorting value, into ascending order.

    @complexity: O(N+U), where N is length of list, and U is size of largest value
    """
    n = len(lst) 
    largest_value = find_max_tuple(lst) 
    sorted_list = [None]*n 
    count_list = [0]*largest_value
    position_list = [0]*largest_value
    # setting up count_list 
    for item in lst: 
        index = item[0] - 1 
        count_list[index] += 1 
    # setting up position_list 
    for i in range(1, len(position_list)): 
        position_list[i] = position_list[i - 1] + count_list[i - 1]
    # inserting to output list 
    for item in lst:
        index = item[0] - 1 
        sorted_list[position_list[index]] = item
        position_list[index] += 1
    return sorted_list


def find_max_tuple(lst: list) -> int:  
    """finds biggest sorting value in tuple (assuming sorting value is first item of tuple""" 
    max = lst[0][0] 
    for item in lst: 
        if item[0] > max: 
            max = item[0]
    return max 

def check_valid_tuple_list(lst: list) -> bool: 
    """checks that tuples in list are valid: the sorting values (first item in typle) are positive integers""" 
    for item in lst: 
        if not isinstance(item[0], int) or item[0] <= 0: 
            return False 
    return True
