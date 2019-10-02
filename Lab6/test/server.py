import socket
import struct
from threading import Thread
import os.path

clients = []

class ClientListener(Thread):
    def __init__(self, sock: socket.socket):
        super().__init__(daemon=True)
        self._sock = sock
 
    def create_file(self, filename):
        if os.path.isfile(filename):
            i = 1
            index = filename.rfind('.')
            new_filename = filename[:index] + "(" + str(i) + ")" + filename[index:]
            while os.path.isfile(new_filename):
                i+=1
                index = filename.rfind('.')
                new_filename = filename[:index] + "(" + str(i) + ")" + filename[index:]
            filename = new_filename
        f = open(filename, 'wb')
        return f

    def recv_msg(self):
        raw_msglen = self.recvall(4)
        if not raw_msglen:
            return None
        msglen = struct.unpack('>I', raw_msglen)[0]
        filename = self.recvall(msglen).decode()
        f = self.create_file(filename)
        raw_msglen = self.recvall(4)
        if not raw_msglen:
            return None
        msglen = struct.unpack('>I', raw_msglen)[0]
        reclen = 0
        while reclen < msglen:
            f.write(self.recvall(1024))
            reclen += 1024
        f.close()

    def recvall(self, n):
        data = b''
        while len(data) < n:
            packet = self._sock.recv(n - len(data))
            if not packet:
                return data
            data += packet
        return data
    
    def run(self):
        self.recv_msg()
    


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', 8800))
    sock.listen()
    while True:
        con, addr = sock.accept()
        clients.append(con)
        ClientListener(con).start()