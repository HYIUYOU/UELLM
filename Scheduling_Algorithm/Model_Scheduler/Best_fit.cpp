#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

struct GPUInfo
{
    int id;            // GPU ID
    float utilization; // GPU Utilization
    float freeMemory;  // GPU Free Memory
    float totalMemory; // GPU Total Memory
};

// Comparison function, sorting by GPU remaining memory from small to large
bool compareGPU(const GPUInfo &g1, const GPUInfo &g2)
{
    return g1.totalMemory - g1.freeMemory < g2.totalMemory - g2.freeMemory;
}

// Best-fit scheduling algorithm
void bestFit(std::vector<GPUInfo> &gpus, float taskMemory)
{
    // Sort GPUs by remaining memory from small to large
    std::sort(gpus.begin(), gpus.end(), compareGPU);

    // Finding the smallest GPU
    auto it = std::find_if(gpus.begin(), gpus.end(), [&](const GPUInfo &gpu)
                           { return gpu.freeMemory >= taskMemory; });

    // If a GPU is found, assign the task to it
    if (it != gpus.end())
    {
        it->freeMemory -= taskMemory;
        std::cout << "Task assigned to GPU " << it->id << std::endl;
    }
    // If no GPU is found, an error message is output
    else
    {
        std::cout << "Error: no GPU available for task" << std::endl;
    }
}

int main()
{
    // Initialize GPU information
    std::vector<GPUInfo> gpus = {{1, 0.5, 1024, 2048}, {2, 0.8, 512, 1024}, {3, 0.3, 2048, 4096}};

    // Execute Best-fit scheduling algorithm
    float taskMemory = 256;
    bestFit(gpus, taskMemory);

    return 0;
}