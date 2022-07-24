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

list_images = os.listdir('./Original_images')
img_name = random.choice(list_images)
destination_path = os.path.join('destination_dir',img_name.split('.')[0]+'_dir')

#################################
st.set_page_config(
    page_title="project-Varnamala",
    page_icon=":pencil:",
)

hide_streamlit_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            #the-title {text-align: center;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.title("project-Varnamala")

#####################
# def save_path(img_data, destination_path,img_name):
def save_path(img_data,img_name):
    # print("save path->",img_data)
    # time.sleep(3)
    if img_data is not None:
        destination_path = os.path.join('destination_dir',img_name.split('.')[0]+'_dir')
        image = Image.fromarray(img_data.astype(np.uint8))
        image = image.resize((64,64))
        image.save(os.path.join(destination_path,img_name+".png"))
        st.success("success")
    else:
        print('error')
        st.warning("img no saved")
    
#########################

def success():
    st.success("File Saved")

############################3


with st.form(key='canvas',clear_on_submit=True): 
    col1,col2 = st.columns(2)

    ################################

    with col1:
        st.header("Observe this")
        st.image(f'./Original_images/{img_name}', width=200)

    #########################################
    with col2:
        # Create a canvas component
        st.header("Draw here")
        img_data = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            background_color=bg_color,
            # background_image = None,
            update_streamlit=True,
            height=300,
            width=300,
            drawing_mode=drawing_mode,
            initial_drawing={'background':'#fffff'},
            key="canvas",
        ).image_data

        # print(img_data)

        ###########################################
        # if st.button('next'):
        #     save_path(img_data, destination_path)
        #     st.success('saved')
        # else:
        #     st.warning("error")
        ############################################
        sub_ =  st.form_submit_button('save & next')
        if sub_:
            # save_path(img_data, destination_path,img_name)
            save_path(img_data,img_name)
            # success()
            # time.sleep(3)
