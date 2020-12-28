from socket import socket, AF_INET, SOCK_DGRAM
def main():
    s=socket(AF_INET,SOCK_DGRAM)
    print("UDP SOCKET PROGRAM : CLIENT  ")
    ip='192.168.56.1' #IP address of the Server,
    port=1234 #server port address
    socket_addr=(ip,port)
    request=input("Enter Filename : ") # requesting the filename from user
    s.sendto(bytes(request,'utf-8'),socket_addr) #sending the request to the Server 
    print(f"Request for contents of File : {request} sent to server.")
    response,addr=s.recvfrom(2048) 
    response=response.decode('utf-8')
    if addr == (ip,port) :
        print("-"*10)
        print(f"Contents of file { request } : ")
        print(response)
        print("-"*10)
        print("Content Recieved.")
main()