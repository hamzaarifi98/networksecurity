from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
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
        print(dataingestionartifact)
       
    except Exception as e:
        raise NetworkSecurityException(e,sys)
                            