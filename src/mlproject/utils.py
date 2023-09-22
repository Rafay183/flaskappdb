import pickle
import numpy as np
from src.mlproject.logger import logging
import sys
from src.mlproject.exception import CustomException
import pymysql
import pandas as pd



# host="localhost"
# user="rafayshaikh"
# password="abcd1234"
# db="mydb"

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host="localhost",
            user="root",
            password="abcd1234",
            db="mydb"

        )

        logging.info("connecttion is established",mydb)
        df=pd.read_sql_query("Select * from data",mydb)
        print(df.head())

        return df


    except Exception as ex:
        raise CustomException(ex, sys)
print("utils is executed")



