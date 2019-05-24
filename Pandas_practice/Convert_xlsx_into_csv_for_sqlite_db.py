import pandas as pd
data_xls = pd.read_excel('Tabel_with_60000_vacancies.xlsx', 'Sheet 1', index_col=None)
data_xls.to_csv('csvfile.csv', encoding='utf-8')

#Can be problem with name of sheet (Try to Sheet1, Sheet 1 or look your sheet name)
