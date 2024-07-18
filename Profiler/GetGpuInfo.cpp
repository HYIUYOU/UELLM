#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
// #include "ToGpuInfo.h"
#include "GPUInfoList.h"
// #define MAX_BUFFER_SIZE 1024

// int getGPUNumber(){
//      std::string command = "python GetGPUNumber.py" ;

//     // cout << "Excuting an order: " << command << endl;
//     // Execute Python script and get output
//     FILE* pipe = popen(command.c_str(), "r");
//     if (!pipe) {
//         std::cerr << "Unable to open pipe!" << std::endl;
//         return 0;
//     }

//     char buffer1[MAX_BUFFER_SIZE];
//     std::string gpunumber = "";

//     while (!feof(pipe)) {
//         if (fgets(buffer1, 128, pipe) != nullptr) {
//             gpunumber += buffer1;
//         }
//     }
//     // cout <<"result's size:"<< result.size() << endl;
//     pclose(pipe);

//     // Remove the trailing newline character
//     gpunumber.erase(gpunumber.find_last_not_of(" \n\r\t") + 1);

//     // std::cout<<"result:"<<gpunumber<<std::endl;
//     return std::stoi(gpunumber);
// }

// GPUInfo e;

// GPUInfo getGpuInfoById(const int& gpu_id ){

//     // Build a command that calls a Python script and passes prompt arguments
//     std::string gpu_index = std::to_string(gpu_id);

//     std::string command = "python GetGpuInfo.py \"" + gpu_index + "\"";

//     // cout << "Excuting an order: " << command << endl;
//     // Execute Python script and get output
//     FILE* pipe = popen(command.c_str(), "r");
//     if (!pipe) {
//         std::cerr << "Unable to open pipe!" << std::endl;
//         return e;
//     }

//     char buffer[MAX_BUFFER_SIZE];
//     std::string result = "";

//     while (!feof(pipe)) {
//         if (fgets(buffer, 128, pipe) != nullptr) {
//             result += buffer;
//         }
//     }
//     // cout <<"result's size:"<< result.size() << endl;
//     pclose(pipe);

//     // Remove the trailing newline character
//     result.erase(result.find_last_not_of(" \n\r\t") + 1);

//     // std::cout<<"result:"<<result<<std::endl;

//     return ToGPUInfo(result, gpu_id);
// }

// Assume this is another function that returns a string
// #include <iostream>
// #include <cuda_runtime.h>

// int getcpu() {
//     int deviceCount;
//     cudaGetDeviceCount(&deviceCount);

//     std::cout << "Total GPUs: " << deviceCount << std::endl;

//     return 0;
// }

int main()
{
    // // getcpu();
    // int id = 0;
    // GPUInfo result = getGpuInfoById(id);
    // std::cout << "Detected GPUs:  "<<result.id<<", utilization： " << result.utilization<<", remaining graphics memory："<<result.freeMemory <<", total graphics memory："<< result.totalMemory<<std::endl;
    // return 0;

    GPUInfoList gpuInfoList = getGpuInfoList();
    std::cout << "The number detected of GPUs为: " << gpuInfoList.gpuNumber << std::endl;
    for (auto &gpuInfo : gpuInfoList.gpuInfoList)
    {
        std::cout << "Detected GPUs:  " << gpuInfo.id << ", utilization： " << gpuInfo.utilization << ", remaining graphics memory：" << gpuInfo.freeMemory << ", total graphics memory：" << gpuInfo.totalMemory << std::endl;
    }

    return 0;
}
