import socket
import select
import queue
conn_list = []
def broadcast(conn,data):
    for sockets in conn_list:
        if sockets != s and sockets != conn:
            sockets.sendall(data.encode())

def single_client(data,write):
    data1 = data.split()
    for sockets in mydict.keys():
        if data1[3] == sockets:
            if mydict[sockets][0] in write :
                mydict[sockets][0].sendall(data.encode())

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("",1234))
    s.listen(5)
    s.setblocking(False)
    mydict = {}
    mydict['server'] = {s,('127.0.0.1',1234)}
    while True:
        read,write,error = select.select([s] + conn_list,conn_list,[])
        for sockets in read:
            if sockets == s:
                conn, addr = s.accept()
                name = conn.recv(56).decode()
                print("got (%s, %s) conn" % addr)
                conn_list.append(conn)
                mydict[name] = (conn,addr)
            else:
                try:
                    data  = sockets.recv(1024).decode()
                    if data != 'quit' and data.split()[3] not in mydict.keys():
                        broadcast(sockets,data)
                    elif data != 'quit' and data.split()[3] in mydict.keys() :
                        single_client(data,write)
                except:
                    conn_list.remove(sockets)
                    continue
    s.close()
