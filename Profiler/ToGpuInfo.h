#include <iostream>
#include <sstream>
#include <string>

struct GPUInfo {
    int id;
    float utilization;
    float freeMemory;
    float totalMemory;
};

GPUInfo ToGPUInfo(const std::string& result, int id) {
    std::istringstream ss(result);
    std::string token;

    // Parsing a String
    std::getline(ss, token, ',');
    float utilization = std::stoi(token);
    
    std::getline(ss, token, ',');
    float freeMemory = std::stof(token);

    std::getline(ss, token, ',');
    float totalMemory = std::stof(token);

    GPUInfo info{id, utilization, freeMemory, totalMemory};
    return info;
}