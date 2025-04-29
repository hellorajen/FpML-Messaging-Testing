import socket
import xml.etree.ElementTree as ET
from datetime import datetime

class FpMLServer:
    def __init__(self, host='0.0.0.0', port=6000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(1)
        
    def log_message(self, msg):
        with open("fpml_messages.log", "a") as f:
            f.write(f"{datetime.now()} | {msg}\n")
    
    def validate_fpml(self, xml_str):
        try:
            ET.fromstring(xml_str)  # Basic XML validation
            return True
        except ET.ParseError:
            return False

    def start(self):
        print("FpML Server listening on port 6000...")
        conn, addr = self.sock.accept()
        
        with conn:
            print(f"Connected to {addr}")
            while True:
                data = conn.recv(4096).decode('utf-8')
                if not data:
                    break
                
                if self.validate_fpml(data):
                    print(f"Valid FpML:\n{data[:200]}...")  # Print first 200 chars
                    self.log_message(data)
                    conn.sendall(b"ACK") 
                else:
                    conn.sendall(b"NAK")

if __name__ == "__main__":
    server = FpMLServer()
    server.start()