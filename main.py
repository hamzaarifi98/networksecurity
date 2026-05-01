from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
import sys
import os

if __name__=="__main__":
    try:

        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiated the data ingestion component")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Completed the data ingestion component")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Initiated the data validation component")
        data_validation_artifact =data_validation.initiate_data_validation()
        logging.info("Completed the data validation component")
        print(data_validation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)
                            