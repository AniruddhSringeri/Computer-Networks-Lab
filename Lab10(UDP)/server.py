from socket import socket, AF_INET, SOCK_DGRAM

s=socket(AF_INET,SOCK_DGRAM)
print("UDP SOCKET PROGRAM : SERVER ")

ip='192.168.56.1' #IP address of the Server, can be used by any PC in LAN to discover this server
port=1234 #port address
s.bind((ip,port))  #specifying the socket to be active at this Socket address 
#making the server up and running 

print(f"Server is Up and Listening at Port : { port } ")

while True:
     
    requestmsg,clientaddr=s.recvfrom(1024) #buffer size is 1024 
    #used to recieve data from the client, assuming request is not more than 1024 bytes
    request=requestmsg.decode('utf-8')
    print(f"Request for filecontent of file : { request } Recieved. ")
    try:
        with open(request,"r") as fd:
            contents=fd.read()
            print("Request Processed")
    except KeyboardInterrupt:
        contents="Request cannot be fullfilled. No file exist."
        print("Request cannot be fullfilled")
    msg=contents  
    s.sendto(bytes(msg,'utf-8'),clientaddr) #used to send data to the client
    print(f"Response Sent to { clientaddr }")
    print("-"*10)