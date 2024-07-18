#ifndef GLSA_VHA_H
#define GLSA_VHA_H

#include <iostream>
#include <string>

class VHA
{
public:
    VHA(int id, int Hardware_id, int all_Vmem, int left_Vmem)
        : id(id), Hardware_id(Hardware_id), all_Vmem(all_Vmem), left_Vmem(left_Vmem) {}

    // :param id: VHA id
    // :param Hardware_id: VHA mapped physical hardware accelerator id
    // :param all_Vmem: VHA total virtual memory
    // :param left_Vmem: VHA remaining virtual memory

    // Getter methods for class members
    int getId() const { return id; }
    int getHardwareId() const { return Hardware_id; }
    int getAllVmem() const { return all_Vmem; }
    int getLeftVmem() const { return left_Vmem; }

    // Mapping VHA to HA
    int mapping()
    {
        // Implement mapping logic here
        return 1; // Example return value, modify as needed
    }

    // Load a model into VHA
    int load()
    {
        // Implement load model logic here
        return 1; // Example return value, modify as needed
    }

private:
    int id;
    int Hardware_id;
    int all_Vmem;
    int left_Vmem;
};

#endif // GLSA_VHA_H
