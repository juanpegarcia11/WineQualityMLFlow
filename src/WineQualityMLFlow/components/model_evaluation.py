import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from WineQualityMLFlow.entity.config_entity import ModelEvaluationConfig
from WineQualityMLFlow.utils.common import save_json, create_directories
from pathlib import Path



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        create_directories([self.config.root_dir])
    


    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            
            # Predict and evaluate model metrics
            predicted_qualities = model.predict(test_x)
            rmse, mae, r2 = self.eval_metrics(test_y, predicted_qualities)

            # Saving metrics as local
            scores = {
                "rmse": rmse, 
                "mae": mae,
                "r2": r2
            }
            print(scores)
            save_json(path=Path(self.config.metric_file_name), data= scores)

            # Logging params and metrics into MLFlow
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(scores)

            # Model Registry
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model,"model")