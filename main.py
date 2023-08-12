from src.WineQualityMLFlow import logger
from WineQualityMLFlow.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from WineQualityMLFlow.config.configuration import ConfigurationManager

logger.info("Initializing custom logging")

STAGE_NAME = "Data Transformation Stage"
logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
obj = DataTransformationTrainingPipeline()
logger.info(f">>>>>> Stage {STAGE_NAME} executing... <<<<<<")
obj.main()
logger.info(f">>>>>> Stage {STAGE_NAME} completed! <<<<<<")
logger.info("\n=========================")

