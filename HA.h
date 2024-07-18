#include <iostream>
#include <string>

class HA
{
public:
    HA(int id, int all_mem, int left_mem, double FLOPS, string type, double price)
        : id(id), all_mem(all_mem), left_mem(left_mem), FLOPS(FLOPS), type(type), price(price) {}

    // :param id: The id of HA
    // :param all_mem: Total memory of HA
    // :param left_mem: HA remaining memory
    // :param FLOPS: FLOPS of HA
    // :param type: Types of HA: GPU,TP....
    // :param price: Price of HA

    int getId() { return id; }
    int getAllMem() { return all_mem; }
    int getLeftMem() { return left_mem; }
    double getFLOPS() { return FLOPS; }
    string getType() { return type; }
    double getPrice() { return price; }
    // Get HA utilization
    double getUtilization() const
    {
        return deviceUtilization;
    }

    // Update HA utilization
    void renewUtilization(HA ha)
    {

        deviceUtilization = ha.getUtilization();
    }

    // Get remaining memory
    double getMemory()
    {
        return left_mem;
    }

    // Update remaining memory
    void renewLeftMem(HA ha)
    {
        left_mem = ha.getMemory();
    }

    // Display HA information
    void displayInfo() const
    {
        cout << "HA ID: " << id << endl;
        cout << "Total Memory: " << all_mem << " MiB" << endl;
        cout << "Left Memory: " << left_mem << " MiB" << endl;
        cout << "FLOPS: " << FLOPS << endl;
        cout << "Type: " << type << endl;
        cout << "Price: $" << price << endl;
    }

private:
    int id;
    double all_mem;
    double left_mem;
    double FLOPS;
    string type;
    double price;
    double deviceUtilization; // Assume there is a member variable to store the device utilization.
};
