from math import ceil, sqrt

from typing import Union, List

def __check_is_prime(n:int):
    if n < 2:
        return False
    elif n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, ceil(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    
    return True

def is_prime(n:Union[int, List[int]]):
    if type(n) is list:
        return [__check_is_prime(x) for x in n if type(x) is int]
    elif type(n) is int:
        return __check_is_prime(n)
    else:
        raise TypeError