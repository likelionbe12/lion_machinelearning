# streamlit에 쓸 파일
# ml은 colab
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pickle

st.title("MachineLearning")
st.header("캘리포니아 집값 예측 프로그램")
cols = ['MedInc','HouseAge','AveRooms','AveBedrms', 'Population','AveOccup','Latitude','Longitude']
datas = [0]*8
for idx, col in enumerate(cols):
    datas[idx] = st.number_input(col)
x = np.array(datas).reshape(1, -1)
# x.shape

with open("rf_house.pickle", 'rb') as f:
    rf_model = pickle.load(f)

y = rf_model.predict(x)

st.header("예측되는 집값은 {}입니다.".format(y))