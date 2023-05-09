import os
import pandas as pd

#path folder 것들의 [, ], '를 없애 target_folder에 새로 저
path = 'C:/Attribute_Detection/07/1_CSV/' #불러올 폴더
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith('.csv')] ## 파일명 끝이 .csv인 경우

for i in range(len(file_list_py)):
    num = file_list_py[i]
    name = path + num
    df = pd.read_csv(name, index_col = 0)
    #df.reset_index()

    df['attribute'] = df['attribute'].str.replace('[', '')
    df['attribute'] = df['attribute'].str.replace(']', '')
    df['attribute'] = df['attribute'].str.replace('\'', '')
    df['attribute_refine'] = df['attribute']
    
    #저장할 폴더
    target_folder = 'C:/Attribute_Detection/07/2_Attribute/' 
    target = target_folder + num
    
    df.to_csv(target)