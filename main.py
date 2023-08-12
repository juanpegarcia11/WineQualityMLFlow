from src.WineQualityMLFlow import logger
from WineQualityMLFlow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from WineQualityMLFlow.config.configuration import ConfigurationManager

logger.info("Initializing custom logging")

STAGE_NAME = "Data Ingestion Stage"
logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<\n")
obj = DataIngestionTrainingPipeline()
logger.info(f">>>>>> Stage {STAGE_NAME} executing... <<<<<<\n")
obj.main()
logger.info(f">>>>>> Stage {STAGE_NAME} completed! <<<<<<\n=========================\n")

