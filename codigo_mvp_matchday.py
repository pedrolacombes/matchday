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
  #expander = st.expander('Comentários')
  #expander.write('Irado')
  #expander.write('Muito legal')
  
  def likes(like_button)
    if st.button('Like'):
      likes = 1
    if st.button('Unlike'):
      likes = 0
    return likes
    
  def like_button(likes):
      if likes == 0:
        st.button('Like'):
      else:
        st.button('Unlike'):

  botao = like_button(likes)     
