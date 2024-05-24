# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv

load_dotenv()
AZURE_OPENAI_API_KEY=os.getenv("AZURE_OPENAI_API_KEY")

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="https://youtubecommunity.openai.azure.com/",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

result = client.images.generate(
    model="Dalle3", # the name of your DALL-E 3 deployment
    prompt="give me closeup image of fish who is dancing in water.",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']

print(image_url)
