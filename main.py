from src.WineQualityMLFlow import logger
from WineQualityMLFlow.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from WineQualityMLFlow.config.configuration import ConfigurationManager

logger.info("Initializing custom logging")

STAGE_NAME = "Data Validation Stage"
logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<\n")
obj = DataValidationTrainingPipeline()
logger.info(f">>>>>> Stage {STAGE_NAME} executing... <<<<<<\n")
obj.main()
logger.info(f">>>>>> Stage {STAGE_NAME} completed! <<<<<<\n=========================\n")

