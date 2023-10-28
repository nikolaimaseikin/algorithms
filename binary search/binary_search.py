def binary_search(target_element: int, collection: list) -> int:
    mid = len(collection) // 2
    if len(collection) == 1:
        if collection[mid] == target_element:
            return mid
        else:
            return None
    elif collection[mid] == target_element:
        return mid
    else:
        if target_element < collection[mid]:
            return binary_search(target_element, collection[:mid])
        else:
            try:
                return mid + binary_search(target_element, collection[mid:])
            except TypeError:
                return None
         

