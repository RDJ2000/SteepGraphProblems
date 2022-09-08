# Python 3.8
# Dependencies [openpyxl,pandas,pyodbc,sqlalchemy]
#Note ODBC DSN is added through controlpanel
#I Backed up DB named "problem4output.bak" as an output ,you can restore bak in

from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.engine import URL

import concurrent.futures

#Reading XLSX file
def read_from_xlsx():
    try:
        excel_df = pd.read_excel('4_Products.xlsx')
        print("XLSX file reading is complete")
        return excel_df
    except:
        print("Error Found : Data is not properly formatted or  File not found")


# Establishing Connection with DB
def create_db_conn():
    try:
        db_dsn = "DSN=DemoServer;Trusted_Connection=yes;"
        db_url = URL.create("mssql+pyodbc", query={"odbc_connect": db_dsn})
        engine = create_engine(db_url)
        print("DB Connected Successfully")
        return engine
    except:
        print("Error in Connecting Database")


# XLXS to MSSQL DB Conversion
def data_conversion_xlsx2mssql(excel_df, engine):
    try:
        excel_df.to_sql('products', con=engine)
    except:
        print("Error in loading from XLSX to MSSQL DB: Maybe Table with same name already exist")
    else:
        print("XLSX File loaded to MSSQL Sucessfully")


if __name__ == "__main__":
    # creating Concurrency

    with concurrent.futures.ThreadPoolExecutor() as executor:
        read_xlsx = executor.submit(read_from_xlsx)
        df = read_xlsx.result()
        connect_db = executor.submit(create_db_conn)
        db_engine = connect_db.result()
        if (read_xlsx.done() and connect_db.done()):
            data_conversion_xlsx2mssql(df, db_engine)
