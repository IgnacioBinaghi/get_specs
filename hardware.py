import psutil
import platform
from size_adjustment import *
import GPUtil
import cpuinfo

base_info = platform.uname() # Utilization of the platform class

# Getting the base System Information
system_type = base_info.system
system_version = base_info.release
system_processor = cpuinfo.get_cpu_info()['brand_raw']  # ['brand_raw'] is added to only extract the gpu's name and cores
system_machine = base_info.machine



# Getting CPU Information
CPU_cores = psutil.cpu_count(logical=False)

frequency = psutil.cpu_freq()
v  = (frequency.max) / 1000   # Converting Mhz to Ghz
CPU_frequency = v



# Getting memory Information
u = psutil.virtual_memory()
Memory = size_adjustment(u.total)


# Getting Storage
disk_usage = psutil.disk_usage("/")
free_storage = size_adjustment(disk_usage.free)

# Getting GPU Information
gpu_info = GPUtil.getGPUs()
for i in gpu_info:
    GPU = i.name
    GPU_storage = i.memoryTotal


# Entering All information into a dictionary

hardware = {}

try:
    hardware.update({"System" : system_type})
except:
    hardware.update({"System": "System Type Not Detected"})
try:
    hardware.update({"Version" : system_version})
except:
    hardware.update({"Version" : "System Version Not Detected"})
try:
    hardware.update({"Processor" : system_processor})
except:
    hardware.update({"Processor": "Processor Not Detected"})
try:
    hardware.update({"Machine" : system_machine})
except:
    hardware.update({"Machine" : "Machine Type Not Detected"})
try:
    hardware.update({"Cores" : CPU_cores})
except:
    hardware.update({"Cores": "Cores Not Detected"})
try:
    hardware.update({"CPU Frequency" : CPU_frequency})
except:
    hardware.update({"CPU Frequency" : "CPU Frequency Not Detected"})
try:
    hardware.update({"RAM Memory" : Memory})
except:
    hardware.update({"RAM Memory": "RAM Memory Not Detected"})
try:
    hardware.update({"Free Storage" : free_storage})
except:
    hardware.update({"Free Storage" : "Free Storage Not Detected"})
try:
    hardware.update({"GPU": GPU})
except:
    hardware.update({"GPU": "GPU Not Detected"})
try:
    hardware.update({"GPU Storage in MB" : GPU_storage})
except:
    hardware.update({"GPU Storage in MB" : "GPU Not Detected"})
try:
    hardware.update({"GPU": GPU})
except:
    hardware.update({"GPU": "GPU Not Detected"})
try:
    hardware.update({"GPU Storage in MB" : GPU_storage})
except:
    hardware.update({"GPU Storage in MB" : "GPU Not Detected"})