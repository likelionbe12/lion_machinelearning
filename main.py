# streamlit에 쓸 파일
# ml은 colab
import streamlit as st
from pages import page2


pg = st.navigation([
    st.Page(page2, title="Stock 데이터분석", icon=":material/favorite:"),
    st.Page("page1.py", title="캘리포니아 집값 예측", icon="🔥"),
])
pg.run()