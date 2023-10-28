def elementwise_multiplication(a: list, b: list) -> list:
    output_list = []
    if len(a) == len(b):
        for i in range(len(a)):
            output_list.append(a[i] * b[i])
        return output_list
    else:
        return None

def elementwise_addition(a: list, b: list) -> list:
    output_list = []
    if len(a) == len(b):
        for i in range(len(a)):
            output_list.append(a[i] + b[i])
        return output_list
    else:
        return None

def vector_sum(a: list) -> float:
    sum = 0
    for element in a:
        sum += element
    return sum

def vector_average(a: list) -> float:
    sum = 0
    for element in a:
        sum += element
    average = sum / len(a)
    return average




a = [1, 2, 3]
b = [3, 4, 5]
print(elementwise_multiplication(a, b))
print(elementwise_addition(a, b))
print(vector_sum(elementwise_multiplication(a, b)))