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

hardware = {
    "System" : system_type,
    "Version" : system_version,
    "Processor" : system_processor,
    "Machine" : system_machine,
    "Cores" : CPU_cores,
    "CPU Frequency" : CPU_frequency,
    "RAM Memory" : Memory,
    "Free Storage" : free_storage,
    }

try:
    hardware.update({"GPU" : GPU})
    hardware.update({"GPU Storage in MB" : GPU_storage})
except:
    hardware.update({"GPU" : "GPU Not Detected"})
    hardware.update({"GPU Storage in MB" : "GPU Not Detected"})