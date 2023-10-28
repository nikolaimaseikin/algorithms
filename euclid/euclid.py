def euclid(a:int, b:int)->int:
    if b == 0:
        return a
    return euclid(b, a%b)

print(euclid(1680, 640))
