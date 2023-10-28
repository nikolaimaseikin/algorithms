def w_sum(a: list, b: list) -> float:
    output = 0.0
    if len(a) == len(b):
        for i in range(len(a)):
            output += a[i] * b[i]
        return output


#Веса выходных функций 
weights = [[0.1, 0.1, -0.3], #Травмы
            [0.1, 0.2, 0.0], #Победа
            [0.0, 1.3, 0.1]] #Печаль

#Набор исходных данных
toes = [8.5, 9.5, 9.9, 9.0] #Текущее среднее число игр
wlrec = [0.65, 0.8, 0.8, 0.9] #Процент побед
nfans = [1.2, 1.3, 0.5, 1.0] #Число болельщиков (млн)

for i in range(len(toes)):
    input = [toes[i], wlrec[i], nfans[i]]
    output = []
    for w_set in weights:
        output.append(w_sum(input, w_set))
    print(output)
    output = []



