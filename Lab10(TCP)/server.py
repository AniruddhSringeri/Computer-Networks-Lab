from socket import socket, AF_INET, SOCK_STREAM

s=socket(AF_INET,SOCK_STREAM)
print("TCP SOCKET PROGRAM : SERVER ")

HEADERSIZE=10  #heder length is fixed 
ip='192.168.56.1' #IP address of the Server, can be used by any PC in LAN to connect to this server
port=8000 #port address
s.bind((ip,port))  #specifying the socket to be active at this Socket address
s.listen(4)  #making the server up and running 

print(f"Server is Up , Listening at Port : { port } ")

while True:
    clientsocket, clientaddr= s.accept()  #Accepting the connection request from a client 
    print(f" Client with  {clientaddr} connected.")
    request=clientsocket.recv(1024) #used to recieve data from the client, assuming request is not more than 1024 bytes
    request=request.decode('utf-8')
    print(f"Request for filecontent of file : { request } Recieved. ")
    try:
        with open(request,"r") as fd:
            contents=fd.read()
            print("Request Processed")
    except:
        contents="Request cannot be fullfilled. No file exist."
        print("Request cannot be fullfilled")
    # Data send == {len ...+ contents }
    msg=f"{len(contents):<{HEADERSIZE}}"+contents  # header contains the length of the payload 
    clientsocket.send(bytes(msg,'utf-8')) #used to send data to the client
    print(f"Response Sent to { clientaddr }")
    print("-"*10)