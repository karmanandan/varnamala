import json
import os
from unittest import result
# list_images = os.listdir('./Original_images')
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


##############################
# 3
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random
import numpy as np

stroke_width = 3
stroke_color =  "#FFFFFF"
bg_color = "#000000"
drawing_mode = "freedraw"


list_images = os.listdir('./Original_images')
img_name = random.choice(list_images)
destination_path = os.path.join('destination_dir',img_name.split('.')[0]+'_dir')

st.title("project-Varnamala")

st.header("Observe this")
st.image(f'./Original_images/{img_name}', width=200)


st.header("Draw here")
        # img_data = None
img_data = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image = None,
    update_streamlit=True,
    height=300,
    width=300,
    drawing_mode=drawing_mode,
    # initial_drawing={'background':'#fffff'},
    key="canvas",
).image_data

if img_data is not None:
    image = Image.fromarray(img_data.astype(np.uint8))
    image = image.resize((64,64))
    image.save(os.path.join(destination_path,"image_file.png"))

st.success("saved")