from WineQualityMLFlow.config.configuration import ConfigurationManager
from WineQualityMLFlow.components.model_trainer import ModelTrainer
from WineQualityMLFlow import logger

STAGE_NAME = "Model Trainer Stage"


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train_test_spliting()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        logger.info(f">>>>>> Stage {STAGE_NAME} executing... <<<<<<")
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed! <<<<<<")
        logger.info("\n=========================")
    except Exception as e:
        logger.exception(e)
        raise e
    