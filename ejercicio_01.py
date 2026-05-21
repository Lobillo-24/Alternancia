import psutil

sistemas = {
    'windows':{"ram" :4,"disco" : 64,},
    'linux':{"ram" :2,"disco" : 25,},
    'macos':{"ram" :8,"disco" : 20,}
}

# RAM total del equipo
#psutil.virtual_memory()

# Espacio en disco
#psutil.disk_usage('/')

def obtener_info_equipo():
    ram_gb = psutil.virtual_memory().total / (1024 ** 3)
    disco_gb = psutil.disk_usage('/').total / (1024 ** 3)
    return ram_gb, disco_gb

def seleccionar_sistema_operativo():
    print("Sistemas operativos disponibles:")
    for sistema in sistemas:
        print(f"- {sistema}")
    sistema = input("Ingrese el sistema operativo: ").lower()
    if sistema in sistemas:
        return sistema
    else:
        print("Sistema operativo no reconocido.")

def verificar_requisitos(sistema, ram_gb, disco_gb):
    viable = True
    requisitos = sistemas[sistema]
    if ram_gb >= requisitos["ram"]:
        print(f"Tu equipo tiene {ram_gb:.2f} GB de RAM de los {requisitos['ram']} GB requeridos. -> Cumple con los requisitos de RAM.")
    else:
        print(f"Tu equipo tiene {ram_gb:.2f} GB de RAM de los {requisitos['ram']} GB requeridos. -> No cumple con los requisitos de RAM.")
        viable = False
       
    if disco_gb >= requisitos["disco"]:
        print(f"Tu equipo tiene {disco_gb:.2f} GB de espacio en disco de los {requisitos['disco']} GB requeridos. -> Cumple con los requisitos de disco.")
    else:
        print(f"Tu equipo tiene {disco_gb:.2f} GB de espacio en disco de los {requisitos['disco']} GB requeridos. -> No cumple con los requisitos de disco.")
        viable = False

    if viable:
        print("Tu equipo es viable para instalar el sistema operativo.")
    else:
        print("Tu equipo no es viable para instalar el sistema operativo.")

if __name__ == "__main__":
    sistema = seleccionar_sistema_operativo()
    if sistema:  # comprobamos que no sea None (por si el usuario escribió mal)
        ram_gb, disco_gb = obtener_info_equipo()
        verificar_requisitos(sistema, ram_gb, disco_gb)