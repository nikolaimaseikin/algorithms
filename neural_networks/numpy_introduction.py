import numpy as np
a = np.array([0, 1, 2, 3]) #Вектор
b = np.array([4, 5, 6, 7]) #Вектор
c = np.array([[0, 1, 2, 3], [4, 5, 6, 7]]) #Матрица
d = np.zeros((2, 4)) #Матрица 2x4, заполненная нулями
e = np.random.rand(2, 5) #Матрица 2x5, заполненная случайнымм числами от 0 до 1
#print(a * e)
#print(b)
#print(c)
#print(d)
#print(e)
a = np.zeros((1, 4))
b = np.zeros((4, 3))
c = a.dot(b)
print(c.shape)