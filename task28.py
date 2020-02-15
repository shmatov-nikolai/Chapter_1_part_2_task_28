'''
Напишите функцию где дан список целых чисел. Заменить отрицательные на -1,
положительные - на число 1, ноль оставить без изменений.
'''

def null_one_list(some_list):
    i=0
    while i < len(some_list):
        if some_list[i] > 0:
            some_list[i] = 1
            i+=1
        elif some_list[i] < 0:
            some_list[i] = -1
            i+=1
        elif some_list[i] == 0:
            i+=1
    print(some_list)
    
spisok = [1, 2, -3, 4, -5, 8, 9, -6, 11, -25, 15, 32, 0, 0, 14]
null_one_list(spisok)    
