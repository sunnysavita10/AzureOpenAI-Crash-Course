import json
import requests
import openai
from openai import AzureOpenAI
import os

def main():
#creating an Azure OpenAI client

 apikey="00a48b1e132c435c94e4e28536047e76"
 endpoint="https://myaudiototranscript.openai.azure.com/"

 client = AzureOpenAI(
  azure_endpoint = endpoint, 
  api_key=apikey,  
  api_version="2024-02-01"
 )


 functions=[
        {
            "name":"getWeather",
            "description":"Retrieve real-time weather information/data about a particular location/place",
            "parameters":{
                "type":"object",
                "properties":{
                    "location":{
                        "type":"string",
                        "description":"the exact location whose real-time weather is to be determined",
                    },
                    
                },
                "required":["location"]
            },
        }
    ] 


 initial_response = client.chat.completions.create(
    model="chatmodel", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "you are an assistant that helps people retrieve real-time weather data/info"},
        {"role": "user", "content": "How is the weather in bhopal?"}
    ],
   functions=functions
 )

 function_argument = json.loads(initial_response.choices[0].message.function_call.arguments)
 location= function_argument['location']
 if(location):
    print(f"city: {location}")
    get_weather(location)

def get_weather(location):
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + location  + "&appid=9714c902c784730338c95bd3140cc6ed"
    response=requests.get(url)
    get_response=response.json()
    latitude=get_response['coord']['lat']
    longitude = get_response['coord']['lon']
    print(f"latitude: {latitude}")
    print(f"longitude: {longitude}")

    url_final ="https://api.openweathermap.org/data/2.5/weather?lat="+ str(latitude) + "&lon=" + str(longitude) + "&appid=9714c902c784730338c95bd3140cc6ed"
    final_response = requests.get(url_final)
    final_response_json = final_response.json()
    weather=final_response_json['weather'][0]['description']
    print(f"weather condition: {weather}")

if __name__ == "__main__":
    main()
    
