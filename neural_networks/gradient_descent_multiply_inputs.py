def neural_network(input, weights):
    prediction = w_sum(input, weights)
    return prediction

def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output

def learning_iteration(weights, weights_deltas):
    alpha = 0.01
    output = [0 for i in range(len(weights))]
    for i in range(len(output)):
        output[i] = weights[i] - (weight_deltas[i] * alpha)
    return output

def ele_mul(number, vector):
    output = [0 for i in range(len(vector))]
    for i in range(len(vector)):
        output[i] = number * vector[i]
    return output


weights = [0.1, 0.2, -0.1]
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]
win_or_lose_binary = [1, 1, 0 ,1]
true = win_or_lose_binary[0]
input = [toes[0], wlrec[0], nfans[0]]
for i in range(3):
    print(f'Итерация {i}')
    prediction = neural_network(input, weights)
    error = (prediction - true) ** 2 
    delta = prediction - true
    weight_deltas = ele_mul(delta, input)
    print(f'До обучения {weights}')
    weights = learning_iteration(weights, weight_deltas)
    print(f'После обучения {weights}')


