#Задача: Узнать бъет ли фигуру ферзь по координатам двух фигур на шахматной доске. Ферзь бьет по горизонтали, вертикали и диагонали.
#Входные данные: координаты двух фигур на шахматной доске



from numpy import diag

# Словарь для перевода буквенных координат в числовые
horisont_coord = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}

input_queen = input("Введите координаты ферзя (например, A1, латиница): ")
input_target = input("Введите координаты целевой фигуры (например, A1, латиница):")

# Переводим координаты ферзя и целевой фигуры в числовой формат
queen_x =  horisont_coord.get(input_queen[0])
queen_y = input_queen[1]
queen_coordinat = [(queen_x,queen_y)]
target_x = horisont_coord.get(input_target[0])
target_y = input_target[1]

# Координаты целевой фигуры в числовом формате
target_coordinat = (int(target_x), int(target_y))
print(f"Координаты ферзя: {queen_coordinat}, Координаты целевой фигуры: {target_coordinat}")

# Список координат диагоналей ферзя
diagonal_coords= []


# Координаты ферзя в числовом формате
queen_x1 = int(queen_x)
queen_y1 = int(queen_y)
queen_x2 = int(queen_x)
queen_y2 = int(queen_y)
queen_x3 = int(queen_x)
queen_y3 = int(queen_y)

# Ищем самую верхнюю точку правой диагонали, по которой может двигаться ферзь
while 8 > queen_x1 >=1  and 8 > queen_y1 >= 1:
    queen_x1+=1
    queen_y1+=1

# Точка правого верхнего угла диагонали
diagonal_coords.append((queen_x1, queen_y1))
peak = diagonal_coords[0]

# Диагональ правого верхнего угла с верхнего угла до нижнего левого угла
while 8 >= peak[0] > 1 and 8 >= peak[1] > 1:
    peak = (peak[0] - 1, peak[1] - 1)
    diagonal_coords.append(peak)

# Линия справа внизу диагонали
while 8 >queen_x2>=1  and 8 >=queen_y2>= 1:
    queen_x2+=1
    queen_y2-=1
    diagonal_coords.append((queen_x2, queen_y2))

# Линия слева вверху диагонали
while 8 >queen_x3>=1  and 8 >queen_y3>= 1:
    queen_x3-=1
    queen_y3+=1
    diagonal_coords.append((queen_x3, queen_y3))
print("Координаты диагонали:")
print(diagonal_coords)


if int(queen_x) == int(target_x) or int(queen_y) == int(target_y) or target_coordinat in diagonal_coords:
    print(f"Ферзь на {input_queen} бъет фигуру на {input_target}")
else: 
    print(f"Ферзь на {input_queen} не бъет фигуру на {input_target}")

     