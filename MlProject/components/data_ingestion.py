from MlProject.constants import *
from MlProject.config.configuration import *
import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from MlProject.logger import logging
from MlProject.exception import CustomException

@dataclass
class DataIngestionConfig:
    train_data_path:str = TRAIN_FILE_PATH
    test_data_path:str = TEST_FILE_PATH
    raw_data_path:str = RAW_FILE_PATH

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def iniitiate_data_ingestion(self):
        try:
            logging.info("Started Data_ingestion Pipeline \n")
            df = pd.read_csv(DATASET_PATH)

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_data_path, index = False)

            train_set, test_set = train_test_split(df, test_size = 0.20, random_state= 42)

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True )
            train_set.to_csv(self.data_ingestion_config.train_data_path, header = True,index=False)

            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path),exist_ok=True )
            test_set.to_csv(self.data_ingestion_config.test_data_path, header = True,index=False)
            logging.info("Data Saved Success in Artifact\data_ingestion \n")

            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException( e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path,test_data_path=obj.iniitiate_data_ingestion()