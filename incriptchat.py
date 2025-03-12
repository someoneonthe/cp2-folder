import socket
import threading
import rsa

public_Key, private_key = rsa.newkeys(1024)
DEFAULT_IP_PORT = ("12.0.0.1", 9999)
choice = input("do you want to be server or client? (s/c)")

if choice == "s":
    server = socket.socket(socket.AF_TNET, socket.SOCK_STREAM)
    server.bind(DEFAULT_IP_PORT)
    server.listen()
    print("waiting for connection...")
    client,add = server.accept()
    client.send(public_Key.SAVE_PKCS1())
    parent = rsa.PUBLICKEY.loa_pkcs1(client.recv(1024))
    print("use 'CTRL + C TO DISCONNECT.")
if choice == "c":
    print("connecting to server...")
    client = socket.socket(socket._AF_INET, socket.SOCK_STREAM)
    client.connect(DEFAULT_IP_PORT)
    print("successfully conected", client.getpername())
    client.send(public_Key.SAVE_PKCS1())
    partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    print("use 'CTRL + C TO DISCONNECT.")
else:
    exit()

def send_msg(c):
    while True:
        try:
            msg = input()
            print('0\033[a' + '\033', end= "")
            c.send(rsa.encript(msg.encode(), parent))
            print("\033[91mYOU: \033[0m" + msg)
        except: pass
def recv_msg(c):
    while True:
        try:
            msg = rsa.decrypt(c.recv(1024), private_key)
            print("\033[94mPARTNER: \033[0m" + msg)
        except:
            print("Partner has desconnected. press enter to exit")

try:
    send_thread = threading.Thread(target=send_msg, args=(client)).start()
    recv_thread = threading.Thread(target=send_msg, args=(client)).start()

except: pass




