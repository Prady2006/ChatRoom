import socket
import threading

def client_recv():

    while True:
        data = s.recv(1024)
        try:
            if data == 'quit':
                print(" Connection terminated by server ..")
                break
            else :
                print(" "*30 + data.decode())
        except:
            print("receiving  error ... ")
    s.close()

def client_send(user):

    while True:
        try:
            data  = input()
            if data == 'quit':
                print("Terminating conn by user .. ")
                s.close()
            else:
                data = f"from {user} : "+ data
                s.send(data.encode())
        except:
            print("sending error ... ")

if __name__ == "__main__":

    #creating socket for connection
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    user = input("Enter your name : ")

    # host = input("Enter host to connect to : ")
    # port = input("Enter port for conn .. :")

    #connecting now to host
    # s.connect_ex((host,int(port)))
    s.connect_ex(('127.0.0.1',1234))
    s.sendall(user.encode())
    #creating threads
    try:
        t1 = threading.Thread(target=client_recv)
        t2 = threading.Thread(target=client_send,args=(user,))
        t1.start()
        t2.start()
    except:
        print("error in threads ... ")
    finally:
        t1.join()
        t2.join()
