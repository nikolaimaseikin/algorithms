def fibonacci_memoized(n: int) -> int:
    memory = [] 
    for i in range(n):
        if i == 0:
            memory.append(0)
        elif i == 1:
            memory.append(1)
        else:
            memory.append(memory[i-1] + memory[i-2])
    return memory[-1]


print(fibonacci_memoized(100))

    
    







