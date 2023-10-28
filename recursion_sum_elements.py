def recursion_sum_elements (elements: list) -> int:
    if len(elements) == 1: 
        return elements[0]
    else:
        return elements[0] + recursion_sum_elements(elements[1:])
