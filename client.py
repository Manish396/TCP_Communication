import socket
import time
import random

port = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(),port))

# Sends the request to Server
def send(message):
    print("Sending "+ message +" to Server")
    message =  message.encode()
    client.sendto(message,(socket.gethostname(),port))


if __name__ == '__main__':
    try:
        while True:
            temperature = random.randint(1,50)
            humidity = random.randint(0,100)
            message = str(temperature)+","+str(humidity)
            send(message)
            time.sleep(1)
    except:
        print("\nStopped Sending requests to Server...")
