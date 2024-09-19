# 1.提取txt文件
# 2.获取内容存入数组
# 3.统计1、0的个数
# 遍历每个数组，检测第一个第一位，是1就biwi_voca_ours_face+1，是0就biwi_voca_voca_face+1
# 4.计算百分比

# voca: 1/6/11
# meshtalk: 2/7/12
# faceformer: 3/8/13
# codetalker: 4/9/14
# gt: 5/10/15

import os

biwi_face = {
    "biwi_gt_ours_face": 0,
    "biwi_gt_gt_face": 0
}

biwi_lip = {
    "biwi_gt_ours_lip": 0,
    "biwi_gt_gt_lip": 0
}

keyname = {
    "gt": 0
}

biwi_realism = {
    "biwi_gt_realism": 0
}

biwi_lip_sync = {
    "biwi_gt_lip_sync": 0
}

def main():
    folder_path = "BIWI_data"
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        if "BIWI" in file_name:
            file_path = os.path.join(folder_path, file_name)
            
            with open(file_path, "r") as file:
                file_content = file.read()
                digits = [char for char in file_content if char.isdigit()]
                array = [int(digit) for digit in digits]
                
                count(array)
    compution()

def count(array):
    global biwi_face, biwi_lip
    
    for key, value in biwi_face.items(): 
        for index, element in enumerate(array):
            for idx, name in enumerate(keyname):
                if name in key and index < 15:
                    if element == 1 and "ours" in key:
                        biwi_face[key]+=1
                    if element == 0 and "ours" not in key:
                        biwi_face[key]+=1  

    for key, value in biwi_lip.items(): 
        for index, element in enumerate(array):
            for idx, name in enumerate(keyname):
                if name in key and index >= 15:
                    if element == 1 and "ours" in key:
                        biwi_lip[key]+=1
                    if element == 0 and "ours" not in key:
                        biwi_lip[key]+=1     

def compution():
    global biwi_face, biwi_lip
    global biwi_realism, biwi_lip_sync

    for key, value in biwi_face.items():
        print(key, value)

    for key, value in biwi_lip.items():
        print(key, value)

    face_keys = list(biwi_realism.keys())  
    face_values = list(biwi_face.values()) 
    for i in range(0, len(face_values), 2):
        if i + 1 < len(face_values): 
            biwi_realism[face_keys[int(i/2)]] = round((face_values[i] /(face_values[i] + face_values[i+1]))*100, 2)

    for key, value in biwi_realism.items():
        print(key, value)    

    lip_keys = list(biwi_lip_sync.keys()) 
    lip_values = list(biwi_lip.values())  
    for i in range(0, len(lip_values), 2):
        if i + 1 < len(lip_values):  
            biwi_lip_sync[lip_keys[int(i/2)]] = round((lip_values[i] /(lip_values[i] + lip_values[i+1]))*100, 2)

    for key, value in biwi_lip_sync.items():
        print(key, value)    

    return biwi_realism, biwi_lip_sync

if __name__=='__main__':
    main()
