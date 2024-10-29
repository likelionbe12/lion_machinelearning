# streamlit에 쓸 파일
# ml은 colab
import streamlit as st

st.title("MachineLearning")
st.header("Stock 예측 프로그램")

option = st.selectbox(
    "기업 선택",
    ("삼성전자", "현대자동차", "SK하이닉스"),
)

st.write("선택 기업명:", option)