import os
import pandas as pd
import cv2
import matplotlib.pyplot as plt
#list를 string으로 변환
def listToString(str_list):
    result = ""
    for s in str_list:
        result += s + ", "
    result = result[:-2]
    return result.strip()

def Click_Mouse(event, x, y, flags, param):
    global mouse_cnt
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_cnt = 1
    if event == cv2.EVENT_RBUTTONDOWN:
        mouse_cnt = 0

#작업마다 csv_path, jpg_path만 바꿔주면 됨
#엑셀 파일이 들어있는 폴더
csv_path = 'C:/Attribute_Detection/07/2_Attribute/' #볼러올 폴더 : csv 
file_list = os.listdir(csv_path)
file_list_csv = [file for file in file_list if file.endswith('.csv')] ## 파일명 끝이 .csv인 경우

for k in range(len(file_list_csv)):
    file_list_csv[k] = file_list_csv[k][:-3]


#remove_att = ['on', 'on top of', 'on a', 'sitting on', 'on side of', 'are on', 'attached to', 'standing on', 'walking on', 'laying on', 'has', 'has a', 'have', 'in', 'in a', 'inside', 'standing in', 'are in', 'inside of', 'sitting in', 'wearing', 'wears', 'wearing a', 'is wearing a', 'behind', 'behind a', 'is behind', 'are behind', 'behind an', 'holding', 'carrying', 'carrying a', 'carrying an', 'are carrying', 'holds', 'holding an', 'holds a', 'holding on to', 'holding onto a', 'near', 'next to', 'by', 'at', 'around', 'beside', 'below', 'under', 'above', 'over', 'hanging over', 'hanging above', 'in front of', 'in front of a', 'in front', 'riding', 'riding a', 'riding on', 'is riding', 'riding in', 'hanging on', 'hanging from', 'hanging off', 'hanging in', 'hanging on a', 'are hanging on', 'eating', 'eating a', 'are eating', 'eats', 'grazing', 'grazing on', 'against', 'leaning on', 'leaning against', 'leaning on a', 'leaning against a', 'looking at', 'watching', 'are watching', 'looking at', 'looking in', 'left of', 'to left of', 'left', 'on left side of', 'on left of', 'right of', 'to right of', 'right', 'on right side of', 'on right of', 'made of', 'made from', 'made with', 'made out of', 'are made of', 'drinking', 'drinking from', 'drinks', 'drinking out of', 'drinks from', 'drink', 'drinking a', 'drink from', 'swimming in', 'swimming', 'swims in']

att_dict = {
'airplane' : ['cloudy', 'concrete', 'small'], 
'ax' : ['baseball'], 
'baby' : ['long', 'metal', 'wood', 'wooden'], 
'back pack' : ['young'], 
'bag' : ['parked', 'resting', 'sitting', 'sleeping', 'standing'], 
'bamboo' : ['calm'], 
'banner' : ['sitting', 'standing'], 
'bed' : ['sitting', 'sleeping'], 
'bicycle' : ['riding'], 
'billboard' : ['parked', 'tall'], 
'bin' : ['parked'], 
'blanket' : ['cooked', 'laying', 'sleeping'], 
'blood' : ['orange', 'white', 'blue'], 
'boat' : ['cement', 'concrete', 'driving', 'flying', 'leather', 'looking', 'paved', 'sitting', 'smiling', 'standing', 'stone', 'swimming', 'walking', 'watching'], 
'bottle' : ['paper', 'parked', 'sitting', 'stone', 'tall', 'wii'], 
'bowl' : ['paper', 'shiny'], 
'box' : ['cement', 'computer', 'concrete', 'parked', 'sitting', 'standing', 'straw', 'tall'], 
'boy' : ['old', 'wooden'], 
'branch' : ['cement', 'concrete', 'metal', 'parked', 'paved', 'standing', 'stone', 'walking'], 
'broom' : ['walking', 'young'], 
'bucket' : ['sitting', 'tall'], 
'building' : ['bare', 'calm', 'cloudy', 'docked', 'flying', 'growing', 'leafless', 'leafy', 'moving', 'parked', 'sitting', 'standing', 'walking', 'watching', 'wii'], 
'buoy' : ['sitting'], 
'bush' : ['metal', 'parked'], 
'cage' : ['large', 'long', 'parked', 'tall'], 
'camera' : ['sitting', 'standing'], 
'canopy' : ['cloudy', 'parked'], 
'car' : ['asphalt', 'calm', 'concrete', 'docked', 'driving', 'hanging', 'leather', 'off', 'paved', 'piled', 'shining', 'shiny', 'sitting', 'standing', 'street', 'tall', 'walking', 'watching', 'wood', 'wooden'], 
'cars' : ['asphalt', 'calm', 'concrete', 'docked', 'driving', 'hanging', 'leather', 'off', 'paved', 'piled', 'shining', 'shiny', 'sitting', 'standing', 'street', 'tall', 'walking', 'watching', 'wood', 'wooden'], 
'cart' : ['sitting', 'standing', 'young'], 
'ceiling fan' : ['flying', 'sitting'], 
'chair' : ['open', 'sitting'], 
'clothes' : ['sitting', 'standing'], 
'cone' : ['walking'], 
'debris' : ['bald', 'calm', 'docked', 'eating', 'parked', 'sitting', 'sleeping', 'smiling', 'standing', 'tall', 'walking', 'young'], 
'dog' : ['metal', 'wooden'], 
'dolphin' : ['denim', 'sitting', 'wood', 'wooden'], 
'dress' : ['sitting'], 
'drum' : ['sitting'], 
'duck' : ['calm', 'metal'],
'ducks' : ['calm', 'metal'], 
'excavator' : ['wooden'], 
'factory' : ['parked'], 
'fence' : ['calm', 'parked', 'sitting', 'smiling'], 
'field' : ['parked', 'tall'], 
'fire' : ['brick', 'chocolate', 'cloudy', 'dead', 'driving', 'hanging', 'long', 'looking', 'metal', 'parked', 'sitting', 'slice', 'sliced', 'standing', 'tall', 'watching'], 
'fire hydrant' : ['sitting', 'swimming', 'walking'], 
'firefighter' : ['glass', 'metal', 'parked', 'stuffed', 'open', 'framed', 'hanging', 'blurry', 'wooden', 'clear'], 
'fish' : ['metal', 'wooden'], 
'fishing rod' : ['calm'], 
'flag' : ['flying', 'metal', 'sitting', 'standing', 'tall', 'wooden'], 
'floor' : ['sitting'], 
'girl' : ['flying'], 
'glass' : ['rocky'], 
'grass' : ['asphalt', 'brick', 'calm', 'cement', 'concrete', 'metal', 'parked', 'paved', 'tiled'], 
'guitar' : ['sitting'], 
'gun' : ['ski'], 
'headphone' : ['baseball'], 
'helicopter' : ['cloudy', 'daytime', 'sitting', 'swimming'], 
'hose' : ['brick', 'sitting', 'smiling', 'standing', 'stone', 'walking', 'wood', 'wooden'], 
'ice' : ['rocky'], 
'jeep' : ['sitting', 'walking'],
'junk vehicle' : ['parked'],
'kitchen' : ['sitting', 'standing'], 
'ladder' : ['glass', 'tall'], 
'lantern' : ['sitting'], 
'license plate' : ['open'], 
'life jacket' : ['sitting'], 
'light' : ['metal'], 
'log' : ['baby', 'calm', 'concrete', 'metal', 'standing'], 
'machine' : ['sitting'],
'mailbox' : ['baseball', 'swimming', 'walking'], 
'man' : ['cardboard', 'concrete', 'large', 'long', 'metal', 'open', 'parked', 'plastic', 'potted', 'stone', 'traffic', 'wooden'], 
'map' : ['standing'], 
'mask' : ['glass'], 
'mattress' : ['concrete', 'laying', 'metal', 'sitting', 'sleeping', 'stone', 'wood', 'wooden'], 
'metal' : ['cement', 'concrete'], 
'motor' : ['driving', 'parked', 'sitting', 'standing', 'walking', 'young'], 
'motorbike' : ['riding', 'sitting', 'walking', 'wooden'], 
'motorbikes' : ['riding', 'sitting', 'walking', 'wooden'], 
'mud' : ['metal'], 
'napkin' : ['dead'], 
'newspaper' : ['purple'], 
'paddle' : ['holding', 'standing', 'walking'], 
'people' : ['cardboard', 'iron', 'long', 'metal', 'open', 'parked', 'plastic', 'potted', 'rocky', 'traffic', 'wood', 'wooden', 'wrinkled'], 
'person' : ['arched', 'cardboard', 'flying', 'framed', 'long', 'metal', 'open', 'parked', 'plastic', 'potted', 'round', 'stone', 'stuffed', 'traffic', 'wooden'], 
'pillow' : ['sleeping'], 
'pipe' : ['parked'], 
'plastic' : ['wooden'],
'pole' : ['bare', 'dead', 'flying', 'leafless', 'walking'], 
'police' : ['glass', 'metal', 'open', 'wooden'], 
'power line' : ['leafy'], 
'ramp' : ['parked'], 
'reflection' : ['calm', 'cement', 'concrete', 'driving', 'old', 'parked', 'shining', 'standing', 'stone', 'tall', 'walking'], 
'refrigerator' : ['wooden'], 
'road' : ['moving', 'parked', 'sitting', 'standing', 'walking', 'young'], 
'rope' : ['metal'], 
'sand' : ['cement', 'concrete', 'pink'], 
'shadow' : ['cement', 'concrete'], 
'shelf' : ['tall'], 
'shoe' : ['airborne', 'standing', 'sitting', 'up'], 
'shovel' : ['glass'], 
'sidewalk' : ['cardboard', 'standing', 'tall', 'walking'], 
'sign' : ['concrete', 'palm', 'parked', 'standing', 'stone', 'walking'], 
'sky' : ['bare', 'big', 'brick', 'bright', 'brown', 'cement', 'concrete', 'green', 'leafless', 'metal', 'pink', 'red', 'stone', 'tall'], 
'smoke' : ['big', 'brick', 'concrete', 'tall'], 
'snow' : ['bare', 'metal', 'concrete'],
'soldier' : ['stuffed', 'metal'], 
'spray' : ['tall', 'water'], 
'stair' : ['standing', 'walking'], 
'stick' : ['smiling', 'standing', 'tall', 'walking', 'young'], 
'stroller' : ['sitting', 'smiling', 'young'], 
'styrofoam' : ['wooden'], 
'suitcase' : ['sitting'], 
'supply' : ['concrete', 'sitting', 'standing'], 
'surveillance camera' : ['sitting', 'standing', 'walking'], 
'suv' : ['driving', 'sitting', 'standing', 'walking'], 
'table' : ['cement', 'concrete', 'parked', 'sitting'], 
'tank' : ['cement', 'concrete', 'tall'], 
'tape' : ['coffee'], 
'tent' : ['cement', 'concrete', 'parked'],
'tents' : ['cement', 'concrete', 'parked'], 
'tractor' : ['standing'], 
'traffic light' : ['flying', 'parked', 'sitting'], 
'trailer' : ['tall'], 
'trash' : ['concrete', 'parked', 'sitting'], 
'tree' : ['blue', 'brick', 'chain link', 'clear', 'clear', 'cloudy', 'concrete', 'cooked', 'flying', 'glass', 'hanging', 'lit', 'long', 'metal', 'off', 'parked', 'paved', 'sitting', 'smiling', 'standing', 'stone', 'striped', 'traffic', 'walking', 'wooden', 'young'], 
'trees' : ['blue', 'brick', 'chain link', 'clear', 'cloudy', 'electrical', 'hanging', 'long', 'metal', 'overcast', 'parked', 'standing', 'wooden'], 
'truck' : ['brick', 'cement', 'concrete', 'docked', 'playing', 'sitting', 'smiling', 'standing', 'stone', 'walking', 'watching', 'wearing', 'wood', 'wooden', 'young'], 
'tube' : ['laying', 'sitting'], 
'umbrella' : ['parked', 'sitting', 'walking', 'wood', 'wooden'], 
'van' : ['driving', 'leather', 'wood', 'wooden'], 
'vehicle' : ['concrete', 'sitting', 'standing', 'walking', 'watching', 'wooden', 'young'], 
'wand' : ['sandy'], 
'water' : ['brick', 'busy', 'cement', 'chain link', 'concrete', 'dead', 'growing', 'metal', 'old', 'painted', 'parked', 'paved', 'sitting', 'standing', 'tall', 'tile', 'tiled', 'walking', 'wearing', 'wood', 'wooden', 'young'], 
'water barrel' : ['denim', 'leather'], 
'wave' : ['moving', 'tall'], 
'wheelchair' : ['riding', 'sitting', 'smiling', 'young'], 
'wire' : ['cloudy', 'overcast', 'tall'], 
'woman' : ['brick', 'cardboard', 'long', 'metal', 'open', 'plastic', 'potted', 'stone', 'traffic', 'wooden'], 
'wood' : ['metal']
}
metallic = ['airplane', 'ambulance', 'antenna', 'ax', 'bicycle', 'bicycles', 'billboard', 'buoy', 'burner', 'bus', 'car', 'cars', 'cart', 'cell phone', 'chainsaw', 'computer', 'crane', 'drone', 'excavator', 'factory', 'fan', 'fire hydrant', 'fire truck', 'flashlight', 'grate', 'grill', 'gun', 'hammer', 'helicopter', 'jeep', 'junk vehicle', 'junk vehicles', 'key', 'lamp post', 'lantern', 'license plate', 'metal', 'microphone', 'microwave', 'motor', 'motor pump', 'motorbike', 'motorbikes', 'outlet', 'phone', 'power line', 'rail', 'railroad', 'refrigerator', 'satellite dish', 'scissors', 'shovel', 'shower head', 'sink', 'steel lamp', 'street light', 'stroller', 'surveillance camera', 'suv', 'tank', 'tractor', 'traffic light', 'trailer', 'train', 'truck', 'van', 'vehicle', 'wheelchair']

unimaterial = ['back pack', 'bag', 'bags', 'barricade', 'barrier', 'basket', 'bed', 'bell', 'bin', 'block', 'board', 'boat', 'boats', 'bottle', 'bowl', 'box', 'boxes', 'brick', 'bricks', 'bucket', 'cabinet', 'cage', 'camera', 'can', 'candle', 'cane', 'carriage', 'case', 'chain', 'chair', 'chairs', 'chalkboard', 'chimney', 'chip', 'column', 'cone', 'cones', 'container', 'cooler', 'couch', 'crate', 'cross', 'cup', 'deck', 'dock', 'door', 'drone', 'dumpster', 'electronics', 'fence', 'fishing rod', 'flippers', 'frame', 'furniture', 'gate', 'globe', 'gravel', 'handle', 'heater', 'helmet', 'jar', 'jug', 'kickstand', 'ladder', 'lamp', 'leash', 'lid', 'mailbox', 'manhole', 'mannequin', 'marker', 'mat', 'megaphone', 'mop', 'net', 'newspaper', 'notebook', 'oven', 'oven door', 'paddle', 'painting', 'parking meter', 'pen', 'pickaxe', 'picutre', 'pier', 'pillar', 'pipe', 'plate', 'pole', 'porch', 'projector', 'railing', 'rake', 'ringer', 'rod', 'rope', 'ruler', 'sacks', 'shed', 'shelf', 'sign', 'sled', 'sleeping bag', 'stair', 'stand', 'statue', 'step', 'stick', 'stool', 'stove', 'straw', 'stretcher', 'suitcase', 'table', 'tower', 'trash can', 'tripod', 'tunnele', 'vent', 'wand', 'water barrel', 'wire', 'writing']

materials  = ['brick', 'ceramic', 'chrome', 'glass', 'gravel', 'hardwood', 'metal', 'plastic', 'stainless steel', 'wooden']

unicolor = ['antenna', 'barricade', 'bicycle', 'bicycles', 'bin', 'block', 'blood', 'boat', 'boats', 'book', 'bowl', 'box', 'brick', 'bricks', 'bridge', 'broom', 'brush', 'bucket', 'buoy', 'burner', 'bus', 'cage', 'calendar', 'camera', 'cane', 'car', 'carriage', 'cars', 'cart', 'cash', 'ceiling', 'ceiling fan', 'cell phone', 'chain', 'chimney', 'cloud', 'column', 'coffin', 'computer', 'cone', 'crane', 'crate', 'cup', 'deck', 'dock', 'door', 'excavator', 'fan', 'fence', 'fire', 'fire extinguisher', 'fire hydrant', 'fish', 'fishing rod', 'flashlight', 'flippers', 'fog', 'gas tank', 'glass', 'globe', 'gravel', 'gravestone', 'grill', 'grinder', 'gun', 'handle', 'highway', 'hole', 'hose', 'ice', 'jeep', 'junk vehicle', 'junk vehicles', 'key', 'ladder', 'lamp', 'lamp post', 'lantern', 'laptop', 'leash', 'license plate', 'lid', 'log', 'mailbox', 'manhole', 'mask', 'mattress', 'microphone', 'microwave', 'monitor', 'motor', 'motorbike', 'motorbikes', 'napkin', 'net', 'oil', 'outlet', 'oven', 'oven door', 'overpass', 'paper', 'paper towel', 'parking meter', 'pen', 'phone', 'pier', 'pillar', 'pipe', 'plate', 'pole', 'power line', 'raft', 'rail', 'railroad', 'railing', 'refrigerator', 'ribbon', 'rock', 'rocks', 'rod', 'rope', 'ringer', 'ruler', 'sack', 'sacks', 'sand', 'satellite dish', 'scooter', 'shelf', 'shower head', 'sign', 'sink', 'sleeping bag', 'snow', 'space ship', 'spoon', 'stair', 'stand', 'step', 'stick', 'stove', 'straw', 'street lamp', 'street light', 'stretcher', 'stroller', 'suitcase', 'surveillance camera', 'suv', 'swimming pool', 'syringe', 'table', 'tag', 'tank', 'tape', 'tarp', 'television', 'tire', 'tires', 'tornado', 'towel', 'tractor', 'trailer', 'train', 'trash can', 'tripod', 'truck', 'tunnel', 'van', 'vehicle', 'vending machine', 'vent', 'wand', 'washing machine', 'water barrel', 'wheelchair', 'wire']

colors = ['beige', 'black', 'black and white', 'blond', 'blonde', 'blue', 'bright blue', 'brown', 'burgundy', 'dark blue', 'gray', 'green', 'light blue', 'maroon', 'orange', 'pink', 'purple', 'red', 'silver', 'teal', 'white', 'wine', 'yellow']

for m in range(len(file_list_csv)):
    name = file_list_csv[m]
    #엑셀 파일 위치
    csv = csv_path + name + 'csv'
    df = pd.read_csv(csv, index_col = 0)
    
    #이미지 파일이 들어있는 폴더
    jpg_path = 'C:/Attribute_Detection/07/0_Image/' #불러올 폴더 : jpg
    jpg = jpg_path + name + 'jpg'
    dst = cv2.imread(jpg, cv2.IMREAD_UNCHANGED)
    
    fig = plt.figure(figsize=(10,10))

    result_list = []
    for i in df.iloc:
        ymin = round(i['ymin'])
        ymax = round(i['ymax'])
        xmin = round(i['xmin'])
        xmax = round(i['xmax'])
        img = dst[ymin:ymax, xmin:xmax]

        #출력 크기 변경
        sx = 800 / (xmax - xmin)
        sy = 800 /(ymax - ymin)
        if (sx > sy) :
            sx = sy
        else :
            sy = sx
        img_resize = cv2.resize(img, None, fx=sx, fy=sy, interpolation = cv2.INTER_AREA)
        img_name = i['class']+"_"+str(xmin)
        
        #원본 전체 이미지 출력
        plt.subplot(2,1,1)
        plt.imshow(dst[:,:,::-1])
        plt.xticks([])
        plt.yticks([])
        #원본 특정 이미지 출력
        plt.subplot(2,1,2)
        plt.imshow(img[:,:,::-1])
        plt.title(i['class'] + '\n' + i['attribute'], fontsize=20)
        plt.xticks([])
        plt.yticks([])
        plt.show()
        
        cv2.namedWindow(img_name)
        #cv2.moveWindow(img_name, 0, round(800-sy*(ymax-ymin)))
        cv2.moveWindow(img_name, 0, round(1000-sy*(ymax-ymin)))
        
        #cv2.moveWindow(img_name, 400, round(1000-sy*(ymax-ymin)))
        
        #str_temp = i['attribute']
        str_temp = i['attribute']
        strings = str_temp.split(', ')
        
        """
        #attribute 사전 제거 
        for k in range(len(remove_att)):
            if remove_att[k] in strings:
                strings.remove(remove_att[k])
        """
        
        #이상한 att_dict와 비교하여 attribute 자동 제거
        if i['class'] in att_dict:
            for k in range(len(att_dict[i['class']])):
                if att_dict[i['class']][k] in strings:
                    strings.remove(att_dict[i['class']][k])
  
        cv2.imshow(img_name, img_resize)
        att_str = []
        
        #attribute가 아니라 판단되는 오브젝트는 x 입력 후 엔터로 제거
        for v in strings[:]:
            # attribute가 2개 이상일 경우 다음 class로 넘김
            if len(att_str) > 1 :
                break
            
            # 무조건 들어갈 내용
            if i['class'] in metallic and v == 'metal':
              att_str.append(v)
              continue
            if i['class'] == 'ax' and (v == 'wooden' or v == 'wood'):
                att_str.append(v)
                continue
            if i['class'] == 'baby' and (v == 'little' or v == 'young' or v == 'small'):
                att_str.append(v)
                continue
            if i['class'] == 'ball' and v == 'round':
                att_str.append(v)
                continue
            if i['class'] == 'billboard' and v == 'square':
                att_str.append(v)
                continue
            if i['class'] == 'board' and (v == 'square' or v == 'framed'):
                att_str.append(v)
                continue
            if i['class'] == 'book' and (v == 'wooden' or v == 'wood'):
                att_str.append(v)
                continue
            if i['class'] == 'bowl' and (v == 'round' or v == 'circular'):
                att_str.append(v)
                continue
            if i['class'] == 'box' and v == 'square':
                att_str.append(v)
                continue
            if i['class'] == 'boy' and (v == 'little' or v == 'young'):
                att_str.append(v)
                continue
            if i['class'] == 'branch' and (v == 'wooden' or v == 'wood'):
                att_str.append(v)
                continue
            if i['class'] == 'broom' and v == 'wooden':
                att_str.append(v)
                continue
            if i['class'] == 'burner' and v == 'electric':
                att_str.append(v)
                continue
            if i['class'] == 'bush' and (v == 'grass' or v == 'grassy' or v == 'short'):
                att_str.append(v)
                continue
            if i['class'] == 'calendar' and v == 'framed':
                att_str.append(v)
                continue
            if i['class'] == 'cash' and v == 'paper':
                att_str.append(v)
                continue
            if i['class'] == 'cat' and (v == 'fluffy' or v == 'furry'):
                att_str.append(v)
                continue
            if i['class'] == 'ceiling fan' and v == 'hanging':
                att_str.append(v)
                continue
            if i['class'] == 'child' and (v == 'little' or v == 'young'):
                att_str.append(v)
                continue
            if i['class'] == 'cloud' and (v == 'cloudy' or v == 'puffy' or v == 'fluffy'):
                att_str.append(v)
                continue
            if i['class'] == 'computer' and v == 'computer':
                att_str.append(v)
                continue
            if i['class'] == 'debris' and v == 'bricked':
                att_str.append(v)
                continue
            if i['class'] == 'dirt' and (v == 'dirt' or v == 'dirty'):
                att_str.append(v)
                continue
            if i['class'] == 'dog' and (v == 'fluffy' or v == 'furry'):
                att_str.append(v)
                continue
            if i['class'] == 'donkey' and (v == 'fluffy' or v == 'furry'):
                att_str.append(v)
                continue
            if i['class'] == 'egg' and v == 'round':
                att_str.append(v)
                continue
            if i['class'] == 'fog' and v == 'wet':
                att_str.append(v)
                continue
            if i['class'] == 'frame' and v == 'framed':
                att_str.append(v)
                continue
            if i['class'] == 'girl' and (v == 'little' or v == 'young'):
                att_str.append(v)
                continue
            if i['class'] == 'glass' and v == 'glass':
                att_str.append(v)
                continue
            if i['class'] == 'globe' and (v == 'blue' or v == 'green'):
                att_str.append(v)
                continue
            if i['class'] == 'grass' and (v == 'grass' or v == 'grassy' or v == 'green'):
                att_str.append(v)
                continue
            if i['class'] == 'gravestone' and v == 'stone':
                att_str.append(v)
                continue
            if i['class'] == 'headphone' and v == 'round':
                att_str.append(v)
                continue
            if i['class'] == 'highway' and v == 'concrete':
                att_str.append(v)
                continue
            if i['class'] == 'junk vehicle' and (v == 'bricked' or v == 'dirt' or v == 'dirty'):
                att_str.append(v)
                continue
            if i['class'] == 'landslide' and (v == 'dirt' or v == 'dirty'):
                att_str.append(v)
                continue
            if i['class'] == 'license plate' and (v == 'license' or v == 'square'):
                att_str.append(v)
                continue
            if i['class'] == 'life jacket' and (v == 'striped' or v == 'multi colored'):
                att_str.append(v)
                continue
            if i['class'] == 'light' and (v == 'bright' or v == 'glowing' or v == 'lit' or v == 'shining'):
                att_str.append(v)
                continue
            if i['class'] == 'log' and (v == 'wooden' or v == 'wood'):
                att_str.append(v)
                continue
            if i['class'] == 'monitor' and (v == 'computer' or v == 'flat screen'):
                att_str.append(v)
                continue
            if i['class'] == 'moose' and (v == 'fluffy' or v == 'furry'):
                att_str.append(v)
                continue
            if i['class'] == 'mud' and (v == 'dirt' or v == 'dirty'):
                att_str.append(v)
                continue
            if i["class"] == 'outlet' and (v == 'electric' or v == 'electrical'):
                att_str.append(v)
                continue
            if i['class'] == 'paper towel' and v == 'paper':
                att_str.append(v)
                continue
            if i['class'] == 'plant' and v == 'potted':
                att_str.append(v)
                continue
            if i['class'] == 'pot' and v == 'potted':
                att_str.append(v)
                continue
            if i['class'] == 'puddle' and v == 'wet':
                att_str.append(v)
                continue
            if i['class'] == 'purse' and v == 'leather':
                att_str.append(v)
                continue
            if i['class'] == 'rabbit' and (v == 'fluffy' or v == 'furry'):
                att_str.append(v)
                continue
            if i['class'] == 'rail' and (v == 'steel' or v == 'railroad'):
                att_str.append(v)
                continue
            if i['class'] == 'reflection' and v == 'reflecting':
                att_str.append(v)
                continue
            if i['class'] == 'river' and v == 'wet':
                att_str.append(v)
                continue
            if i['class'] == 'rock' and v == 'rocky':
                att_str.append(v)
                continue
            if i['class'] == 'rocks' and v == 'rocky':
                att_str.append(v)
                continue
            if i['class'] == 'rug' and v == 'fluffy':
                att_str.append(v)
                continue
            if i['class'] == 'sand' and v == 'sandy':
                att_str.append(v)
                continue
            if i['class'] == 'shadow' and v == 'dark':
                att_str.append(v)
                continue
            if i['class'] == 'spray' and v == 'water':
                att_str.append(v)
                continue
            if i['class'] == 'squirrel' and (v == 'brown' or v == 'furry'):
                att_str.append(v)
                continue
            if i['class'] == 'tire' and (v == 'black' or v == 'rubber'):
                att_str.append(v)
                continue
            if i['class'] == 'trafic light' and (v == 'street' or v == 'electric' or v == 'traffic'):
                att_str.append(v)
                continue
            if i['class'] == 'trash' and (v == 'dirt' or v == 'dirty'):
                att_str.append(v)
                continue
            if i['class'] == 'water' and v == 'wet':
                att_str.append(v)
                continue
            if i['class'] == 'wave' and (v == 'splashing' or v == 'wet' or v == 'foamy'):
                att_str.append(v)
                continue
            if i['class'] == 'wood' and (v == 'wooden' or v == 'wood'):
                att_str.append(v)
                continue
            
            
            
            #특정 class에서 이미 들어가 있는 요소와 세트로 넣기 - 코드 더 효율적으로 만들기
            if (i['class'] == 'branch' or i['class'] == 'tree' or i['class'] == 'trees') and 'bare' in att_str and (v =='brown' or v == 'leafless'):
                att_str.append(v)
                continue
            if (i['class'] == 'branch' or i['class'] == 'tree' or i['class'] == 'trees') and 'leafless' in att_str and (v =='bare' or v == 'brown'):
                att_str.append(v)
                continue
            if (i['class'] == 'tree' or i['class'] == 'trees') and 'large' in att_str and v =='leafy':
                att_str.append(v)
                continue
            if i['class'] == 'snow' and 'snow-covered' in att_str and v =='snowy':
                att_str.append(v)
                continue
            if i['class'] == 'snow' and 'snowy' in att_str and v =='snow-covered':
                att_str.append(v)
                continue
            
            
            #상반되는 attribute 제거     
            if 'airborne' in att_str and (v == 'fallen' or v== 'flying' or v == 'flying' or v == 'hanging' or v == 'jumping'):
                continue
            if 'american' in att_str and (v == 'blue' or v== 'red' or v == 'white'):
                continue
            if 'baby' in att_str and (v == 'old' or v== 'older'):
                continue
            if 'bald' in att_str and v == 'hairy':
                continue
            if 'balding' in att_str and v == 'hairy':
                continue
            if 'big' in att_str and (v == 'little' or v== 'small'):
                continue
            if 'blurry' in att_str and v == 'clear':
                continue
            if 'bright' in att_str and v == 'dark':
                continue
            if 'busy' in att_str and v == 'calm':
                continue
            if 'calm' in att_str and (v == 'busy' or v== 'cluttered' or v == 'crashing' or v == 'splashing'):
                continue
            if 'checkered' in att_str and v == 'striped':
                continue
            if 'clean' in att_str and (v == 'dirt' or v== 'dirty'):
                continue
            if 'clear' in att_str and (v == 'blurry' or v== 'cloudy' or v == 'hazy' or v == 'overcast'):
                continue
            if 'closed' in att_str and (v == 'open' or v== 'opened'):
                continue
            if 'cloudless' in att_str and v == 'cloudy':
                continue
            if 'cloudy' in att_str and (v == 'clear' or v== 'cloudless' or v == 'overcast'):
                continue
            if 'cluttered' in att_str and v == 'calm':
                continue
            if 'colorful' in att_str and (v == 'blue' or v == 'gray' or v == 'green' or v == 'orange' or v == 'pink' or v == 'purple' or v == 'red' or v == 'yellow'):
                continue
            if 'cooked' in att_str and v == 'cooking':
                continue
            if 'cooking' in att_str and v == 'cooked':
                continue
            if 'crashing' in att_str and v == 'calm':
                continue
            if 'dark' in att_str and v == 'bright':
                continue
            if 'dirt' in att_str and v == 'clean':
                continue
            if 'dirty' in att_str and v == 'clean':
                continue
            if 'driving' in att_str and (v == 'eating' or v == 'parked'):
                continue
            if 'eating' in att_str and (v == 'driving' or v== 'moving'):
                continue
            if 'empty' in att_str and (v == 'full' or v== 'piled' or v == 'stacked'):
                continue
            if 'fallen' in att_str and (v == 'airborne' or v== 'flying' or v == 'hanging' or v == 'jumping'):
                continue
            if 'flying' in att_str and (v == 'airborne' or v== 'fallen' or v == 'hanging' or v == 'jumping'):
                continue
            if 'full' in att_str and v == 'empty':
                continue
            if 'hairy' in att_str and (v == 'bald' or v== 'balding'):
                continue
            if 'hanging' in att_str and (v == 'airborne' or v== 'fallen' or v == 'flying' or v == 'jumping'):
                continue
            if 'jumping' in att_str and (v == 'airborne' or v== 'fallen' or v == 'flying' or v == 'hanging'):
                continue
            if 'large' in att_str and v == 'small':
                continue
            if 'laying' in att_str and (v == 'leaning' or v== 'sitting' or v == 'standing' or v == 'running'):
                continue
            if 'leafless' in att_str and v == 'leafy':
                continue
            if 'leafy' in att_str and v == 'leafless':
                continue
            if 'leaning' in att_str and (v == 'laying' or v== 'standing' or v == 'running'):
                continue
            if 'little' in att_str and v == 'big':
                continue
            if 'long' in att_str and v == 'short':
                continue
            if 'looking' in att_str and (v == 'walking' or v== 'watching'):
                continue
            if 'lying' in att_str and (v == 'sitting' or v== 'standing' or v == 'running' or v == 'walking'):
                continue
            if 'moving' in att_str and (v == 'eating' or v== 'parked' or v == 'sitting'):
                continue
            if 'old' in att_str and (v == 'baby' or v== 'young'):
                continue
            if 'older' in att_str and (v == 'baby' or v== 'young'):
                continue
            if 'open' in att_str and v == 'closed':
                continue
            if 'opened' in att_str and v == 'closed':
                continue
            if 'overcast' in att_str and (v == 'clear' or v == 'cloudy'):
                continue
            if 'palm' in att_str and v == 'pine':
                continue
            if 'parked' in att_str and (v == 'moving' or v== 'riding' or v == 'driving'):
                continue
            if 'piled' in att_str and v == 'empty':
                continue
            if 'pine' in att_str and v == 'palm':
                continue
            if 'riding' in att_str and (v == 'parked' or v == "sitting" or v == "standing" or v =="walking"):
                continue
            if 'running' in att_str and (v == 'laying' or v== 'leaning' or v == 'lying' or v == 'standing' or v == 'sitting'):
                continue
            if 'shirtless' in att_str and v == 'wearing':
                continue
            if 'short' in att_str and (v == 'long' or v == 'tall'):
                continue
            if 'sitting' in att_str and (v == 'laying' or v == 'lying' or v == 'moving' or v == 'riding' or v == 'running' or v == 'standing' or v == 'walking' or v == 'swimming' or v == 'surfing'):
                continue
            if 'sleeping' in att_str and (v == 'moving' or v== 'standing' or v == 'walking'):
                continue
            if 'small' in att_str and (v == 'big' or v== 'large' or v == 'tall'):
                continue
            if 'splashing' in att_str and v == 'calm':
                continue
            if 'stacked' in att_str and v == 'empty':
                continue
            if 'standing' in att_str and (v == 'driving' or v == 'laying' or v == 'leaning' or v == 'lying'  or v == 'riding' or v == 'running' or v == 'sitting' or v == 'sleeping' or v == 'walking' or v == 'swimming'):
                continue
            if 'striped' in att_str and v == 'checkered':
                continue
            if 'surfing' in att_str and v == 'sitting':
                continue
            if 'swimming' in att_str and (v == 'sitting' or v == 'standing'):
                continue
            if 'tall' in att_str and (v == 'short' or v == 'small'):
                continue
            if 'thick' in att_str and v == 'thin':
                continue
            if 'thin' in att_str and v == 'thick':
                continue
            if 'walking' in att_str and (v == 'looking' or v== 'lying' or v == 'running' or v == 'sitting' or v == 'sleeping' or v == 'standing'):
                continue
            if 'watching' in att_str and (v == 'looking' or v== 'walking'):
                continue
            if 'wearing' in att_str and v == 'shirtless':
                continue
            if 'young' in att_str and (v == 'old' or v== 'older'):
                continue
        
        
            
            #특정 class에서 이미 들어가 있는 요소가 있으면 제거 - 코드 더 효율적으로 만들기
            unicolor_cnt = 0
            unimaterial_cnt = 0
            for  w in att_str[:]:
                #단색인 물체는 colors 중 하나가 이미 들어있으면 나머지 색상은 제거
                if i['class'] in unicolor and w in colors and v in colors:
                    unicolor_cnt = 1
                    break
            if unicolor_cnt == 1:
                continue
            
            for  w in att_str[:]:
                #단일 물질은 materials 중 하나가 이미 들어있으면 나머지 물질은 제거
                if i['class'] in unimaterial and w in materials and v in materials:
                    unimaterial_cnt = 1
                    break
            if unimaterial_cnt == 1:
                continue
            
            #metalic인 물질은 다른 물질을 넣지 않음
            if i['class'] in metallic and v in materials and v!= 'metal':
              continue

            if i['class'] == 'bottle' and 'glass' in att_str and v =='plastic':
                continue
            if i['class'] == 'bottle' and 'plastic' in att_str and v =='glass':
                continue
            if i['class'] == 'water' and 'brown' in att_str and (v =='green' or v == 'white'):
                continue
            if i['class'] == 'water' and 'green' in att_str and (v =='brown' or v == 'white'):
                continue
            if i['class'] == 'water' and 'white' in att_str and (v =='brown' or v == 'green'):
                continue
            
            
            
            print(v)
            print("")
            #좌클릭으로 mouse_cnt를 1로 만들어 append, 우클릭으로 mouse_cnt를 0으로 만들어 제거, 클릭 할 때까지 대기
            mouse_cnt = 2
            while True :
                cv2.setMouseCallback(img_name, Click_Mouse, att_str)
                if cv2.waitKey(1) & mouse_cnt != 2:
                    break
            if mouse_cnt  == 1:
                att_str.append(v)

        #정리된 attribute를 새로 저장
        result = listToString(att_str)
        result_list.append(result)
        cv2.destroyAllWindows()

    for j in range(len(result_list)):
        df['attribute_refine'][j] = result_list[j]
    
    target = csv
    df.to_csv(target)