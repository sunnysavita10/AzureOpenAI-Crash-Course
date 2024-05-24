import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv
import requests

load_dotenv()
#AZURE_OPENAI_API_KEY=os.getenv("AZURE_OPENAI_API_KEY")
key="27f9e30ee1b7430cbfc35ed4bd6b494c"
endpoint_url="https://myspeechtotext.openai.azure.com/"
whisper_model="transcript"
chat_model="chat"
region="northcentralus"

final_url = f"{endpoint_url}/openai/deployments/{whisper_model}/audio/transcriptions?api-version=2023-09-01-preview"

headers = {
    "api-key": key,
}

file_path = r"C:\\Users\\sunny\\azureopenai\\voicedata\\voice.mp4"

# Open the file in binary mode and close it after reading
with open(file_path, "rb") as file:
    files = {"file": (os.path.basename(file_path), file, "application/octet-stream")}

    final_response = requests.post(final_url, headers=headers, files=files).json()
    print(final_response)
    
    user_prompt=final_response['text']
    
    client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint=endpoint_url,
    api_key=key
    )

    completion = client.chat.completions.create(
    model=chat_model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_prompt}
    ]
    )
  
    print(completion.choices[0].message.content)

