import os
import math

def count_total_files(current_dir,input_dir_path):
    total_files = 0
    for dirpath, dirs, files in os.walk(input_dir_path):
        # Root dir
        if dirpath == input_dir_path or dirpath == current_dir:
            # print 'dirpath',dirpath
            continue
        total_files = total_files+len([f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))])
    # print 'total files >>>>>>>>>>>>>>',total_files
    return total_files

def count_pickfiles(input_dir_path,total_files,based_dir_path):
    num_files_in = len([f for f in os.listdir(input_dir_path) if os.path.isfile(os.path.join(input_dir_path, f))])
    picked_files_num = {}

    
    for dirpath, dirs, files in os.walk(based_dir_path):
        # Root dir
        if dirpath == based_dir_path or dirpath == input_dir_path:
            # print 'dirpath',dirpath            
            continue
        deepestFolderName = os.path.split(dirpath)[-1]
        classId = deepestFolderName.split('_')[0]
        className = deepestFolderName.split('_')[1]
        num_files = len([f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))])
        picked_files_num[classId] = int(math.ceil((num_files*num_files_in)/float(total_files)))
    # print picked_files_num
    return picked_files_num
    

# total_files = count_total_files('./train-data/10_Bakery Cake','./train-data')
# print total_files
# print count_pickfiles('./train-data/10_Bakery Cake',total_files,'./train-data')
