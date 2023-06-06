# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

base_degree = int(input("Введите основание степени (base_degree): "))
degree_indicator = int(input("Введите показатель степени (degree_indicator): "))


def power(base_degree, degree_indicator):
    if degree_indicator < 0:
        return (1 / base_degree)*power(base_degree, degree_indicator + 1)
    if degree_indicator > 0:
        return base_degree * power(base_degree, degree_indicator - 1)
    else:
        return 1


print(f"Число {base_degree} в степени {degree_indicator} равно: {power(base_degree, degree_indicator)}")
