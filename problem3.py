# Python 3.8
# Dependencies [openpyxl,pandas,json]
import json

import pandas as pd

try:
    #Reading .xlsx file
    excel_df = pd.read_excel('3_Products.xlsx')
    if excel_df.empty:
        print("No Data in XLSX file")
    else:
        #converting data to json
        json_data = excel_df.to_json(orient='records')
        #loading json to Dictionary
        file_json_dict = json.loads(json_data)
        #Creating the .json file in directory
        with open('3_Products_output.json', 'w') as jsonFile:
            json.dump(file_json_dict, jsonFile)

except:
    print("Error Found : Data is not properly formatted or  File not found")
else:
    print("XLSX File Coverted to JSON Sucessfully")
