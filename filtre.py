'''import math

def is_even(x):


   return x % 2 == 0

given = [1.0, float('nan'), 2.0, float('nan'), 3.0]

def is_not_nan(value):
   return not math.isnan(value)


returns = filter(is_not_nan, given)



elements = [1, 2, 3, 4, 5, 6]
numbers = [-3, -2, -1, 0, 1, 2, 3]


built = filter(is_even, elements)
filtered_numbers = filter(lambda x: x > 0, numbers)

print(list(filtered_numbers))
print(built)
print(list(returns)) '''

# импортируем reduce
from functools import reduce

# создаём список натуральных чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# фильтруем чётные числа
filtered_numbers = filter(lambda x: x % 2 == 0, numbers)

# удваиваем каждое отфильтрованное число
doubled_numbers = map(lambda x: x * 2, filtered_numbers)

# суммируем все удвоенные числа
sum_of_numbers = reduce(lambda x, y: x + y, doubled_numbers)

# выводим результат
print(sum_of_numbers)