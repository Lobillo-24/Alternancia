# Proyecto Python - Alternancia

## ¿Qué hace?
Tres herramientas desarrolladas en Python que simulan el trabajo real de un equipo de administración de sistemas y ciberseguridad.

---

## Ejercicio 1 - Planificador de instalación de Sistemas Operativos

Programa que analiza las características de tu equipo y determina si es viable instalar un sistema operativo.

### Sistemas operativos disponibles
| Sistema | RAM mínima | Disco mínimo |
|---|---|---|
| Windows | 4 GB | 64 GB |
| Linux | 2 GB | 25 GB |
| macOS | 8 GB | 20 GB |

### Librerías utilizadas
- `psutil` - para obtener información real del equipo

### Cómo usarlo
1. Instalar: `python -m pip install psutil`
2. Ejecutar: `python ejercicio_01.py`
3. Seleccionar el sistema operativo

---

## Ejercicio 2 - Escáner de Red Automático

Programa que detecta automáticamente la red local y escanea qué dispositivos están activos.

### Librerías utilizadas
- `socket` - para obtener la IP del equipo
- `platform` - para detectar el sistema operativo
- `subprocess` - para ejecutar el comando ping

### Cómo usarlo
1. Ejecutar: `python ejercicio_02.py`
2. El programa escanea automáticamente toda la red

---

## Ejercicio 3 - Conexión a MySQL en Aiven con Streamlit

Aplicación web que se conecta a una base de datos MySQL en la nube y muestra los datos en una interfaz web.

### Librerías utilizadas
- `pymysql` - para conectarse a MySQL
- `streamlit` - para la interfaz web
- `python-dotenv` - para gestionar credenciales de forma segura

### Cómo usarlo
1. Instalar librerías:
   `python -m pip install pymysql streamlit python-dotenv`
2. Crear archivo `.env` con la contraseña de la base de datos
3. Ejecutar: `python -m streamlit run ejercicio_03.py`
4. Abrir el navegador en `http://localhost:8501`
5. Hacer clic en "Cargar datos"
