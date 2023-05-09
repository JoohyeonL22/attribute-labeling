import os
import pandas as pd
import sys

attribute_list = ['airborne', 'alone', 'american', 'apple', 'arched', 'asphalt', 'baby', 'back', 'bald', 'balding', 'bare', 'barefoot', 'barren', 'baseball', 'beige', 'bending', 'bent', 'big', 'black', 'black and white', 'blond', 'blonde', 'blue', 'blurry', 'brick', 'bricked', 'bright', 'bright blue', 'brown', 'bunch', 'burgundy', 'busy', 'calm', 'cardboard', 'carpeted', 'cast', 'cement', 'ceramic', 'chain link', 'checkered', 'chocolate', 'choppy', 'chrome', 'circular', 'clay', 'clean', 'clear', 'closed', 'cloudless', 'cloudy', 'cluttered', 'coffee', 'colorful', 'computer', 'concrete', 'cooked', 'cooking', 'covered', 'cracked', 'crashing', 'crouching', 'curly', 'curved', 'cut', 'dark', 'dark blue', 'daytime', 'dead', 'decorated', 'decorative', 'denim', 'digital', 'dirt', 'dirty', 'distant', 'docked', 'double decker', 'dried', 'driving', 'dry', 'eating', 'electric', 'electrical', 'empty', 'evergreen', 'extended', 'fallen', 'fire', 'flat', 'flat screen', 'floral', 'fluffy', 'flying', 'foamy', 'framed', 'fried', 'frosted', 'full', 'furry', 'glass', 'glazed', 'glowing', 'gold', 'golden', 'grass', 'grassy', 'gravel', 'gray', 'grazing', 'green', 'growing', 'hairy', 'hanging', 'hardwood', 'hazy', 'holding', 'huge', 'in air', 'iron', 'jumping', 'khaki', 'kneeling', 'laptop', 'large', 'laying', 'leafless', 'leafy', 'leaning', 'leather', 'license', 'light blue', 'lit', 'little', 'long', 'long sleeved', 'looking', 'lush', 'lying', 'made', 'male', 'marble', 'maroon', 'metal', 'metallic', 'moving', 'muddy', 'multi colored', 'murky', 'neon', 'octagonal', 'off', 'old', 'older', 'open', 'opened', 'orange', 'ornate', 'outstretched', 'overcast', 'overhead', 'painted', 'palm', 'paper', 'parked', 'parking', 'patterned', 'paved', 'performing', 'pile', 'piled', 'pine', 'pink', 'plaid', 'plastic', 'playing', 'playing tennis', 'pointed', 'pointing', 'pointy', 'polar', 'porcelain', 'posing', 'potted', 'power', 'puffy', 'purple', 'railroad', 'rainbow colored', 'raised', 'red', 'reflecting', 'reflective', 'resting', 'riding', 'ripe', 'rock', 'rocky', 'roll', 'rolled', 'rough', 'round', 'rubber', 'running', 'rusted', 'rusty', 'sand', 'sandy', 'sharp', 'sheer', 'shining', 'shiny', 'shirtless', 'short', 'short sleeved', 'silver', 'sitting', 'skateboarding', 'skating', 'ski', 'skiing', 'sleeping', 'slice', 'sliced', 'small', 'smiling', 'snow-covered', 'snowboarding', 'snowy', 'splashing', 'square', 'squatting', 'stacked', 'stainless steel', 'standing', 'steel', 'stone', 'stop', 'straw', 'street', 'striped', 'stuffed', 'surfing', 'swimming', 'swinging', 'talking', 'tall', 'tan', 'teal', 'tennis', 'thick', 'thin', 'tile', 'tiled', 'toilet', 'traffic', 'train', 'up', 'walking', 'watching', 'water', 'waving', 'wearing', 'wet', 'white', 'wicker', 'wii', 'wine', 'wire', 'wispy', 'wood', 'wooden', 'woven', 'wrinkled', 'written', 'yellow', 'young']

#새로 들어온 파일
csv_path = 'C:/Attribute_Detection/07/2_Attribute/'
file_list = os.listdir(csv_path)
file_list_csv = [file for file in file_list if file.endswith('.csv')] ## 파일명 끝이 .csv인 경우

for k in range(len(file_list_csv)):
    file_list_csv[k] = file_list_csv[k][:-3]
    
attribute_name = []

for m in range(len(file_list_csv)):
    name = file_list_csv[m]
    #엑셀 파일 위치
    csv = csv_path + name + 'csv'
    df = pd.read_csv(csv, index_col = 0)
    for i in df.iloc:
        str_temp = i['attribute']
        strings = str_temp.split(', ')
        for j in range(len(strings)):
            attribute_name.append(strings[j])

attribute_name = list(set(attribute_name))
attribute_name.sort()
#print(class_name)


#1. 새로 추가된 class 확인
for i in range(len(attribute_name)):
    if attribute_name[i] not in attribute_list:
        print(attribute_name[i])


"""
#2. 새로 적용할 전체 class 리스트
all_list =[]

for i in range(len(attribute_list)):
    all_list.append(attribute_list[i])

for i in range(len(attribute_name)):
    all_list.append(attribute_name[i])

all_list = list(set(all_list))
all_list.sort()
print(all_list)
"""
