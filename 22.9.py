array = [int(x) for x in input("Введите последовательность чисел через пробел: ").split()]

def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
array = merge_sort(array)

print("Список по возрастанию элементов  ", array)

element = int(input("Введите любое число. "))
if element < min(array) or element > max(array):
    print("Число не входит в диапазон списка!")
if element <= 0:
    print("Вводите целое число!")

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
I = (binary_search(array, element, 0, len(array)))
if I > element:
    iI = I
else:
    iI = I + 1
print("Позиция элемента   ", iI)