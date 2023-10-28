input  = 2
target_prediction = 0.8
weight = 0.5
alpha = 0.1

for i in range(20):
    current_prediction = input * weight
    error = (current_prediction - target_prediction) ** 2 #Среднее квадратическое отклонение
    derivative = (current_prediction - target_prediction) * input
    weight -= (derivative * alpha)
    print(f'Iteration: {i}\nCurrent prediction = {current_prediction}\nError = {error}')

