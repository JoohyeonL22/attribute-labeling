import os
import pandas as pd
import sys

#작업마다 csv_path, jpg_path만 바꿔주면 됨
#엑셀 파일이 들어있는 폴더
csv_path = 'C:/Attribute_Detection/07/2_Attribute/'
file_list = os.listdir(csv_path)
file_list_csv = [file for file in file_list if file.endswith('.csv')] ## 파일명 끝이 .csv인 경우

for k in range(len(file_list_csv)):
    file_list_csv[k] = file_list_csv[k][:-3]
    
class_name = []

for m in range(len(file_list_csv)):
    name = file_list_csv[m]
    #엑셀 파일 위치
    csv = csv_path + name + 'csv'
    df = pd.read_csv(csv, index_col = 0)
    for i in df.iloc:
        class_name.append(i['class'])

class_name = list(set(class_name))
class_name.sort()

#class의 개수만큼 길이를 가지는 2차원 배열 att_list 생성
att_list= []
for i in range(len(class_name)):
    temp_list = []
    for j in range(1):
        temp_list.append(0)
    att_list.append(temp_list)

for m in range(len(file_list_csv)):
    name = file_list_csv[m]
    #엑셀 파일 위치
    csv = csv_path + name + 'csv'
    df = pd.read_csv(csv, index_col = 0)
    
    for i in df.iloc:
        str_temp = i['attribute_refine']
        if type(str_temp) is float:
            continue
        strings = str_temp.split(', ')
        for j in range(len(class_name)):
            if class_name[j] == i['class']:
                for k in range(len(strings)):
                    att_list[j].append(strings[k])
                
for j in range(len(att_list)):
    del att_list[j][0]
    att_list[j] = list(set(att_list[j]))

for m in range(len(file_list_csv)):
    name = file_list_csv[m]
    #엑셀 파일 위치
    csv = csv_path + name + 'csv'
    df = pd.read_csv(csv, index_col = 0)
    
    for i in df.iloc:
        str_temp = i['attribute_refine']
        if type(str_temp) is float:
            print(i['class'])
            continue
        strings = str_temp.split(', ')
        for j in range(len(class_name)):
            if class_name[j] == i['class']:
                for k in range(len(strings)):
                    for v in att_list[j][:]:
                        if v not in strings[k]:
                            att_list[j].remove(v)

#print(att_list)

#sys.stdout = open('stdout.txt', 'w')
for k in range(len(class_name)):
    #print("\'" + class_name[k] + "\'",end = " : ")
    print("\'" + class_name[k] + "\' : ", end = "")
    print(att_list[k], end =", \n")
    print("")
#sys.stdout.close()

