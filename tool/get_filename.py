import os

folder_list = {
    "user_study/multiface/CodeTalker",
    "user_study/multiface/FaceFormer",
    "user_study/multiface/GT",
    "user_study/multiface/MeshTalk",
    "user_study/multiface/voca",
    "user_study/multiface/SelfTalk",
    "user_study/multiface/DiffSpeaker",
    "user_study/multiface/TalkingStyle",
    "user_study/multiface/FaceDiffuser",
}


for folder_path in folder_list:
    # 获取文件夹中的文件名列表
    file_names = os.listdir(folder_path)
    # 确定文本文件的路径：如multiface_codetalker
    txt_file_name = "_".join(folder_path.split("/")[1:])
    # txt文件路径
    os.makedirs('filename', exist_ok=True)
    txt_file_path = fr"filename/{txt_file_name}.txt"
    # 打开txt文件并写入文件名
    with open(txt_file_path, 'w') as txt_file:
        for file_name in file_names:
            txt_file.write(folder_path + '/' + file_name + '\n')


