# Написать точно такую же процедуру, но в декларативном стиле

from random import randint
from typing import List


def sort_array(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        raise ValueError(
            'Некорректный массив')
    return sorted(arr, reverse=True)


lst = [randint(0, 100) for i in range(7)]
print(lst)
print(sort_array(lst))
