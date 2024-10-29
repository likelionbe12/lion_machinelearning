from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pickle
import streamlit as st

st.title("MachineLearning")
st.header("캘리포니아 집값 예측 프로그램")
cols = ['MedInc','HouseAge','AveRooms','AveBedrms', 'Population','AveOccup','Latitude','Longitude']
datas = [0]*8
for idx, col in enumerate(cols):
    datas[idx] = st.number_input(col)
# MedInc= st.number_input("MedInc")
# HouseAge= st.number_input("HouseAge")
# AveRooms= st.number_input("AveRooms")
# AveBedrms= st.number_input("AveBedrms")
# Population= st.number_input("Population")
# AveOccup= st.number_input("AveOccup")
# Latitude= st.number_input("Latitude")
# Longitude= st.number_input("Longitude")


x = np.array(datas).reshape(1, -1)
# x.shape

with open("rf_house.pickle", 'rb') as f:
    rf_model = pickle.load(f)

y = rf_model.predict(x)

st.header("예측되는 집값은 {}입니다.".format(y))