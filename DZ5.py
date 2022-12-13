
# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
#
# my_text = 'abvgteksb, rtegdjsha, dhfjgbnmxg, ooeoia, rtiop, rats'
# my_text_list = list(filter(lambda i:'a'not in i and 'b' not in i and 'v' not in i, my_text.split()))
# print(my_text_list)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# def compress (file):
#     with open (file, 'r') as file:
#         same_str=file.readline()
#         count=1
#         i=0
#         compress_str=''
#         while i< len(same_str)-1:
#             if same_str[i]==same_str[i+1]:
#                 count+=1
#             else:
#                 if count == 1:
#                     compress_str +=same_str[i]
#                 else:
#
#                     compress_str+=str(count)+same_str[i]
#                 count=1
#             i+=1
#         return compress_str
#
#
# compress=compress('Dz5.txt')
#
# def decompress (compress):
#     decompress_str=''
#     for i in range(1,len(compress)):
#         if compress[i-1].isdigit():
#             decompress_str+=(int(compress[i-1])*compress[i])
#         else:
#             if compress[i].isdigit():
#                 i+=1
#             else:
#                 decompress_str += compress[i]
#     return decompress_str
#
# decompress=decompress(compress)
# print (compress)
# print (decompress)

# Создайте программу для игры в ""Крестики-нолики"".


def draw_board(board):
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")

def inpute(board,igrok):
   valid=False
   while not valid:
      ansver=int(input(f'Vvedite nomer kletki dlya {igrok}=> '))
      if ansver >0 and ansver <10:
         if (str(board[ansver-1])) not in 'XO':
            board[ansver-1]= igrok
            valid=True
         else:
            print('Kletka Zanyata')
      else:
         print('Nekoreknyi VVod')

def Pobeda (board):
   win=False

   for i in board:
      if ('X'== board [0] and 'X'== board [1] and 'X'== board [2]) or ('X'== board[3] and 'X'== board [4] and 'X'== board [5]) or ('X'== board[6] and 'X'== board [7] and 'X'== board [8]) or ('X'== board[0] and 'X'== board [3] and 'X'== board [6]) or ('X'== board[1] and 'X'== board [4] and 'X'== board [7]) or ('X'== board[2] and 'X'== board [5] and 'X'== board [8]) or ('X'== board[0] and 'X'== board [4] and 'X'== board [8]) or ('X'== board[6] and 'X'== board [4] and 'X'== board [6]):
         print ('Pobeda X')
         print(draw_board(board))
         win=True
         break
      if ('O'== board [0] and 'O'== board [1] and 'O'== board [2]) or ('O'== board[3] and 'O'== board [4] and 'O'== board [5]) or ('O'== board[6] and 'O'== board [7] and 'O'== board [8]) or ('O'== board[0] and 'O'== board [3] and 'O'== board [6]) or ('O'== board[1] and 'O'== board [4] and 'O'== board [7]) or ('O'== board[2] and 'O'== board [5] and 'O'== board [8]) or ('O'== board[0] and 'O'== board [4] and 'O'== board [8]) or ('O'== board[6] and 'O'== board [4] and 'O'== board [6]):
         print ('Pobeda O')
         print(draw_board(board))
         win = True
         break
   return win

board = list(range(1,10))
igrok='O'
while not Pobeda(board):
   draw_board(board)
   inpute(board, igrok)
   Pobeda(board)
   if igrok=='O':
      igrok='X'
   else:
      igrok = 'O'
