import os
import random
from shutil import copy2

# 原始img文件夹路径
file_path = r"D:/Anaconda/DeepLreaning/鼻色/data/5"
# 新文件路径
new_file_path = r"D:/Anaconda/DeepLreaning/鼻色/data"
# 划分数据比例6:2:2
split_rate = [0.6, 0.2, 0.2]
class_names = os.listdir(file_path)
# 目标文件夹下创建文件夹
split_names = ['train', 'val', 'test']
print(class_names)  # ['00000.jpg', '00001.jpg', '00002.jpg'... ]

# 判断是否存在目标文件夹，不存在则创建---->创建train\val\test文件夹w
if os.path.isdir(new_file_path):
    pass
else:
    os.makedirs(new_file_path)
for split_name in split_names:
    split_path = new_file_path + "/" + split_name
    print(split_path)  # D:/Code/Data/GREENTdata/train, val, test
    if os.path.isdir(split_path):
        pass
    else:
        os.makedirs(split_path)

# 按照比例划分数据集，并进行数据图片的复制
for class_name in class_names:
    current_data_path = file_path  # D:/Code/Data/centerlinedata/tem_voc/JPEGImages/
    current_all_data = os.listdir(current_data_path)
    current_data_length = len(current_all_data)  # 文件夹下的图片个数
    current_data_index_list = list(range(current_data_length))
    random.shuffle(current_data_index_list)

    train_path = os.path.join(new_file_path, 'train/')  # D:/Code/Data/GREENTdata/train/
    val_path = os.path.join(new_file_path, 'val/')  # D:/Code/Data/GREENTdata/val/
    test_path = os.path.join(new_file_path, 'test/')  # D:/Code/Data/GREENTdata/test/

    train_stop_flag = current_data_length * split_rate[0]
    val_stop_flag = current_data_length * (split_rate[0] + split_rate[1])

current_idx = 0
train_num = 0
val_num = 0
test_num = 0
# 图片复制到文件夹中
for i in current_data_index_list:
    src_img_path = os.path.join(current_data_path, current_all_data[i])
    if current_idx <= train_stop_flag:
        copy2(src_img_path, train_path)
        train_num += 1
    elif (current_idx > train_stop_flag) and (current_idx <= val_stop_flag):
        copy2(src_img_path, val_path)
        val_num += 1
    else:
        copy2(src_img_path, test_path)
        test_num += 1
    current_idx += 1
print("Done!", train_num, val_num, test_num)