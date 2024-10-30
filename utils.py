import FinanceDataReader as fdr
def get_company_stock_data(company_code):
  company_stock = fdr.DataReader(company_code)
  return company_stock