from src.mlproject.logger import logging
from src.mlproject.exception import CustomExeption
import sys
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.utils import read_sql_data
if __name__=="__main__":
    logging.info("The program started")
    try:
        data_ingstaion=DataIngestion()
        data_ingstaion.initiate_data_ingestion()
    except Exception as e:
        logging.info("custom exception")
        raise CustomExeption(e,sys)
            
    