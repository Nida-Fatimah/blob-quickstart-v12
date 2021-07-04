import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

from azure.storage.blob import BlobServiceClient
connection_string = "DefaultEndpointsProtocol=https;AccountName=practise1;AccountKey=5PJdi6BWSCsV0KIiAAfzYjvvLd9StuKyH6vluTaPkH5r8PU9mGzrKvneLwFHOvcbegbG/7qC0IK4QhAEjVsUUQ==;EndpointSuffix=core.windows.net"
service = BlobServiceClient.from_connection_string(conn_str=connection_string)

from azure.storage.blob import ContainerClient
container_client = ContainerClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=practise1;AccountKey=5PJdi6BWSCsV0KIiAAfzYjvvLd9StuKyH6vluTaPkH5r8PU9mGzrKvneLwFHOvcbegbG/7qC0IK4QhAEjVsUUQ==;EndpointSuffix=core.windows.net", container_name="mycontainer1")
container_client.create_container()

from azure.storage.blob import BlobClient
blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=practise1;AccountKey=5PJdi6BWSCsV0KIiAAfzYjvvLd9StuKyH6vluTaPkH5r8PU9mGzrKvneLwFHOvcbegbG/7qC0IK4QhAEjVsUUQ==;EndpointSuffix=core.windows.net", container_name="mycontainer1", blob_name="myblob1")

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
    print("Established connection to azure storage account")
    print("Created a new container")
    print("Created a new blob inside the container")

    # Quick start code goes here

except Exception as ex:
    print('Exception:')
    print(ex)
    