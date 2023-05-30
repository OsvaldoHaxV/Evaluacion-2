import re
from datetime import datetime, timedelta

# Obtener la hora actual
current_time = datetime.now()

# Calcular la última hora cerrada y la hora inicial del rango
if current_time.hour == 0:
    last_hour = 23
    start_hour = 0
else:
    last_hour = current_time.hour - 1
    start_hour = last_hour

# Obtener el rango de tiempo en formato HH:MM - HH:MM
time_range = f"{start_hour:02d}:00 - {last_hour:02d}:59"

# Leer el archivo de registro de autenticación
log_file = "/var/log/auth.log"
with open(log_file, "r") as file:
    log_lines = file.readlines()

# Definir el patrón de búsqueda para los intentos fallidos de inicio de sesión
pattern = r"Failed password .* from"

# Contador de intentos fallidos
failed_attempts = 0

# Recorrer las líneas del archivo de registro
for line in log_lines:
    # Obtener la fecha y hora de la línea de registro
    match = re.search(r"(\w{3} +\d{1,2} \d{2}:\d{2}:\d{2})", line)
    if match:
        log_time = datetime.strptime(match.group(1), "%b %d %H:%M:%S")
        
        # Verificar si la línea de registro está dentro del rango de tiempo especificado
        if start_hour <= log_time.hour <= last_hour:
            # Verificar si la línea de registro contiene un intento fallido de inicio de sesión
            if re.search(pattern, line):
                failed_attempts += 1

# Mostrar la cantidad de intentos fallidos en el rango de tiempo especificado
print(f"Cantidad de intentos fallidos en el rango {time_range}: {failed_attempts}")
