import socket
import threading

def client_recv():

    while True:
        data = s.recv(1024)
        if data == 'quit':
            print(" Connection terminated by server ..")
            break
        else :
            print(" "*30 + data.decode())
    s.close()



def client_send(user):

    while True:
        data  = input()
        if data == 'quit':
            print("Terminating conn by user .. ")
            s.close()
        else:
            data = f"from {user} : "+ data
            s.send(data.encode())


if __name__ == "__main__":

    #creating socket for connection
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    user = input("Enter your name : ")

    host = input("Enter host to connect to : ")
    port = input("Enter port for conn .. :")

    #connecting now to host
    s.connect_ex((host,int(port)))
    s.sendall(user.encode())
    #creating threads
    t1 = threading.Thread(target=client_recv)
    t2 = threading.Thread(target=client_send,args=(user,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
