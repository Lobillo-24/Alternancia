import socket
import platform
import subprocess

def obtener_ip():
    ip = socket.gethostbyname(socket.gethostname())
    red = ip.rsplit(".", 1)[0] #Para obtener solamente la parte de la red
    return ip, red

if __name__ == "__main__":
    ip, red = obtener_ip()
    print(f"Tu IP es: {ip}")
    print(f"Tu red es: {red}")