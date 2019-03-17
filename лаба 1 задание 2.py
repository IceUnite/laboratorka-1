from random import randrange
print("Введите левую границу")
a = int(input())
print("Введите правую границу")
b = int(input())
z = randrange(a,b)
k = int(input())
while k!=z:
    if k > z:
        print("Ваше число больше")
    else:
        print("Ваше число меньше")
    k = int(input())
print("Вы победили)")

