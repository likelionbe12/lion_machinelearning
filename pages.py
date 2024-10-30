import streamlit as st
import FinanceDataReader as fdr
stocks = fdr.StockListing('KOSPI') # KOSPI: 940 종목
stocks_df = stocks[['Code','Name']]
company_dict_comp = {company.Name : company.Code for idx, company in stocks_df.iterrows()}
# {한화우:005885}

def page2():
    options = st.multiselect(
    "관심 기업을 선택하세요",
    list(company_dict_comp.keys()),
    list(company_dict_comp.keys())[:5],
    )
    # print(type(options))
    st.write("You selected:", options)
    