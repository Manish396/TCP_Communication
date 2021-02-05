import socket
import sys
import csv
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding socket at localhost and port
def socket_binding():
    try:
        s.bind((socket.gethostname(), port))
        print("socket binded to port: " + str(port))
        listen_socket()
    except socket.error as msg:
        print("socket creation error " + str(msg) + "\n" + "Retrying....")
        socket_binding()
        
#listening socket
def listen_socket():
    try:
        s.listen(5)
        print("Socket is listening....")
        conn, address = s.accept();
        print("Got connection from " + str(address[0]) + " at port " + str(address[1]))
        receive_data(conn)
        conn.close()
    except socket.error as msg:
        print("socket listening error " + str(msg))
        
#Recieve data from client and store it to my.csv file
def receive_data(conn):
    with open('my.csv','w') as obj:
        writer = csv.writer(obj)
        fieldnames = ['Temperature', 'Humidity']
        writer.writerow(fieldnames)
        while True:
            message = conn.recv(1024).decode('utf-8')
            data = message.split(",")
            print(data)
            writer.writerow(data);
    obj.close()
    
#main starts here
if __name__ == '__main__':
    try:
        socket_binding()
    except:
        print("\nSocket binding failed\n")
    finally:
        s.close()
