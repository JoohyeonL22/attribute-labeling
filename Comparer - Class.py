import os
import pandas as pd
import sys

class_list = ['airplane', 'ambulance', 'animal', 'antenna', 'avalanche', 'ax', 'baby', 'back pack', 'bag', 'bags', 'ball', 'balloon', 'bamboo', 'banana', 'banner', 'barrel', 'barrels', 'barricade', 'barrier', 'basket', 'basketball board', 'beach', 'bear', 'bed', 'bell', 'bench', 'bicycle', 'bicycles', 'billboard', 'bin', 'bins', 'bird', 'blanket', 'blind', 'block', 'blood', 'board', 'boat', 'boats', 'body', 'book', 'booth', 'bottle', 'bowl', 'box', 'boxes', 'boy', 'branch', 'brick', 'bricks', 'bridge', 'broom', 'brush', 'bucket', 'buidling', 'build', 'building', 'buoy', 'burner', 'bus', 'bush', 'cabinet', 'cactus', 'cage', 'calendar', 'camera', 'can', 'candle', 'cane', 'canopy', 'car', 'cargo', 'carpet', 'carriage', 'cars', 'cart', 'case', 'cash', 'cat', 'ceiling', 'ceiling fan', 'cell phone', 'chain', 'chainsaw', 'chair', 'chairs', 'chalkboard', 'chicken', 'child', 'chimney', 'chip', 'cliff', 'clock', 'cloth', 'clothes', 'cloud', 'coconut', 'coffin', 'column', 'computer', 'cone', 'cones', 'container', 'cooler', 'couch', 'cover', 'cow', 'cows', 'crack', 'crane', 'crate', 'cross', 'crosswalk', 'cup', 'curb', 'curtain', 'cushion', 'debris', 'dec', 'deck', 'deer', 'dirt', 'dock', 'dog', 'doll', 'dolphin', 'donkey', 'door', 'dress', 'drone', 'drum', 'duck', 'ducks', 'dumpster', 'earring', 'egg', 'electronics', 'excavator', 'factory', 'fan', 'fence', 'field', 'fire', 'fire extinguisher', 'fire hydrant', 'fire truck', 'firefighter', 'fireplace', 'fish', 'fishing rod', 'flag', 'flashlight', 'flippers', 'floor', 'flower', 'fog', 'foil', 'food', 'frame', 'fruit', 'furniture', 'gas station', 'gas tank', 'gate', 'girl', 'glass', 'globe', 'goat', 'goggles', 'grass', 'grate', 'gravel', 'gravestone', 'grill', 'grinder', 'guitar', 'gun', 'hammer', 'handle', 'hay', 'headphone', 'heater', 'helicopter', 'helmet', 'highway', 'hill', 'hole', 'horse', 'hose', 'ice', 'jar', 'jeep', 'jet ski', 'jug', 'juice', 'junk vehicle', 'junk vehicles', 'key', 'kickstand', 'kitchen', 'knife', 'ladder', 'lamp', 'lamp post', 'landslide', 'lantern', 'laptop', 'leaf', 'leash', 'license plate', 'lid', 'life jacket', 'light', 'log', 'machine', 'mailbox', 'male', 'man', 'manhole', 'mannequin', 'map', 'marker', 'mask', 'mat', 'material', 'mattress', 'medicines', 'megaphone', 'metal', 'microphone', 'microwave', 'monitor', 'moose', 'mop', 'motor', 'motor pump', 'motorbike', 'motorbikes', 'mountain', 'mud', 'napkin', 'net', 'newspaper', 'notebook', 'oar', 'oil', 'outlet', 'oven', 'oven door', 'overpass', 'paddle', 'painting', 'paper', 'paper towel', 'parachute', 'parking lot', 'parking meter', 'path', 'pen', 'pencil', 'people', 'person', 'phone', 'piano', 'pickaxe', 'picture', 'pier', 'pigeon', 'pile', 'pillar', 'pillow', 'pineapple', 'pipe', 'pitcher', 'pizza', 'pizza box', 'plant', 'planter', 'plants', 'plastic', 'plate', 'playground', 'pole', 'police', 'polices', 'pool', 'porch', 'post', 'poster', 'pot', 'power line', 'printer', 'projector', 'puddle', 'purse', 'rabbit', 'radio', 'raft', 'rail', 'railing', 'railroad', 'rainbow', 'rake', 'ramp', 'reflection', 'refrigerator', 'ribbon', 'ringer', 'river', 'road', 'rock', 'rocks', 'rod', 'roof', 'room', 'rope', 'rug', 'ruler', 'sack', 'sacks', 'saddle', 'sand', 'satellite dish', 'satue', 'saw', 'scissors', 'scooter', 'seaweed', 'shadow', 'shark', 'shed', 'sheet', 'shelf', 'shoe', 'shovel', 'shower head', 'sidewalk', 'sign', 'sink', 'skateboard', 'sky', 'sled', 'sleeping bag', 'slippers', 'smoke', 'snake', 'snow', 'soccer ball', 'soldier', 'space ship', 'spoon', 'spray', 'squirrel', 'stair', 'stand', 'statue', 'step', 'stick', 'sticker', 'stool', 'stove', 'straw', 'street', 'street lamp', 'street light', 'stretcher', 'stroller', 'structure', 'styrofoam', 'suitcase', 'sun', 'supply', 'surfboard', 'surveillance camera', 'suv', 'swimming pool', 'syringe', 'table', 'tablet', 'tag', 'tank', 'tape', 'tarp', 'television', 'tent', 'tents', 'tire', 'tires', 'toilet', 'tool', 'tornado', 'towel', 'tower', 'town', 'toy', 'track', 'tractor', 'traffic light', 'trailer', 'train', 'trash', 'trash can', 'tree', 'trees', 'tripod', 'truck', 'tube', 'tunnel', 'umbrella', 'van', 'vase', 'vegetable', 'vehicle', 'vending machine', 'vent', 'wall', 'wand', 'washing machine', 'watch', 'water', 'water barrel', 'waterfall', 'wave', 'well', 'wheelchair', 'wire', 'woman', 'womasn', 'wood', 'writing']

#새로 들어온 파일
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
    
    
    #오타가 난 class가 있는 파일 찾기
    for i in df.iloc:
        if i['class'] == 'pereson':
            print(name)
    
    for i in df.iloc:
        class_name.append(i['class'])
    
    
class_name = list(set(class_name))
class_name.sort()


#1. 새로 추가된 class 확인

for i in range(len(class_name)):
    if class_name[i] not in class_list :
        print(class_name[i])


"""
#2. 새로 적용할 전체 class 리스트
all_list =[]

for i in range(len(class_list)):
    all_list.append(class_list[i])

for i in range(len(class_name)):
    all_list.append(class_name[i])

all_list = list(set(all_list))
all_list.sort()
print(all_list)
"""





