# Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

from random import randint
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        raise ValueError(
            'Некорректный массив')
    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1):
            if (arr[j] < arr[j + 1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


lst = [randint(0, 100) for i in range(7)]
print(lst)
print(bubble_sort(lst))
