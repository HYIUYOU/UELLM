import pynvml

# Initialize the NVML library
pynvml.nvmlInit()

try:
    # Get the number of GPUs in the system
    gpu_count = pynvml.nvmlDeviceGetCount()
    print(f"{gpu_count}")

except pynvml.NVMLError as e:
    print(f"NVML Error: {e}")

finally:
    # Cleaning up NVML resources
    pynvml.nvmlShutdown()
