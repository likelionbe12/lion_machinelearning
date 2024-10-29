# streamlit에 쓸 파일
# ml은 colab
import streamlit as st

def page2():
    st.title("Second page")

pg = st.navigation([
    st.Page("page1.py", title="캘리포니아 집값 예측", icon="🔥"),
    st.Page(page2, title="Second page", icon=":material/favorite:"),
])
pg.run()