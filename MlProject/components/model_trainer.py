from MlProject.constants import *
from MlProject.logger import logging
from MlProject.exception import CustomException
import os, sys
from MlProject.config.configuration import *
from dataclasses import dataclass
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd
from MlProject.utils import evaluate_model,save_obj

from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

@dataclass
class ModelTrainingConfig:
    trained_model_file_path = MODEL_FILE_PATH

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainingConfig
    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info("\t\t\t Training Pipeline is Started \n")
            X_train , y_train , X_test , y_test = (train_array[:,:-1],train_array[:,-1],
                                                   test_array[:,:-1],test_array[:,-1])
            models = {
                "XGBRegressor" : XGBRegressor(),
                "DecisionTreeRegressor" : DecisionTreeRegressor(),
                "SVR" : SVR(),
                "RandomForestRegressor" : RandomForestRegressor(),
                "GradientBoostingRegressor" : GradientBoostingRegressor()
            }
            model_report = evaluate_model(X_train , y_train , X_test , y_test,models)
            logging.info(f"\t\t\t Training Report is : {model_report}\n")
            best_model_name = max(model_report, key=model_report.get)
            best_model_score = model_report[best_model_name]
            best_model = models[best_model_name]
            logging.info(f"\t\t\t Out Of All The Models {best_model_name} is the best model withy the r2score of : {best_model_score} \n")
            save_obj(file_path=self.model_trainer_config.trained_model_file_path , obj=best_model)
            logging.info("\t\t\t Training Pipeline is Finished \n")


        
        except Exception as e:
            raise CustomException( e,sys)



