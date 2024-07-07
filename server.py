# import yaml

# with open('config.yaml', 'r') as file:
#     config = yaml.safe_load(file)

# run_localhost = config['run_localhost']

# class Server:
#     def __init__(self):
#         self.run_localhost = run_localhost

#     def start(self):
#         if self.run_localhost:
#             print("Error: Running on localhost is not allowed.")
#         else:
#             print("Server starting...")

# if __name__ == "__main__":
#     server = Server()
#     server.start()
import yaml
import os

config_file = os.path.join(os.path.dirname(__file__), 'C:/Users/user/Desktop/FSW/githubProjects/fullstack-repo/config.yaml')

with open(config_file, 'r') as f:
    config = yaml.safe_load(f)

server_ip = config.get('ip_address')

print(f"Connecting to server at IP address: {server_ip}")

print("test test")