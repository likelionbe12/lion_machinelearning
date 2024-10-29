# streamlit에 쓸 파일
# ml은 colab
import streamlit as st

st.title("MachineLearning")
st.header("Stock 예측 프로그램")

option = st.selectbox(
    "관심 기업은?",
    ("테슬라", "OpenAI", "Meta"),
)

st.write("You selected:", option)