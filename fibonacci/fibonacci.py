"""Three ways of finding the nth Fibonacci number""" 

def iterative_fibonacci(n: int) -> int: 
    """Finding the nth Fibonacci number using an iterative method

    @complexity: O(n)
    """
    if n < 0: 
        raise Exception("Input must be a non-negative integer")
    elif n == 0: 
        return 0 
    elif n == 1: 
        return 1 
    else: 
        a = 0 
        b = 1 
        c = a + b 
        while n > 2: 
            temp = c 
            c = b + c 
            a = b 
            b = temp 
            n -= 1  
        return c 



def recursive_fibonacci(n: int) -> int: 
    """Finding the nth Fibonacci number recursively. 

    @complexity: O(n)
    """
    if n < 0: 
        raise Exception("Input must be a non-negative integer")
    elif n == 0: 
        return 0
    elif n == 1: 
        return 1 
    else: 
        return recursive_fibonacci(n - 2) + recursive_fibonacci(n - 1)


def tail_recursive_fibonacci(n: int, N_2=0, N_1=1) -> int: 
    """Finding the nth Fibonacci number using tail recursion. 

    @complexity: O(n)
    """
    if n < 0: 
        raise Exception("Input must be a non-negative integer")
    elif n == 0: 
        return N_2
    elif n == 1: 
        return N_1 
    elif n == 2: 
        return N_1 + N_2 
    else: 
        return tail_recursive_fibonacci(n - 1, N_1, N_2 + N_1)
