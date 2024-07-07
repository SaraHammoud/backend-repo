import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

run_localhost = config['run_localhost']

class Server:
    def __init__(self):
        self.run_localhost = run_localhost

    def start(self):
        if self.run_localhost:
            print("Error: Running on localhost is not allowed.")
        else:
            print("Server starting...")

if __name__ == "__main__":
    server = Server()
    server.start()
