import os
import math

def count_total_files(input_dir_path):
    total_files = 0
    for dirpath, dirs, files in os.walk(input_dir_path):
        # Root dir
        if dirpath == input_dir_path:
            # print 'dirs',dirs
            continue
        total_files = total_files+len([f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))])
    return total_files

def count_pickfiles(input_dir_path,total_files):
    num_files_in = len([f for f in os.listdir(input_dir_path) if os.path.isfile(os.path.join(input_dir_path, f))])
    dirPath = os.path.dirname(input_dir_path+"/")
    dirName = os.path.basename(dirPath) # 10_Bakery Cake
    classId_in = dirName.split('_')[0]
    picked_files_num = {}

    PATH = './train-data'
    for dirpath, dirs, files in os.walk(PATH):
        # Root dir
        if dirpath == PATH:
            # print 'dirs',dirs
            continue
        deepestFolderName = os.path.split(dirpath)[-1]
        classId = deepestFolderName.split('_')[0]
        className = deepestFolderName.split('_')[1]
        num_files = len([f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))])
        picked_files_num[classId] = int(math.ceil((num_files*num_files_in)/total_files))
    return picked_files_num
    

total_files = count_total_files('./train-data')
print count_pickfiles('./train-data/10_Bakery Cake',total_files)
