import os
import sys
from src.mlproject.exception import CustomExeption
from src.mlproject.logger import logging
import pandas as pd
from dataclasses import dataclass
from src.mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train_data.csv")
    test_data_path: str = os.path.join("artifacts", "test_data.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    
class DataIngestion:
    def __init__(self):        
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        try:
            logging.info("Starting data ingestion process.")
            df = read_sql_data()
            logging.info(f"DataFrame loaded with {df.shape[0]} rows and {df.shape[1]} columns.")

            artifact_dir = os.path.dirname(self.ingestion_config.train_data_path)
            logging.info(f"Creating artifacts directory at: {artifact_dir}")
            os.makedirs(artifact_dir, exist_ok=True)

            logging.info(f"Saving raw data to: {self.ingestion_config.raw_data_path}")
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info(f"Saving train data to: {self.ingestion_config.train_data_path}")
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            logging.info(f"Saving test data to: {self.ingestion_config.test_data_path}")
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion completed successfully.")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            logging.error("Error occurred during data ingestion", exc_info=True)
            raise CustomExeption(e, sys)
