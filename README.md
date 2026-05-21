🖥️ Ejercicio 1 - Planificador de instalación de Sistemas Operativos
¿Qué hace?
Programa en Python que analiza las características de tu equipo y determina si es viable instalar un sistema operativo concreto.
El programa compara los recursos reales de tu máquina (RAM y disco) con los requisitos mínimos de cada sistema operativo y genera un informe por pantalla.
🖥️ Sistemas operativos disponibles
SistemaRAM mínimaDisco mínimoWindows4 GB64 GBLinux2 GB25 GBmacOS8 GB20 GB
📦 Librerías utilizadas

psutil → para obtener información real del equipo (RAM y disco)

⚙️ Instalación
Instala la librería necesaria:
bashpython -m pip install psutil
▶️ Cómo usarlo

Ejecuta el programa:

bashpython ejercicio_01.py

Selecciona el sistema operativo que quieres instalar
El programa analizará tu equipo automáticamente
Verás el informe con el resultado

📋 Ejemplo de salida
Sistemas operativos disponibles:
- windows
- linux
- macos
Ingrese el sistema operativo: windows
Tu equipo tiene 31.64 GB de RAM de los 4 GB requeridos. -> Cumple con los requisitos de RAM.
Tu equipo tiene 952.79 GB de espacio en disco de los 64 GB requeridos. -> Cumple con los requisitos de disco.
Tu equipo es viable para instalar el sistema operativo.
