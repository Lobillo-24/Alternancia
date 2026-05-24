import socket
import platform
import subprocess

def obtener_ip():
    ip = socket.gethostbyname(socket.gethostname())
    red = ip.rsplit(".", 1)[0]
    return ip, red

def obtener_comando_ping(ip):
    sistema = platform.system()
    if sistema == "Windows":
        return ["ping", "-n", "1", ip]
    else:
        return ["ping", "-c", "1", ip]

def hacer_ping(ip):
    comando = obtener_comando_ping(ip)
    resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if resultado.returncode == 0:
        return True
    else:
        return False

def escanear_red(red):
    dispositivos_activos = []
    for i in range(1, 255):
        ip_completa = f"{red}.{i}"
        if hacer_ping(ip_completa):
            print(f"✅ Dispositivo activo: {ip_completa}")
            dispositivos_activos.append(ip_completa)
    return dispositivos_activos

if __name__ == "__main__":
    ip, red = obtener_ip()
    print(f"Tu IP es: {ip}")
    print(f"Escaneando la red: {red}.0/24...\n")
    activos = escanear_red(red)
    print(f"\nTotal de dispositivos encontrados: {len(activos)}")