from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

st.set_page_config(page_title="gemini Image info")

st.header("Gemini LLM Application")

input=st.text_input('Input:',key="input")
upload=st.file_uploader("Chooose image",type=["jpg","jpeg","png"])
image=""
if upload is not None:
    image=Image.open(upload)
    st.image(image,caption="Uploaded image",use_column_width=True)
submit=st.button("Tell me about image")

if submit:
    response=get_gemini_response(input)
    st.subheader("the response is")
    st.write(response)