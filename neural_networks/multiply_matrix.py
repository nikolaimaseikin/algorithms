from re import T
from xml.dom.minidom import Element
from numpy import matrix

def verify_matrix(a: list, b: list) -> bool:
    number_of_columns = 0
    number_of_strings = len(b)
    if type(a[0]) == list:
        number_of_columns = len(a[0])
    elif type(a[0]) == int:
        number_of_columns = len(a)
    else:
        print(1)
        return False
    if type(b[0]) == list:
        number_of_strings = len(b)
    elif type(b[0]) == int:
        number_of_strings = 1
    else:
        print(2)
        return False
    if number_of_columns == number_of_strings:
        return True
    else:
        return False

    
    
    
    
    
    
    
    if number_of_columns == number_of_strings:
        return True
    else:
        return False

def multiply_matrix(a: list, b: list) -> list:
    element = []
    w_sum = 0
    output_matrix = []
    for i in range(len(a)):
        for k in range(len(b[0])):
            for j in range(len(a[0])):
                w_sum += a[i][j] * b[j][k]
            element.append(w_sum)
            w_sum = 0
        output_matrix.append(element)
        element = []
        
    return output_matrix

a = [[1, 2, 3], [4, 5, 6]]
b = [[1, 2], [3, 4], [5, 6]]

print(multiply_matrix(a, b))
        
            
               
            
            

    
        

    