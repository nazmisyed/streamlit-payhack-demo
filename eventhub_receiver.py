import asyncio
import csv 
import time 
import json 
import os 
from dotenv import load_dotenv

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient

load_dotenv()

EVENT_HUB_CONNECTION_STR = os.environ['EVENT_HUB_CONNECTION_STR']
EVENT_HUB_NAME = os.environ['EVENT_HUB_NAME']

async def run(email):
    producer = EventHubProducerClient.from_connection_string(
            conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name=EVENT_HUB_NAME
        )
    
    email_struct = {"email" : email, "is_fraud" : "1"}
    async with producer:
        json_message = json.dumps(email_struct)
        event_data = EventData(json_message)

        try:
            await producer.send_batch([event_data])
            print("Send succeeded")

            time.sleep(2)
        
        except Exception as e:
            print("Send failed: {e}")
