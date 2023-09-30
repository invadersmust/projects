def greet():
    print("-----------------------")
    print("  Приветствую в игре,")
    print("Крестики и Нолики (X&O)")
    print("-----------------------")
    print("формат ввода:x y")
    print("x - номер строки")
    print("y - номер столбца")

def show():
    print(f"  0_1_2")
    for i in range(3):
        info = " ".join(field[i])
        print(f"{i} {info}")

def ask():
    while True:
        cord = input("      Ваш ход: ").split()

        if len(cord) != 2:
            print("Необходимо ввести 2 координаты! ")
            continue

        x, y = cord

        if not (x.isdigit()) and (y.isdigit()):
            print(" Введите число! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Данные вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Ячейка занята! ")
            continue

        return x, y

def check_win():
    cord_win = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in cord_win:
        symbols = []

        for c in cord:
            symbols.append(field[c[0]][c[1]])

        if symbols == ["X", "X", "X"]:
            print("Выиграли Крестик!!!")
            return True

        if symbols == ["O", "O", "O"]:
            print("Выиграли Нолики!!!")
            return True
    return False

greet()

field = [[" "] * 3 for i in range(3)]

numb = 0

while True:
    numb += 1

    show()

    if numb % 2 == 1:
        print(" Ход крестика")
    else:
        print(" Ход нолика")

    x, y = ask()

    if numb % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if check_win():
        break

    if numb == 9:
        print("Ничья!!! ")
        break