import pandas as pd
import numpy as np
import datacompy
import os

from header_column import COGNOS_TO_LOOKER,LOOKER_TO_COGNOS

# hàm bỏ bớt cột
def drop_columns(df, columns_to_drop):
    df = df.drop(columns=columns_to_drop)
    return df

def check_columns_combination_uniqueness(df_cognos, df_looker, columns_to_check):
    def combine_columns(df):
        return df[columns_to_check].apply(lambda x: '-'.join(x.astype(str).str.upper()), axis=1)
    df_cognos_combined = combine_columns(df_cognos)
    df_looker_combined = combine_columns(df_looker)
    are_columns_combined_unique = df_cognos_combined.is_unique and df_looker_combined.is_unique
    if are_columns_combined_unique:
        result = "Danh sách các cột được chọn ---CÓ--- tạo ra một tổ hợp khóa duy nhất để so sánh hai DataFrame."
    else:
        result = "Danh sách các cột được chọn ---KHÔNG--- tạo ra một tổ hợp khóa duy nhất để so sánh hai DataFrame."
    return result

df_cognos = pd.read_excel(r"C:\Users\hoa.nd\Desktop\WAP\compare\new-compare\Special cargo fleet-Cognos2.xlsx", dtype=str)
df_looker = pd.read_excel(r"C:\Users\hoa.nd\Desktop\WAP\compare\new-compare\Special cargo fleet-Looker2.xlsx", dtype=str)

columns_to_drop_cognos = ['Lease Start Year','Lease End Year']
df_cognos = drop_columns(df_cognos, columns_to_drop_cognos)

columns_to_drop = ['Lease Effective Start Year','Lease Effective End Year','Build Down Fiscal Year Quarter']
df_looker = drop_columns(df_looker, columns_to_drop)

df_cognos= df_cognos.reindex(columns=['MST Parent Company Code','Term Code', 'Lessor Name',
    'Contract No.', 'AGMT No.', 'TP/SZ Code',
    'Per diem', 'Sublease per diem',
    'Total per diem', 'On-Hire Date', 'Lease Start Date',
    'Lease Start Month', 'Lease End Date',
    'Lease End Month', 'Expiry Year (Build Down)',
    'Min Binding Period Date (From)', 'Min Binding Period Date (To)',
    'Container No.', 'Year Build Date', 'Reefer Maker',
    'Model No.'])

df_cognos = df_cognos.rename(columns=COGNOS_TO_LOOKER)

for column in df_cognos.columns:
    if df_looker[column].dtype == 'object':
            df_looker[column].fillna("No_data", inplace=True)
            df_cognos[column].fillna("No_data", inplace=True)
    if df_looker[column].dtype == 'datetime64[ns]':
        df_cognos[column] = df_cognos.apply(lambda row:
            pd.Timestamp(row[column]).round('S'), axis=1)
        df_looker[column] = df_looker.apply(lambda row:
            pd.Timestamp(row[column]).round('S'), axis=1)
        df_looker[column].fillna(0, inplace=True)
        df_cognos[column].fillna(0, inplace=True)
    if df_looker[column].dtype == 'float64' or df_looker[column].dtype == 'int64':
        df_looker[column].fillna(0, inplace=True)
        df_cognos[column].fillna(0, inplace=True)


# not_keys= ['Parent Company Code', 'Lease Term Code', 'Lessor Name',
#        'Contract Number', 'Agreement Number', 'EQ Type Size Code',
#        'Rates - Per Diem', 'Rates - Sublease Per Diem',
#        'Rates - Total Per Diem', 'On Hire Date', 'Lease Effective Start Date',
#        'Lease Effective Start Calendar Year Month', 'Lease Effective End Date',
#        'Lease Effective End Calendar Year Month', 'Build Down Fiscal Year',
#        'Minimum Binding Period From Date', 'Minimum Binding Period To Date',
#        'Container Number', 'EQ Manufacture Date', 'Reefer Maker',
#        'Reefer Model Number']
df_looker.columns
# LOOKER_COLUMNS=[]
# not_keys= []

# keys_list = [x for x in LOOKER_COLUMNS if x not in not_keys]


# compare = datacompy.Compare(
#     df_cognos, df_looker, 
#     join_columns=keys_list, df1_name='Cognos', df2_name='Looker')
# print(compare.report())



# result = check_columns_combination_uniqueness(df_cognos, df_looker, columns_to_check)
# print(result)