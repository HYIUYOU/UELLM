import GPUtil
import time
import matplotlib.pyplot as plt
import csv
import os

def monitor_and_record_gpus(duration=10, interval=1, filename='/path/to/data'):
    print("Monitoring started...")
    # Initialize data storage
    fields = ['Time', 'GPU1 Load', 'GPU2 Load', 'GPU3 Load', 'GPU4 Load', 'Total Memory Change']
    data_records = []

    start_time = time.time()
    
    # Open the file for writing
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)  # Write header of table
        
        # Monitoring and recording
        while time.time() - start_time < duration:
            gpus = GPUtil.getGPUs()
            if not gpus:
                print("No GPU found.")
                break
            load = [gpu.load * 100 for gpu in gpus]
            memory_used = [gpu.memoryUsed for gpu in gpus]
            total_memory_change = sum(memory_used) 

            # Preparing to record data
            current_time = time.time() - start_time
            record = [current_time] + load + [total_memory_change]
            data_records.append(record)
            
            # Writing to a CSV file
            csvwriter.writerow(record)

            # Printing record data
            print(f"Recorded: {record}")

            # Wait 1 second
            time.sleep(interval)

   # Drawing pictures
    plot_data2(data_records, fields)

def plot_data(data_records, fields):
    print("Plotting data...")
    transposed_data = list(zip(*data_records))
    time = transposed_data[0]
    loads = transposed_data[1:5]
    memory_changes = transposed_data[5]

    # Plot the load of each GPU
    for i in range(4):
        plt.figure(figsize=(10, 4))
        plt.plot(time, loads[i], label=f'GPU {i+1} Load', marker='o')
        plt.title(f'GPU {i+1} Load Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Load %')
        plt.legend()
        plt.grid(True)
        plt.show()  # Display the current GPU graph and wait for shutdown to continue

    # Plot Memory Change
    plt.figure(figsize=(10, 4))
    plt.plot(time, memory_changes, label='Memory Change', color='red', marker='o')
    plt.title('Memory Change Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Memory Change (MB)')
    plt.legend()
    plt.grid(True)
    plt.show()  # Display memory change chart



def plot_data2(data_records, fields):
    print("Plotting data...")
    transposed_data = list(zip(*data_records))
    time = transposed_data[0]
    loads = transposed_data[1:5]
    memory_changes = transposed_data[5]

    # Create a window with four subgraphs to show the utilization of the four GPUs
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))  # Create a 2x2 grid of sub-images
    axs = axs.flatten()  # Flatten the 2x2 array into a one-dimensional array for easy traversal

    for i in range(4):
        axs[i].plot(time, loads[i], label=f'GPU {i+1} Load', marker='o')
        axs[i].set_title(f'GPU {i+1} Load Over Time')
        axs[i].set_xlabel('Time (s)')
        axs[i].set_ylabel('Load %')
        axs[i].legend()
        axs[i].grid(True)

    plt.tight_layout()  # Adjust the layout of subgraphs
    plt.show()  # Display a window containing the utilization of four GPUs

    # Display graphics memory changes separately
    plt.figure(figsize=(10, 4))
    plt.plot(time, memory_changes, label='Memory Change', color='red', marker='o')
    plt.title('Memory Change Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Memory Change (MB)')
    plt.legend()
    plt.grid(True)
    plt.show()  # Display graphics memory change chart





if __name__ == "__main__":
    monitor_and_record_gpus(duration=1000)  # 监控60秒
