'''


this is a server


'''

import socket
import threading
lockit = threading.Lock()

mydict = {}


# def recv():
#     while True:
#         for user1 in mydict.keys():
#             if len(mydict[user1][0].recv(1024)) > 0:
#                 data = mydict[user1][0].recv(1024).decode()
#                 if data == 'quit':
#                     print(" Connection terminated by server ...")
#                     conn.close()
#                     break
#                 else :
#                     print(" "*30 + data)
#             else:
#                 continue
#     s.close()

def incoming_connections(s):
    while True:
        conn, addr = s.accept()
        name = conn.recv(50).decode()
        print(f" {name} joined chat ... ")
        mydict[name] = (conn,addr)
        t3 = threading.Thread(target=recv,args=(conn,))
        t3.start()


def recv(conn):

    while True:
        data = conn.recv(1024)
        if data == 'quit':
            print(" Connection terminated by server ..")
            break
        else :
            print(" "*30 + data.decode())
    s.close()

def send():
     while True:
        for index,name in enumerate(mydict) :
            print(index,name)
        name = input("Enter a client name to chat with : \n")
        for user1 in mydict.keys():
            if name == user1:
                data = input("Enter data : ")
                if data != 'quit':
                    mydict[name][0].sendto(data.encode(),mydict[name][1])
                else:
                    conn.close()
                    break
            else:
                continue

if __name__ == "__main__":

    #creating socket for connection
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("",1234));
    s.listen(4)
    t1 = threading.Thread(target=incoming_connections, args=(s,))
    t2 = threading.Thread(target=send)


    t1.start()
    t2.start()



