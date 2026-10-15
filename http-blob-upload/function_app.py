import json
import os
import traceback

import azure.functions as func
from azure.storage.blob import BlobServiceClient

AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=rg1blob1store;AccountKey=i6DKuonR030PSMSZBcdMCvq1PF0tCjH+9saunTLPHoj6TsmddZ14uZGiCMxjqX2q01DNOwCblewE+AStmqy7oQ==;EndpointSuffix=core.windows.net"
AZURE_STORAGE_CONTAINER_NAME = "container-spikeblob-test"
BLOB_NAME = "example.txt"

app = func.FunctionApp()

@app.route(route="upload", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def test_blob(req: func.HttpRequest) -> func.HttpResponse:

    try:
        content = "Data content to save to blob"

        blob_service_account = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
        container_name = AZURE_STORAGE_CONTAINER_NAME

        blob_client = blob_service_account.get_blob_client(container=container_name, blob=BLOB_NAME)

        blob_client.upload_blob(data=content, overwrite=True)

        return func.HttpResponse(
            f"Successfully wrote {BLOB_NAME} to {container_name}",
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        error_details = traceback.format_exc()

        return func.HttpResponse(
            body=(
                f"FAILED\n\n"
                f"Error: {str(e)}\n\n"
                f"Stack trace:\n{error_details}"
            ),
            status_code=200
        )

