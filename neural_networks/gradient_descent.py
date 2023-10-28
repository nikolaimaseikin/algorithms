weight = 0.5
goal_prediction = 0.8
input = 2
alpha = 0.1

for iteration in range(20):
    prediction = input * weight
    error = (prediction - goal_prediction) ** 2
    direction_and_amount = (prediction - goal_prediction) * input
    weight -= direction_and_amount * alpha
    print(f"prediction = {prediction};\n error = {error}")
