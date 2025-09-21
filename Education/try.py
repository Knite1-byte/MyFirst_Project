# x = 0
# while x == 0:
#     try:
#         x = int(input("Введите число: "))
#         x += 5
#     except ValueError:
#         print("Введите  число!!!")

try:
    x = 5 / 0
    x = int(input())
except ZeroDivisionError:
    print("Деление на ноль!")
except ValueError:
    print("не так ввели")
else:
    print("else")
finally:
    print("Finily")