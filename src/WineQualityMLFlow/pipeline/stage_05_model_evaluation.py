import os
from WineQualityMLFlow.config.configuration import ConfigurationManager
from WineQualityMLFlow.components.model_evaluation import ModelEvaluation
from WineQualityMLFlow import logger

STAGE_NAME = "Model Evaluation Stage"


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/juanpegarcia11/WineQualityMLFlow.mlflow"
        os.environ["MLFLOW_TRACKING_USERNAME"]="juanpegarcia11"
        os.environ["MLFLOW_TRACKING_PASSWORD"]="f23bd58860909feaf183020ef3f43ad3c1cef4e7"

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_evaluation_config()
        model_trainer = ModelEvaluation(model_trainer_config)
        model_trainer.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        logger.info(f">>>>>> Stage {STAGE_NAME} executing... <<<<<<")
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed! <<<<<<")
        logger.info("\n=========================")
    except Exception as e:
        logger.exception(e)
        raise e
    