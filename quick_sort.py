import random


def quick_sort(data: list) -> list:
    largest_elements = []
    smallest_elements = []
    if len(data) <= 1:
        return data
    else:
        base_element = data[len(data) // 2]
        for element in data:
            if element < base_element:
                smallest_elements.append(element)
            elif element > base_element:
                largest_elements.append(element)
        return quick_sort(smallest_elements) + [base_element] + quick_sort(largest_elements)


data = [random.randint(1, 100) for i in range(30)]
print(data)
print(quick_sort(data))


