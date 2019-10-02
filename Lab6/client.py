import socket
import sys
import struct

class ClientPidor():
    def __init__(self, ip, port):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((ip, port))
    
    def send_file(self, filename):
        fn = struct.pack('>I', len(filename)) + filename.encode()
        self._sock.send(fn)
        dlina = ''
        with open(filename, 'rb') as file:
            dlina = len(file.read())

        with open(filename, "rb") as file:
            cursend = 0
            self._sock.send(struct.pack('>I', dlina))
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                self._sock.send(chunk) 
                if (dlina < 1024):
                    print("Sent 100 percent")
                else:
                    cursend+=1024
                    print("Sent %d percent" % (cursend/dlina*100, ))
            

if __name__ == "__main__":
    client = ClientPidor(sys.argv[2], int(sys.argv[3]))
    client.send_file(sys.argv[1])
    