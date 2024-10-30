from sklearn.model_selection import train_test_split
import streamlit as st
import FinanceDataReader as fdr
from utils import get_company_stock_data
from lightgbm import LGBMClassifier
import pandas as pd

stocks = fdr.StockListing('KOSPI') # KOSPI: 940 종목
stocks_df = stocks[['Code','Name']]
company_dict_comp = {company.Name : company.Code for idx, company in stocks_df.iterrows()}
# {한화우:005885}
predict_data={}

def page2():
    st.header("최고의 주식분석 서비스!!")
    options = st.multiselect(
    "관심 기업을 선택하세요",
    list(company_dict_comp.keys()),
    list(company_dict_comp.keys())[:5],
    )
    # print(type(options))
    # st.write("You selected:", options)

    # 버튼을 누르면
    # 관심기업 리스트를 순차적으로 돌면서 
    # 다음날의 예측값을 리턴한다
    # 이 내용들을 종합해서 dataframe(표 형식)으로 보여준다
    if st.button("분석 시작", type="secondary", use_container_width=True ):
        for company_code in options:
            company_data = get_company_stock_data(company_dict_comp[company_code])
            company_data['Target'] = (company_data['Close'].shift(-1) > company_data['Close']).astype(int)
            company_df = company_data.dropna()
            # 특성과 타겟 분리
            X = company_df.drop('Target', axis=1)
            y = company_df['Target']
            # train test 데이터 분할
            # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            X_train = X.iloc[:-1]
            y_train = y[:-1]
            X_test = X.iloc[[-1]]
            y_test=y[-1]
            classifier=LGBMClassifier()
            classifier.fit(X_train, y_train)
            y_pred = classifier.predict(X_test)
            predict_data[company_code]=int(y_pred)
        df1 = pd.DataFrame(predict_data.items(), columns=['기업명', '예측값'])
        st.write(df1)