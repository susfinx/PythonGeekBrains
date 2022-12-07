# # Вычислить число c заданной точностью d
# #
# # Пример:
# #
# # - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# #f'{round(math.pi,count+1)}, {count}'
# import math
#
# tochnost= (input('Vvedite Chislo'))
# count=0
# if '.' in tochnost:
#     count=len(tochnost.split('.')[1])
#
# print(round(math.pi,count))

# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

N= int(input('Vvedite Chislo '))
mnojitel=[]
prostoymnojetel=[]
for i in range(1,N+1):
    if N % i==0:
        mnojitel.append(i)
for j in mnojitel:
    for k in range(1, j+1):
        if j%k!=0:
            prostoymnojetel.append(j)
print(prostoymnojetel)

# Nikak ne mogu ponyat pochemu to po neskolko raz na pechat elementy vyhodyat..




# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

# import random
#
# Len_list= int(input('Vvedite dlinu Spiska'))
#
# mylist=[random.randint(0,10) for _ in range(Len_list)]
# print(mylist)
# mylist2=[]
# for i in mylist:
#     if mylist.count(i)==1:
#         mylist2.append(i)
# print(mylist2)














