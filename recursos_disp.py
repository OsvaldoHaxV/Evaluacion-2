import psutil

# Obtener la información de los recursos de hardware
disk_usage = psutil.disk_usage("/")
memory_usage = psutil.virtual_memory()
cpu_usage = psutil.cpu_percent()
network_stats = psutil.net_io_counters()

# Calcular el porcentaje de uso y disponibilidad de los recursos
disk_usage_percent = disk_usage.percent
disk_usage_available = disk_usage.free / 2**30  # Convertir a GB
memory_usage_percent = memory_usage.percent
memory_usage_available = memory_usage.available / 2**30  # Convertir a GB
cpu_usage_percent = cpu_usage
network_usage_sent = network_stats.bytes_sent / 2**20  # Convertir a MB
network_usage_received = network_stats.bytes_recv / 2**20  # Convertir a MB

# Mostrar la información en pantalla
print("Recursos de hardware disponibles:")
print(f"Uso de disco: {disk_usage_percent:.2f}%")
print(f"Disponibilidad de disco: {disk_usage_available:.2f} GB")
print(f"Uso de memoria: {memory_usage_percent:.2f}%")
print(f"Disponibilidad de memoria: {memory_usage_available:.2f} GB")
print(f"Uso de CPU: {cpu_usage_percent:.2f}%")
print(f"Uso de red - Bytes enviados: {network_usage_sent:.2f} MB")
print(f"Uso de red - Bytes recibidos: {network_usage_received:.2f} MB")
