import os
### initialize
path = '/Users/louis/macFolder/lane_data/final_data'
image_foldername = 'images'
label_foldername = 'labels'
train_test_ratio = 0.8

train_num = 1850 #int(train_test_ratio * file_num)
###
image_folder_path = path + '/' + image_foldername
label_folder_path = path + '/' + label_foldername
image_filelist = os.listdir(image_folder_path)
image_filelist.sort()
# .DS_Store 오류 수정
image_filelist = image_filelist[1:]
label_filelist = os.listdir(label_folder_path)
label_filelist.sort()
label_filelist = label_filelist[1:] # 오류 수정 코드
file_num = len(image_filelist)

if file_num != len(label_filelist):
    print("Image and label files have not same number.")

f = open(os.path.join(path, 'train.txt'), 'w')
for idx in range(train_num):
    f.write(image_foldername + '/' + image_filelist[idx] + ' ' + label_foldername + '/' + label_filelist[idx] + '\n')
f.close()

f = open(os.path.join(path, 'val.txt'), 'w')

for idx in range(train_num, file_num):
    f.write(image_foldername + '/' + image_filelist[idx] + ' ' + label_foldername + '/' + label_filelist[idx] + '\n')
f.close()
