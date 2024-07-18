import multiprocessing

# Define a task function to simulate the execution of GPU tasks
def gpu_task(task_id, gpu_id):
    print(f"Task {task_id} is running on GPU {gpu_id}")

# Get the number of GPU devices in the system
gpu_count = multiprocessing.cpu_count()  # Here we use the number of CPU cores as the number of GPUs

print("Number of GPUs",gpu_count)  # Output the number of CPU cores


# Create a task list
tasks = [(i, i % gpu_count) for i in range(1, 6)]  # Generate 5 tasks and assign them to different GPU devices

# Create a process pool, each process is responsible for executing a task
with multiprocessing.Pool(processes=gpu_count) as pool:
    pool.starmap(gpu_task, tasks)
