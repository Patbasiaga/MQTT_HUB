class PLC_CONFIG:
    IP = "192.168.0.1"
    RACK = 0
    SLOT = 1


#class MQTT_CONFIG:
#    MQTT_SERVER_ADDRESS = 'mqtt.flespi.io'
##    USERNAME = "el30F7IQyOctoTGHNAYGv8YO9eYkvCezO5oh3UXryXILFciiA6OV3Dy0Fka0Meoo"
 #   PASSWORD = ""
 #   TOPICS = ["HUB_001", "HUB_002", "Live_Bit"]

class MQTT_CONFIG_SERVER:
    IP_ADDRESS = '10.121.18.67'
    USERNAME = "patryk"
    PASSWORD = "patryk"
    TOPICS = ["REAKTO/HUB001/HEARTBEAT", "PING", "MIRROR", 'REAKTO/telemetry/drone1']


class MQTT_CONFIG_CLIENT:
    IP_ADDRESS = "10.121.18.29"
    DEVICE_TYPE = "HUB"
    DEVICE_ID = "001"
    DEVICE_NAME = "HUB_001"
    DEVICE_IP = "10.121.18.29"


class WRITE_FILE_CONFIG:
    #MESSAGE_LOG_PATH = r"C:\Users\Patryk\Desktop\PycharmProjects\Python\MQTT\venv\Logs"
    #CONNECTION_LOG_PATH = r"C:\Users\Patryk\Desktop\PycharmProjects\Python\MQTT\venv\Logs"
    MESSAGE_LOG_PATH = r"/app"
    CONNECTION_LOG_PATH = r"/app"
