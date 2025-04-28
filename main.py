# Списки та кортежі #
# 1
seq = input("Enter numbers separated by spaces: ")
lst = list(map(int, seq.split()))
new_lst = lst[-2:] + lst[:-2]
print("Modified list:", new_lst)

# 2
languages = input("Enter languages separated by spaces: ").split()
languages.sort()
print(' '.join(languages))

# 3
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
even_index_elements = numbers[::2]
print(' '.join(map(str, even_index_elements)))

# 4
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_numbers = [num for num in numbers if numbers.count(num) == 1]
print(' '.join(map(str, unique_numbers)))

# 5
numbers = list(map(int, input().split()))
for i, num in enumerate(numbers):
    print(i, num)

# 6
filename = input().split('.')[-1]
print(filename)

# 7
numbers = tuple(map(int, input().split(', ')))
print(list(numbers))
print(numbers)

# 8
from functools import reduce
numbers = list(map(int, input().split()))
product = reduce(lambda x, y: x * y, numbers)
print(product)

# 9
binary_numbers = input().split(',')
divisible_by_5 = [num for num in binary_numbers if int(num, 2) % 5 == 0]
print(','.join(divisible_by_5))

# 10
day, month, year = input().split(', ')
print(f"{day}/{month}/{year}")

# 11
grades = input().split()
total_students = len(grades)
a_grades = grades.count('A')
print(f"{a_grades / total_students:.2f}")

# 12) Заміна пропусків на підкреслення
print('_'.join(input().split()))

# 13) Видалення кожного третього елемента
lst = list(map(int, input().split()))
idx = 0
while lst:
    idx = (idx + 2) % len(lst)
    lst.pop(idx)
    print(lst)

# 14) Створення шахової дошки
n, m = map(int, input().split())
for i in range(n):
    row = ''
    for j in range(m):
        row += '. ' if (i + j) % 2 == 0 else '* '
    print(row.rstrip())

# 15) Шифр Цезаря для смайликів
shift = int(input())
text = input()
start, end = 0x1F600, 0x1F64F
size = end - start + 1
result = ''
for ch in text:
    code = ord(ch)
    if start <= code <= end:
        code = start + (code - start + shift) % size
    result += chr(code)
print(result)

# 16) Створення 3D масиву
a, b, c = map(int, input().split())
array = [[[0 for _ in range(c)] for _ in range(b)] for _ in range(a)]
print(array)

# 17) Перевірка на анаграму
word1 = input().replace('-', '').lower()
word2 = input().replace('-', '').lower()
print(sorted(word1) == sorted(word2))