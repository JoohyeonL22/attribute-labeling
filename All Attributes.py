import os
import pandas as pd
import sys
# 모든 attribute를 출력
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
        str_temp = i['attribute']
        strings = str_temp.split(', ')
        for j in range(len(strings)):
            class_name.append(strings[j])

class_name = list(set(class_name))
class_name.sort()
sys.stdout = open('stdout.txt', 'w')
for k in range(len(class_name)):
    print(class_name[k])
    print("")
sys.stdout.close()
