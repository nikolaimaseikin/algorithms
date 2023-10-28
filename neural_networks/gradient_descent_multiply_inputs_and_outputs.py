def neural_network(input, weights):
    prediction = vect_mat_mul(input, weights)

    return prediction

def vect_mat_mul(inputs, weights):
    output = [0 for weights_set in weights]

    for i in range(len(output)):
        output[i] = w_sum(inputs, weights[i])

    return output

def w_sum(inputs, weights):
    output_w_sum = 0
    for i in range(len(inputs)):
        output_w_sum += inputs[i] * weights[i]

    return output_w_sum

def outer_prod(input, delta):
    out = [[0 for i in range(len(delta))] for j in range(len(input))]
    for i in range(len(input)):
        for j in range(len(delta)):
            out[i][j] = input[i] * delta[j]
    
    return out

def show_matrix(matrix: list) -> None:
    for row in matrix:
        print(*row)




weights = [[0.1, 0.1, -0.3], #Травмы
            [0.1, 0.2, 0.0], #Победа
            [0.0, 1.3, 0.1]] #Печаль

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

hurt = [0.1, 0.0, 0.0, 0.1]
win = [1, 1, 0, 1]
sad = [0.1, 0.0, 0.1, 0.2]

alpha = 0.01

input = [toes[0], wlrec[0], nfans[0]]
true = [hurt[0], win[0], sad[0]]

prediction = neural_network(input, weights)

error = [0 for i in true]
delta = [0 for i in true]

for i in range(len(true)):
    error[i] = (prediction[i] - true[i]) ** 2
    delta[i] = prediction[i] - true[i]

weight_deltas = outer_prod(input, delta)
show_matrix(weight_deltas)


