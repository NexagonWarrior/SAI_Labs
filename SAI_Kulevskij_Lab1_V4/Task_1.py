def calculate_area(coords):

    n = len(coords)
    area = 0

    for i in range(n):
        j = (i + 1) % n
        area += coords[i][0] * coords[j][1]
        area += coords[j][0] * coords[i][1]

    return abs(area) / 2.0

verticles = []

for i in range(4):
    while True:
        try:
            raw_input = input(f"Вершина {i + 1} (x y):")
            x, y = map(float, raw_input.split())
            verticles.append((x, y))
            break
        except ValueError:
            print(("Помилка! Будь ласка, введіть два числа, розділені пробілом."))

area = calculate_area(verticles)
print(f"\nПлоща чотирикуттника {area:.3f}")