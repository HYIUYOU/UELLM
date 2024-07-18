#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>

#define MAX_BUFFER_SIZE 1024

struct GPUInfo
{
    int utilization;
    float freeMemory;
    float totalMemory;
};

std::string getGpuInfo(const int &gpu_id)
{
    // Build a command that calls a Python script and passes prompt arguments
    std::string gpu_index = std::to_string(gpu_id);

    std::string command = "python getgpuinfo.py \"" + gpu_index + "\"";

    // cout << "Excuting an order: " << command << endl;
    // Execute Python script and get output
    FILE *pipe = popen(command.c_str(), "r");
    if (!pipe)
    {
        std::cerr << "Unable to open pipe!" << std::endl;
        return "error";
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

    return result;
}

// Assume this is another function that returns a string

int main()
{
    int id = 0;
    std::string result = getGpuInfo(id);
    std::cout << "The detected gpu information is: " << result << std::endl;
    return 0;
}
