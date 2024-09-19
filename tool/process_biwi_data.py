import os

biwi_face = {
    "biwi_voca_ours_face": 0,
    "biwi_voca_voca_face": 0,
    "biwi_meshtalk_ours_face": 0,
    "biwi_meshtalk_meshtalk_face": 0,
    "biwi_faceformer_ours_face": 0,
    "biwi_faceformer_faceformer_face": 0,
    "biwi_codetalker_ours_face": 0,
    "biwi_codetalker_codetalker_face": 0,
    "biwi_gt_ours_face": 0,
    "biwi_gt_gt_face": 0
}

biwi_lip = {
    "biwi_voca_ours_lip": 0,
    "biwi_voca_voca_lip": 0,
    "biwi_meshtalk_ours_lip": 0,
    "biwi_meshtalk_meshtalk_lip": 0,
    "biwi_faceformer_ours_lip": 0,
    "biwi_faceformer_faceformer_lip": 0,
    "biwi_codetalker_ours_lip": 0,
    "biwi_codetalker_codetalker_lip": 0,
    "biwi_gt_ours_lip": 0,
    "biwi_gt_gt_lip": 0
}

keyname = {
    "voca": 0,
    "meshtalk": 1,
    "faceformer": 2,
    "codetalker": 3,
    "gt": 4
}

biwi_realism = {
    "biwi_voca_realism": 0,
    "biwi_meshtalk_realism": 0,
    "biwi_faceformer_realism": 0,
    "biwi_codetalker_realism": 0,
    "biwi_gt_realism": 0
}

biwi_lip_sync = {
    "biwi_voca_lip_sync": 0,
    "biwi_meshtalk_lip_sync": 0,
    "biwi_faceformer_lip_sync": 0,
    "biwi_codetalker_lip_sync": 0,
    "biwi_gt_lip_sync": 0
}

def main():
    folder_path = "biwi_data"
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        if "biwi" in file_name:
            file_path = os.path.join(folder_path, file_name)
            
            with open(file_path, "r") as file:
                file_content = file.read()
                digits = [char for char in file_content if char.isdigit()]
                array = [int(digit) for digit in digits]
                
                count(array)
    compution()

def count(array):
    global biwi_face, biwi_lip
    indices = [
        [0, 5, 10],
        [1, 6, 11],
        [2, 7, 12],
        [3, 8, 13],
        [4, 9, 14],
        [15, 20, 25],
        [16, 21, 26],
        [17, 22, 27],
        [18, 23, 28],
        [19, 24, 29]
    ]  

    for key, value in biwi_face.items(): 
        for index, element in enumerate(array):
            for idx, name in enumerate(keyname):
                if name in key and index in indices[idx]:
                    if element == 1 and "ours" in key:
                        biwi_face[key]+=1
                    if element == 0 and "ours" not in key:
                        biwi_face[key]+=1  

    for key, value in biwi_lip.items(): 
        for index, element in enumerate(array):
            for idx, name in enumerate(keyname):
                if name in key and index in indices[idx+5]:
                    if element == 1 and "ours" in key:
                        biwi_lip[key]+=1
                    if element == 0 and "ours" not in key:
                        biwi_lip[key]+=1     

def compution():
    global biwi_face, biwi_lip
    global biwi_realism, biwi_lip_sync

    # 遍历字典的键和值
    for key, value in biwi_face.items():
        print(key, value)

    for key, value in biwi_lip.items():
        print(key, value)

    face_keys = list(biwi_realism.keys())  # 获取字典的所有键并转换为列表
    face_values = list(biwi_face.values())  # 获取字典的所有值并转换为列表
    for i in range(0, len(face_values), 2):
        if i + 1 < len(face_values):  # 检查下一个索引是否存在，确保索引不越界
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

