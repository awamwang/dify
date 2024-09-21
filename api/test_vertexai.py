# Drawn from https://cloud.google.com/vertex-ai/docs/generative-ai/migrate/migrate-palm-to-gemini
import json
import os

import vertexai
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from vertexai.preview.generative_models import GenerativeModel

load_dotenv()

PROJECT = "..."
LOCATION = "us-central1"

# Import credentials 
service_account_json_string = os.getenv('GCP_SERVICE_ACCOUNT_JSON')
service_account_info = json.loads(service_account_json_string)
google_credentials = Credentials.from_service_account_info(service_account_info)


# Initialize Vertex AI
vertexai.init(project=PROJECT, location=LOCATION, credentials=google_credentials)

# Start prediction
model = GenerativeModel("gemini-pro")

responses = model.generate_content("The sun's colour is ", stream=True)

for response in responses:
    print(response.text)