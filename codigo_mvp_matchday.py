# -*- coding: utf-8 -*-
"""Codigo_MVP_Matchday

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10HbU1kZl20gJgK8-MBIZeuppj6aZRfCV
"""

import streamlit as st

with st.container():
  url = 'https://www.youtube.com/watch?v=JK14AYu-wOs'
  st.video(url)
  expander = st.expander('Comentários')
  expander.write('Irado')
  expander.write('Muito legal')
  title = st.text_input('Deixe seu comentário','')
  title
  
    
  
  
  
