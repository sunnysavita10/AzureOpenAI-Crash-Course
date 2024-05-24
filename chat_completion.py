import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv

load_dotenv()
#AZURE_OPENAI_API_KEY=os.getenv("AZURE_OPENAI_API_KEY")

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="https://mypractice.openai.azure.com/",
    api_key="7b2f895c6bed4be0870b6fb0c3762ecd"
)

completion = client.chat.completions.create(
    model="chat",
    messages=[
        {
            "role": "user",
            "content": "what is a capital of delhi?",
        }
    ]
)
      
print(completion.to_json())

