#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include "ToGpuInfo.h"
#include <vector>
#define MAX_BUFFER_SIZE 1024
#define MAX_GPU_NUMBER 1024

struct GPUInfoList
{
    std::vector<GPUInfo> gpuInfoList;
    int gpuNumber;
};

GPUInfoList GPUqueue;

GPUInfo e;

// Get the total number of GPUs
int getGPUNumber()
{
    std::string command = "python Profiler/GetGPUNumber.py";

    // cout << "Excuting an order: " << command << endl;
    // Execute Python script and get output
    FILE *pipe = popen(command.c_str(), "r");
    if (!pipe)
    {
        std::cerr << "Unable to open pipe!" << std::endl;
        return 0;
    }

    char buffer1[MAX_BUFFER_SIZE];
    std::string gpunumber = "";

    while (!feof(pipe))
    {
        if (fgets(buffer1, 128, pipe) != nullptr)
        {
            gpunumber += buffer1;
        }
    }
    // cout <<"result's size:"<< result.size() << endl;
    pclose(pipe);

    // Remove the trailing newline character
    gpunumber.erase(gpunumber.find_last_not_of(" \n\r\t") + 1);

    // std::cout<<"result:"<<gpunumber<<std::endl;
    return std::stoi(gpunumber);
}

// Get GPU information by GPU ID
GPUInfo getGpuInfoById(const int &gpu_id)
{

    // Build a command that calls a Python script and passes prompt arguments
    std::string gpu_index = std::to_string(gpu_id);

    std::string command = "python Profiler/GetGpuInfo.py \"" + gpu_index + "\"";

    // cout << "Excuting an order: " << command << endl;
    // Execute Python script and get output
    FILE *pipe = popen(command.c_str(), "r");
    if (!pipe)
    {
        std::cerr << "Unable to open pipe!" << std::endl;
        return e;
    }

    char buffer[MAX_BUFFER_SIZE];
    std::string result = "";

    while (!feof(pipe))
    {
        if (fgets(buffer, 128, pipe) != nullptr)
        {
            result += buffer;
        }
    }
    // cout <<"result's size:"<< result.size() << endl;
    pclose(pipe);

    // Remove the trailing newline character
    result.erase(result.find_last_not_of(" \n\r\t") + 1);

    // std::cout<<"result:"<<result<<std::endl;

    return ToGPUInfo(result, gpu_id);
}

// Get information about all GPUs
GPUInfoList getGpuInfoList()
{
    GPUqueue.gpuNumber = getGPUNumber();
    GPUqueue.gpuInfoList.resize(GPUqueue.gpuNumber);
    for (int i = 0; i < GPUqueue.gpuNumber; i++)
    {
        GPUqueue.gpuInfoList[i] = getGpuInfoById(i);
    }
    return GPUqueue;
}
