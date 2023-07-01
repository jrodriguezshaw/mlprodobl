import os
from scrapy import settings
from azure.storage.blob import BlobServiceClient

#CONNECT_STR = settings.get('CONNECT_STR_VAR') 
#CONTAINER_NAME = settings.get('CONTAINER_NAME_VAR') 

CONNECT_STR = "DefaultEndpointsProtocol=https;AccountName=azureworkspace5122300523;AccountKey=syBgKmFWZo1V5lTFRdP0M5RBEN//C715NzT3mIUkTIWF9slf2+GhBpyaS6R/DPaob3dfWfqtV0TH+ASttXbJMQ==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "blob-storage"


blob_service_client = BlobServiceClient.from_connection_string(CONNECT_STR)
container_client = blob_service_client.get_container_client(container=CONTAINER_NAME)


def upload_blob(path, buf):
    container_client.upload_blob(name=path, data=buf.getvalue())


def append_file_to_blob(path):
    with open(path, mode="rb") as data:
        container_client.upload_blob(name=path, data=data, blob_type="AppendBlob")
