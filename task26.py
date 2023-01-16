# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
 
a = int(input("Введите число "))
b = int(input("Введите степень в которую хотите возвести "))
def rank(digit, grade):
    if grade == 1:
        return digit
    if grade != 1:
            return (digit * rank(digit, grade - 1)) 
print(rank(a, b))
 
