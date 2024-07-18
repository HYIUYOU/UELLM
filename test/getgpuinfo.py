import pynvml

# Initialize the NVML library
pynvml.nvmlInit()

# Specifies the GPU index to query (usually starts at 0)
gpu_index = 0

try:
    # Get the handle of the specified GPU
    handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_index)

    # Get GPU utilization
    utilization = pynvml.nvmlDeviceGetUtilizationRates(handle).gpu

    # Get video graphics memory usage
    memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    free_memory = memory_info.free / (1024 * 1024)  # MB
    total_memory = memory_info.total / (1024 * 1024)  # MB

    print(f"GPU Utilization: {utilization}%")
    print(f"Free Memory: {free_memory} MB")
    print(f"Total Memory: {total_memory} MB")

except pynvml.NVMLError as e:
    print(f"NVML Error: {e}")
finally:
    # Cleaning up NVML resources
    pynvml.nvmlShutdown()
