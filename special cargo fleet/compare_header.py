import pandas as pd

try:
    cognos_headers = pd.read_excel('Special cargo fleet-Cognos2.xlsx', header=None).iloc[0]
    looker_headers = pd.read_excel('Special cargo fleet-Looker2.xlsx', header=None).iloc[0]

    print(len(cognos_headers))
    print('=============')
    print(len(looker_headers))

except Exception as e:
    print("Đã xảy ra lỗi:", str(e))
