#   1)	Напишите функцию, которая принимает список элементов и число, а возвращает список элементов,
#   умноженных на это число. Укажите типизацию в функции.
#   Функция необязательно будет принимать множитель, в этом случае выдайте список элементов, умноженный на 2.
#   2)	Напишите лямбда функцию с аналогичным функционалом.


from typing import List, Union

def multiply_list(items: List[Union[int, float]], multiplier: Union[int, float] = 2) -> List[Union[int, float]]:
    doubled = []
    for item in items:
        doubled.append(item * multiplier)
    return doubled

data = [1, 2, 3, 4, 5]
d_data = multiply_list(data)
print(f"double list: {d_data}")

multiply_lambda = lambda items: [item * 2 for item in items] # lambda items: multiply_list(items)


double = multiply_lambda(data)
print(f"double list (лямбда): {double}")
