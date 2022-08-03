import paho.mqtt.client as mqtt
import config
import json
import communication_status
import message_handler_ping


class MQTT:

    TOPICS = config.MQTT_CONFIG_SERVER.TOPICS
    PASSWORD = config.MQTT_CONFIG_SERVER.PASSWORD
    USERNAME = config.MQTT_CONFIG_SERVER.USERNAME
    MQTT_SERVER_ADDRESS = config.MQTT_CONFIG_SERVER.IP_ADDRESS

    def __init__(self):
        self.mqtt_client = mqtt.Client()
        self.json_message = ''
        self.converted_message = {}
        self.topic = ''
        self.is_connected = False
        self.received = False
        self.communication = communication_status.CommunicationStatus()

    def on_connect(self, client, userdata, flags, rc):
        for topic in MQTT.TOPICS:
            self.mqtt_subscribe(topic)
        print("Connected with result code " + str(rc))
     #   self.communication.log_in_status(status='Connected', rc_code=rc)

    def on_disconnect(self, client, userdata, rc):
        print("Disconnected from MQTT server with code: %s" % rc)
        self.disconnect_mqtt()
     #   self.communication.log_in_status(status='Disconnected', rc_code=rc)
        self.is_connected = False

    def on_message(self, client, userdata, msg):
        print(f"Received '{msg.payload.decode('utf-8')}' from '{msg.topic}' topic")
        self.topic = msg.topic
        self.received = True
        self.json_message = msg.payload.decode('utf-8')
        self.converted_message = json.loads(self.json_message)
        self.handle_the_right_topic()

    def connect_mqtt(self):
        self.disconnect_mqtt()
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.on_message = self.on_message
        try:
            print("connecting to mqtt server " + str(MQTT.MQTT_SERVER_ADDRESS))
            self.mqtt_client.username_pw_set(MQTT.USERNAME, MQTT.PASSWORD)
            self.mqtt_client.connect(MQTT.MQTT_SERVER_ADDRESS, 1883, 2)
            self.mqtt_client.loop_start()
            self.is_connected = True

        except Exception:
            print("Unable to connect to MQTT server" + str(MQTT.MQTT_SERVER_ADDRESS))

    def disconnect_mqtt(self):
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()

    def mqtt_publish(self, topic, msg):
        self.mqtt_client.publish(topic, msg)
        print(f'Successful published {msg} to {topic}')

    def mqtt_subscribe(self, topic):
        self.mqtt_client.subscribe(topic)
        print(topic)

    def message_received(self):
        if self.received:
            self.received = False
            return True

    def handle_the_right_topic(self):
        pass


