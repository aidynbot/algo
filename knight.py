# Узнать бъет ли конь фигуру на заданной позиции

horisont_coords = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}

knight_raw_coor = input("Введите координату коня")
figure_raw_coor = input("Введите координату фигуры")


knight_x = int(horisont_coords.get(knight_raw_coor[0], 0))
knight_y = int(knight_raw_coor[1])

figure_x = int(horisont_coords.get(figure_raw_coor[0],0))
figure_y = int(figure_raw_coor[1])

if abs(knight_x - figure_x) == 2 and abs(knight_y - figure_y) == 1 or abs(knight_x - figure_x) == 1 and abs(knight_y - figure_y) == 2:
    print(f"Конь на {knight_raw_coor} бъет фигуру на {figure_raw_coor}")
else:
    print(f"Конь на {knight_raw_coor} не бъет фигуру на {figure_raw_coor}")