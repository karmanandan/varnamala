import json
import os
from unittest import result
list_images = os.listdir('./Original_images')
##############
# 1. creating subfolders for each original_img
# for i in list_images:
#     path_ = i.split(".")[0]+"_dir"
#     os.mkdir(os.path.join('./destination_dir',path_))


###############
# 2. create a txt file of source and destination path of images
# result_dict = {}
# for i in list_images:
#     path_ = i.split(".")[0]+"_dir"
#     fol_path = os.path.join('destination_dir',path_)
#     result_dict[i] = fol_path

# with open("./resources/file_path_src_destination.txt",'w') as f:
#     f.write(json.dumps(result_dict))
