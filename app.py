from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import base64
import io
import os
import numpy as np
import random
import time
import pyautogui


stroke_width = 3
stroke_color =  "#FFFFFF"
bg_color = "#000000"
drawing_mode = "freedraw"
st.set_page_config(page_title="project-Varnamala", layout="wide")

list_images = os.listdir('./Original_images')
img = random.choice(list_images)

col1,col2 = st.columns([1,2])

with col1:
    st.header("Observe this image, Draw in next canvas")
    st.image(f'./Original_images/{img}', width=200)
    # time.sleep(1)
with col2:
    st.header("Draw here")
    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        # background_image=Image.open(bg_image) if bg_image else None,
        background_image = None,
        update_streamlit=True,
        height=300,
        width=300,
        drawing_mode=drawing_mode,
        # point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
        key="canvas",
    )


# if canvas_result.image_data is not None:
#     st.image(canvas_result.image_data)


#Saving upload
img_data = canvas_result.image_data

if img_data is not None:
    image = Image.fromarray(img_data.astype(np.uint8))
    image = image.resize((64,64))
    image.save(os.path.join("Images","image_file.png"))
    st.success("File Saved")

    # #You can check .empty documentation
    # placeholder = st.empty()

    # with placeholder.container():
    #     btn = st.button("Next")

    # #If btn is pressed or True
    # if btn:
    #     #This would empty everything inside the container
    #     placeholder.empty()

 
    # if st.button("Next"):
    #     pyautogui.hotkey("ctrl","F5")