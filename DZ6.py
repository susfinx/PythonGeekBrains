# ZADACHA 5
# mnojestvo_list = [1,4,5,2,3,9,8,0,15,16]
# mnojestvo_list = sorted(mnojestvo_list)
# strit=str(mnojestvo_list[0])
# for i in range(1,len(mnojestvo_list)):
#     if mnojestvo_list[i]-1>mnojestvo_list[i-1]:
#         strit+= f'-{str(mnojestvo_list[i-1])}, {(str(mnojestvo_list[i]))}'
#     if i+1 == len(mnojestvo_list):
#         strit+=f'-{str(mnojestvo_list[-1])}'
#
# print(strit)

# ZAdacha 6

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


