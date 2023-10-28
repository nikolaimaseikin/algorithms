weight = 0.5
input = 0.5
goal_prediction = 0.8

step_amount = 0.2

for iteration in range(1101):
    prediction = input * weight
    error = (prediction - goal_prediction) ** 2
    
    print(f"Error = {error};\n Prediction = {prediction}")

    up_prediction = input * (weight + step_amount)
    up_error = (up_prediction - goal_prediction) ** 2
 
    down_prediction = input * (weight - step_amount)
    down_error = (up_prediction - goal_prediction) ** 2
  
    if up_error <= down_error:
        weight += step_amount
    if down_error < up_error:
         weight -= step_amount

        


    




