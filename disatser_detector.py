from PIL import Image
import requests
import torch
import os
import shutil
from transformers import CLIPProcessor, CLIPModel
from PIL import UnidentifiedImageError
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


device = torch.device("cuda")
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

model.to(device)

# 사진 폴더 
jpg_path = 'C:/disaster_detection/image/RawImg_0509/'

file_list = os.listdir(jpg_path)
file_list_jpg = [file for file in file_list if file.endswith('.jpg')]

move_path = 'C:/disaster_detection/classified_image/'
for m in range(len(file_list)):
    
    name = file_list_jpg[m]
    jpg = jpg_path + name
    try : 
        image = Image.open(jpg)
    except UnidentifiedImageError :
        continue
    except OSError :
        continue
    
    try :
        """
        inputs = processor(
        text=[
            "A photo of a flood.", 
            "A photo of no flood."
            ], 
        images=image, return_tensors="pt", padding=True)
        """
        inputs = processor(
        text=[
            "A photo of a disaster or an accident.", 
            "A photo of no disaster or no accident."
            ], 
        images=image, return_tensors="pt", padding=True)
        
    except ValueError :
        continue
    
    inputs.to(device)
    
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
    probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities
    
    #복사할 폴더
    if torch.argmax(probs) == 0:
        move_path = 'C:/disaster_detection/classified_image/disaster/'
    if torch.argmax(probs) == 1:
        move_path = 'C:/disaster_detection/classified_image/z_etc/'    
    
    destination = move_path + name
    image.close()
    shutil.copyfile(jpg, destination)