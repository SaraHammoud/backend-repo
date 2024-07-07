import configparser

config = configparser.ConfigParser()
config.read('config.ini')

server_ip = config['DEFAULT']['ServerIPAddress']

class Server:
    def __init__(self):
        self.server_ip = server_ip

    def start(self):
        print(f"Server starting at {self.server_ip}")

if __name__ == "__main__":
    server = Server()
    server.start()
