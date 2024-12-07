from src.mlproject.logger import logging
from src.mlproject.exception import CustomExeption
import sys
import os
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv('password')
db=os.getenv("db")

def read_sql_data():
    logging.info("reading mysql startted")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            passwd=password,
            db=db
        )
        logging.info("connection established ",mydb)
        df=pd.read_sql_query("select * from student",mydb)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomExeption(ex,sys)
        
    
    
    