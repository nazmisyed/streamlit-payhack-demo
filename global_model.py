import joblib
from azure.storage.blob import BlobServiceClient
import shap
from dotenv import load_dotenv
import os 
import pandas as pd 
from io import StringIO
import xgboost

load_dotenv()

BLOB_CONNECTION_STRING = os.getenv('BLOB_CONNECTION_STRING')
CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")

def global_model():
    # Azure Blob Storage Configuration
    blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob="global_model.pkl")
    blob_client_csv = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob="X_test_global.csv")

    # Download the joblib file from Azure Blob
    with open("global_model.pkl", "wb") as file:
        file.write(blob_client.download_blob().readall())

    # Load the model using joblib
    global_model = joblib.load("global_model.pkl")

    download_stream = blob_client_csv.download_blob()
    csv_data = download_stream.content_as_text()
    X_test = pd.read_csv(StringIO(csv_data))

    # Initialize SHAP Explainer
    explainer = shap.Explainer(global_model)

    # Sample data for explanation (replace with your dataset)
    sample_data = X_test.iloc[:500]  # Example subset from your test data

    # Calculate SHAP values
    shap_values = explainer(sample_data)

    # Azure Blob Storage Configuration
    blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob="global_model.pkl")

    # Download the joblib file from Azure Blob
    with open("global_model.pkl", "wb") as file:
        file.write(blob_client.download_blob().readall())

    # Load the model using joblib
    global_model = joblib.load("global_model.pkl")


    # Initialize SHAP Explainer
    explainer = shap.Explainer(global_model)

    # Sample data for explanation (replace with your dataset)
    sample_data = X_test.iloc[:500]  # Example subset from your test data

    # Calculate SHAP values
    shap_values = explainer(sample_data)


    return shap_values, sample_data, explainer 