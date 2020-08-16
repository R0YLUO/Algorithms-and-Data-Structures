from counting_sort import counting_sort_tuples

def radix_sort(lst: list) -> list: 
    """Sorts a list of integers into ascending order using radix sort algorithm
    
    @complexity: O(kN) where N is the size of the list and k is the greatest number of digits. 
    This is derived from O((N+U)*k), where we are performing counting sort k amount of times since
    we are sorting by each digit. But U in this case is 10, since we are considering integers of 
    base 10. 
    """ 
    digits = get_number_of_digits(get_max(lst)) 
    tuple_list = [] 
    for item in lst: 
        tuple_list.append((None, convert_to_string_with_n_digits(item, digits)))
    for digit_position in range(digits -1, -1, -1): 
        for i in range(len(tuple_list)): 
            tuple_list[i] = (int(tuple_list[i][1][digit_position]), tuple_list[i][1])
        tuple_list = counting_sort_tuples(tuple_list)
    sorted_list = [] 
    for item in tuple_list: 
        sorted_list.append(int(item[1]))
    return sorted_list


def get_max(lst: list) -> int: 
    """returns maximum value in a list""" 
    max = lst[0] 
    for item in lst: 
        if item > max: 
            max = item 
    return max 

def get_number_of_digits(n: int) -> int: 
    """returns the number of digits in a number""" 
    digit_count = 0 
    while n != 0: 
        n //= 10 
        digit_count += 1 
    return digit_count 

def convert_to_string_with_n_digits(x: int, digits: int) -> str: 
    """converts a number to a string of the specified amount of digits. 

    for example, if number of digits is 4, and our number is 21, this gets converted to 0021 as a string
    """ 
    output = str(x) 
    while len(output) != digits: 
        output = '0' + output 
    return output

print(radix_sort([123,231,26,234,231,41,15,9,10]))