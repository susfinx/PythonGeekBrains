# 6) Напишите программу, которая принимает на вход цифру, обозначающую день 
# недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day = int(input('chislo dnya Nedeli '))
# if day>7 or day<=0:
#     print('nekoreknyi vvod')
# elif day==7 or day==6:
#     print('Eto Vyhodnoy')
# else:
#     print('NET ne vyhodnoy')

# 7) Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in [True, False]:
#     for y in [True, False]:
#         for z in [True, False]:
#             print(not(x or y or z)==(not x and not y and not z))

# 8) Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой 
# находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
             
# x= int(input('tochka x '))
# y= int(input('tochka y '))
# if x>0 and y>0:
#     print (f'tochka coordinat x= {x} i y= {y}, Nahoditsya v 1 chetverti')
# elif x>0 and y<0:
#     print (f'tochka coordinat x= {x} i y= {y}, Nahoditsya v 2 chetverti')
# elif x<0 and y<0:
#     print (f'tochka coordinat x= {x} i y= {y}, Nahoditsya v 3 chetverti')
# elif x<0 and y>0:
#     print (f'tochka coordinat x= {x} i y= {y}, Nahoditsya v 4 chetverti')             


# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

# Chetvert=int (input('vvedite nomer chetverti, ot 1 do 4 => '))
# if Chetvert <1 or Chetvert >4:
#     print ('Necoreknyi Vvod')
# elif Chetvert==1:
#     print (f'diapazon chetverty {Chetvert}, ot x>0, y>0')
# elif Chetvert==2:
#     print (f'diapazon chetverty {Chetvert}, ot x>0, y<0')
# elif Chetvert==3:
#     print (f'diapazon chetverty {Chetvert}, ot x<0, y<0')
# elif Chetvert==4:
#     print (f'diapazon chetverty {Chetvert}, ot x<0, y>0')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

xA= float(input('coordinata x tochki A => '))
yA= float(input('coordinata y tochki A => '))
xB= float(input('coordinata x tochki B => '))
yB= float(input('coordinata y tochki B => '))
import math
reshenie=(math.sqrt((xB-xA)**2+(yB-yA)**2))
print (round(reshenie,2))