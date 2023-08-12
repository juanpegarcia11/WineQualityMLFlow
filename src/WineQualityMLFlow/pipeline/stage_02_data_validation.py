from WineQualityMLFlow.config.configuration import ConfigurationManager
from WineQualityMLFlow.components.data_validation import DataValidation
from WineQualityMLFlow import logger

STAGE_NAME = "Data Validation Stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        logger.info(f">>>>>> Stage {STAGE_NAME} executing... <<<<<<")
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed! <<<<<<")
        logger.info("\n=========================")
    except Exception as e:
        logger.exception(e)
        raise e
    