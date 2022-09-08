# Python 3.8
# Dependencies [openpyxl,pandas,json]


import pandas as pd

try:
    #Reading .txt file
    df = pd.read_json('2_Products.txt')
    if(df.empty):
        print("No Data in txt file")
    else:
        #converting to XLSX
        df.to_excel('2_Products_output.xlsx')
except:
    print("Error Found : Data is not properly formatted or  File not found")
else:
    print("JSON File Coverted to XLSX Sucessfully")
