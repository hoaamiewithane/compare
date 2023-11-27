import pandas as pd
import json
from map_column import LOOKER_TO_COGNOS


def map_looker_to_cognos(df, mapping):
    return df.rename(columns=mapping)


try:
    cognos_columns_to_drop = ['Lease Start Year', 'Lease End Year']
    cognos_excel = pd.read_excel('Special cargo fleet-Cognos2.xlsx',
                                 usecols=lambda col: col not in cognos_columns_to_drop)
    looker_columns_to_drop = ['Lease Effective Start Year', 'Lease Effective End Year',
                              'Build Down Fiscal Year Quarter']
    looker_excel = pd.read_excel('Special cargo fleet-Looker2.xlsx',
                                 usecols=lambda col: col not in looker_columns_to_drop)
    looker_excel_mapped = map_looker_to_cognos(looker_excel, LOOKER_TO_COGNOS)

    cognos_json_str = cognos_excel.to_json(orient='records')
    looker_json_str = looker_excel_mapped.to_json(orient='records')
    cognos_json = json.loads(cognos_json_str)
    looker_json = json.loads(looker_json_str)

    with open('cognos.json', 'w') as cognos_file:
        json.dump(cognos_json, cognos_file, indent=4)

    with open('looker.json', 'w') as looker_file:
        json.dump(looker_json, looker_file, indent=4)

    min_length = min(len(cognos_json), len(looker_json))
    looker_to_cognos_values = list(LOOKER_TO_COGNOS.values())
    for i in looker_to_cognos_values:
        count = 0
        for j in range(min_length):
            if cognos_json[j][i] == looker_json[j][i]:
                count = count + 1
        print('% match of ', i, ': ', count)

except Exception as e:
    print("Đã xảy ra lỗi:", str(e))
