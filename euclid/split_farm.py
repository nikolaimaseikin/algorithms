def split_farm(width: int, height: int) -> int:
    try:
        if width % height == 0:
            return height
        else:
            return split_farm(height, width % height)
    except ZeroDivisionError:
        return None


while True:
    try:
        width = int(input("Значение длины участка:\n"))
        heigth = int(input("Значение ширины участка:\n"))
        length_side_square = split_farm(width, heigth)
        print(f"Длина стороны квадрата = {length_side_square}, количество квадратов = {(width/length_side_square) * (heigth / length_side_square)}")
        break
    except TypeError:
        print("Значение длины или ширины участка не должны иметь нулевые значения")
    except KeyboardInterrupt:
        print("Программа завершена")
        exit()