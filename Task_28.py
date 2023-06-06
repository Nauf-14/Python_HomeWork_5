# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1
# Также нельзя использовать циклы.
# 2 2 -> 4

def sum(first_numb, sec_numb):
    if first_numb == 0:
        return sec_numb
    return sum(first_numb-1, sec_numb+1)    
    

print(sum(int(input('Введите 1-е число (first_numb): ')), int(input('Введите 2-е число (sec_numb): '))))