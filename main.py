array = []
print("Введите 3 числа")
while len(array) < 3:
    array.append(input())
print(max(array) + " - Максимальное число.")
