from random import randint

x = 10
a = []
for i in range(x): # O(N)
    a.append(randint(1, 99))
print(a)
b = len(a)

for i in range (b): # O(N)
    f = 0 
    for j in range (b-1-i): # O(N)
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            f = 1
        print(a)
    if f == 0:
        break
print(a)
 
# O(N) + O(N) * O(N) = O(N)+O(N)=O(N)  O(N)*O(N)= O(N*N) = O(N^2) 


print("-----------------------------")
print("Перевод числа из десятичного \n   в бинарное состояние")
n = int(input("Введите любое число: "))

def bin_des(n): # O(N)
    if n >= 2:
        bin_des(n//2)
    print(n % 2, end = " ")
    
    
print("Ваше число в бинарном виде: ")
bin_des(n)
print()

print("-----------------------------")

print("Сумма двух чисел")

def sum(a,b): # O(N)
    if b==0:
        return a
    return sum(a+1,b-1)
    
    
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print("Сумма ваших чисел равна:")

print(sum(a, b))
print("-----------------------------")

print("Возведение в степень")

def step(a, b): # O(N)
    if b <= 0:
        return 1
    elif b == 1:
        return a
    elif b != 1:
        return (a * step(a, b - 1))   
    
    
a = int(input("Введите любое число: "))
b = int(input("Введите степень для этого числа: "))

print("Число", a, "в степени", b, "равно:")
print(step(a, b))
print("-----------------------------")

# функции из Домашнего Задания 4 имеют такую низкую сложность (O(N)), потому что принимают в себя
# вводные данные от пользователя, а не список как в Домашнем Задании 3, при обработке списка пришлось
# дважды использовать цикл for, что привело к сложности функции O(N^2).
