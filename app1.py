from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import base64
import io
import os
import numpy as np
import random
import time

stroke_width = 3
stroke_color =  "#FFFFFF"
bg_color = "#000000"
drawing_mode = "freedraw"

# Clean initial drawing, override its background color
# initial_drawing = (
#     {"version": "4.4.0"} if initial_drawing is None else initial_drawing
# )
# initial_drawing["background"] = "#000000"

# @st.cache()#(suppress_st_warning=True)
# def create_randomAlphabet(img_name,img_data):
#     # img_name = random.choice(list_images)
#     # print("img_name",img_name)
#     destination_path = os.path.join('destination_dir',img_name.split('.')[0]+'_dir')
#     print("destination_path",destination_path)
#     save_imageData(destination_path,img_data)
#     # st.image(f'./Original_images/{img_name}', width=200)
    
def showImage(img_name):
    st.image(f'./Original_images/{img_name}', width=200)

# @st.cache()(suppress_st_warning=True)
def draw_Canvas():
    st.header("Draw here")
    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        background_image = None,
        update_streamlit=True,
        height=300,
        width=300,
        drawing_mode=drawing_mode,
        initial_drawing={'background':'#fffff'},
        key="canvas",
    )
    # st.experimental_singleton.clear()
    return canvas_result


def save_imageData(destination_path,img_data):
    if img_data is not None:
        image = Image.fromarray(img_data.astype(np.uint8))
        image = image.resize((64,64))
        image.save(os.path.join(destination_path,"image_file.png"))
        st.success("File Saved")
        # st.experimental_singleton.clear()

st.set_page_config(page_title="project-Varnamala", layout="wide")

list_images = os.listdir('./Original_images')
# img = random.choice(list_images)

def main():
    with st.form(key='draw',clear_on_submit=True):
        canvas_result = draw_Canvas()
        img_data = canvas_result.image_data
        img_name = random.choice(list_images)
        print("img_name",img_name)
        showImage(img_name)
        destination_path = os.path.join('destination_dir',img_name.split('.')[0]+'_dir')
        save_imageData(destination_path,img_data)
        # st.form_submit_button("next")
        # btn = st.form_submit_button("next")
        # if btn:
        #     st.experimental_rerun()
            # create_randomAlphabet(img_name,img_data)
        # st.form_submit_button('save & next',on_click=create_randomAlphabet(img_name,img_data))


if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()