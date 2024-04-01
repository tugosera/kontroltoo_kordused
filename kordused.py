﻿#1
try:
   i=int(input("sisesta sõnaseadjate arv (1-9) ")) 
except:
   ValueError
if 0>i>9:
   print("error")
else:
   for i in range (0,i,1):
       print("  -----  \n |  O  |  \n !  -  !  \n  -----  \n")

#2


stepen = int(input("Введите показатель степени: "))
n = int(input("Введите число n: "))

max_chislo = int(n ** 3)
for i in range(1, max_chislo + 1):
    result = i ** stepen
    if result <= n ** 3:
        print(f"{i}^{stepen} = {result}")

#3

from math import *
from random import *

ocenki=randint(1,5)
ucheniki=randint(1,30)
sum_ocenki=0
print("всего учеников - ",ucheniki)
for i in range(ucheniki):
    ocenka=randint(1,5)
    sum_ocenki+=ocenka
srednee=sum_ocenki/ucheniki   
print("Средний балл в классе cосставляет - ",srednee)

#4

vozrast=1
denga=1
while denga<=100:
    denga+=vozrast
    vozrast+=1
    print(f"В возрасте {vozrast} лет, подарок составляет {denga} долларов")

#5

spisok=[0, 1]
kolichestvo=int(input("Ведите количество чисел в ряде Фибоначчи"))
for i in range(2, kolichestvo):
    next_chislo=spisok[-1]+spisok[-2]
    spisok.append(next_chislo)
for a in spisok:
    print(a)
