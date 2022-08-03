import config
import json
import text_file_writer
import message_handler
from datetime import datetime as timer


class MessageHandlerHeartbeat:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client
        self.message_handler = message_handler.MessageHandler(self.mqtt_client)
        self.message = {}
        self.message_json = ''

    def is_valid_message(self):
        if(self.mqtt_client.topic == 'HEARTBEAT' and self.message_handler.is_message_for_this_device() and
                self.mqtt_client.converted_message["frame_type"] == "0"):
            print("HEARTBEAT Received")

    def create_message(self):
        current_time = timer.now().strftime("%H:%M:%S")
        self.message = {
            'frame_type': '0',
            'device_type': config.MQTT_CONFIG_CLIENT.DEVICE_TYPE,
            'device_id': config.MQTT_CONFIG_CLIENT.DEVICE_ID,
            'device_name': config.MQTT_CONFIG_CLIENT.DEVICE_NAME,
            'device_IP': config.MQTT_CONFIG_CLIENT.IP_ADDRESS,
            'timestamp': current_time,
           }
        self.message_json = json.dumps(self.message)

    def send_message(self):
        print(self.message_json)
        self.mqtt_client.mqtt_publish("REAKTO/HUB001/HEARTBEAT", self.message_json)

    def clear_message(self):
        self.message = {}
        self.message_json = ''

    def process_message(self):
         self.clear_message()
         self.create_message()
         self.send_message()