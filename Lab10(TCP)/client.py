# Client Side program for TCP Socket communication 
from socket import socket, AF_INET, SOCK_STREAM
def main():
    s=socket(AF_INET,SOCK_STREAM)
    print("TCP SOCKET PROGRAM : CLIENT  ")

    HEADERSIZE=10  #header length is fixed 
    ip='192.168.56.1' #IP address of the Server,
    port=5243 #server port address
    s.connect((ip,port))  #Connecting to the server 
    print("Client Connected to the server ")
    request=input("Enter Filename : ") # requesting the filename from user
    s.send(bytes(request,'utf-8')) #sending the request to the Server 
    print(f"Request for contents of File : {request} sent.")
    new_msg=True
    fullmsg=''
    while True:   #Used as buffer size might be less than the payload 
        response=s.recv(50)  #client buffer is 50 bytes long ....
        response=response.decode('utf-8')
        if new_msg:
            msglen= int(response[:HEADERSIZE])  #header contains the length of the Payload
            new_msg=False
        fullmsg+=response
        if len(fullmsg)-HEADERSIZE == msglen : #checking whether full messsage is recieved or not 
            print("-"*10)
            print(f"Contents of file { request } : ")
            print(fullmsg[HEADERSIZE:])
            print("-"*10)
            print("Content Recieved.")
            s.close()
            print("Connection Terminated . ")
            break
main()