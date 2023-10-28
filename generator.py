def next_cube():
    acc = 1
    while True:
        yield acc**3
        acc += 1


