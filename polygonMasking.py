import os
import shutil
from glob import glob
import json
import numpy as np
from PIL import Image, ImageDraw
import itertools
def masking(filename_idx):

    path = '/Users/louis/macFolder/mask/segmentaion_json'
    file_list = os.listdir(path)
    file_list.sort()
    dir_path = '/Users/louis/macFolder/mask/segmentation_label'

    for filename in file_list:
        file = open(path + '/' + filename)
        jsonString = json.load(file)
        annotations = jsonString.get("annotations")
        polygons = []

        crossWalkCheck = 0
        #annotations의 class에 crosswalk가 포함되어 있는지 확인.
        for keyidx in annotations:
            ano_class = keyidx.get("class")
            if ano_class == 'crosswalk' and keyidx.get("data") != []:
                crossWalkCheck = 1
        
        if crossWalkCheck == 1:
            for keyidx in annotations:
                ano_class = keyidx.get("class")
                if ano_class == 'crosswalk' and keyidx.get("data") != []:
                    ano_data = keyidx.get("data")
                    polygon = []
                    for dataidx in ano_data:
                        polygon.append(int(dataidx.get("x")))
                        polygon.append(int(dataidx.get("y")))
                    polygon = [polygon]
                    polygons.append(polygon)
                    
            # polygon 구성 point들을 polygons에 저장했음.
            img_size = jsonString.get("image").get("image_size")
            width = img_size[1]
            height = img_size[0]         
            img = Image.new('L', (width, height), 1)
            for idx2 in range(len(polygons)):
                ImageDraw.Draw(img).polygon(list(itertools.chain(*polygons[idx2])), outline=0, fill=0)
            # polygon masking 했음.
            mask_img = np.array(img)
            mask_img = Image.fromarray(mask_img)
            #mask_img.show()
            mask_img.save(dir_path + '/' + filename[:-5] + '.png')
            
            crossWalkCheck = 0


if __name__ == '__main__':

    for idx in range(3, 5):
        masking(idx) 
        print(idx, "/ 4")
    