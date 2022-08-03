import text_file_writer
import config
import socket
from datetime import datetime as timer


class CommunicationStatus:
    def __init__(self):
        self.write_file = text_file_writer.TextFileWriter()
        self.write_path = config.WRITE_FILE_CONFIG.CONNECTION_LOG_PATH
        self.message = {}

    def create_log_message(self, status, rc_code):
        current_time = timer.now().strftime("%H:%M:%S")
        self.message = {
            'brooker_ip_address': '10.121.18.29',
            'user_name': config.MQTT_CONFIG_CLIENT.DEVICE_TYPE,
            'client_ip_address': socket.gethostbyname(socket.gethostname()),
            'device_type': config.MQTT_CONFIG_CLIENT.DEVICE_NAME,
            'device_id': config.MQTT_CONFIG_CLIENT.DEVICE_IP,
            'timestamp': current_time,
            'status': status,
            'rc_code': rc_code
        }

    def log_in_status(self, status, rc_code):
        self.create_log_message(status, rc_code)
        self.write_file.handle_writing_to_file(self.write_path, 'ConnectionLog', 'a', self.message)


