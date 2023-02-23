n = int(input("Введите число для которого хотите получить факториал: "))
x = 1
for i in range(2, n+1):
    x *= i
print(x)