#ifndef GLSA_MODEL_H
#define GLSA_MODEL_H

#include <iostream>
#include <string>

using namespace std;

// Model structure
struct Model
{
    std::string label;
    int memory; // storage
    std::string language;
    std::string type;
    int popularity;

    //    Model()
    //            : label(label), memory(memory), language(language), type(type), popularity(popularity) {}

    // Deploy the model to a device
    int modelLoad(string device)
    {
        // Implement model loading logic here
        return 1; // Example return value, modify as needed
    }

    // Calculate model-device affinity
    double modelDeviceAffinity(string device)
    {
        // Implement model-device affinity calculation here
        double modelDeviceAffinity = 0.75; // Example value, modify as needed
        return modelDeviceAffinity;
    }

    // Calculate model-inference affinity
    double modelInferenceAffinity(string inference)
    {
        // Implement model-inference affinity calculation here
        double modelInferenceAffinity = 0.85; // Example value, modify as needed
        return modelInferenceAffinity;
    }

    //    size_t operator()(const Model& model) const {
    //        // You can choose any attribute that is suitable as an input to the hash function
    //        // Here we use the label string to calculate the hash value
    //        return std::hash<std::string>{}(model.label);
    //    }
};

// class Model {
// public:
//     Model(string label, int memory, string language, string type, double popularity)
//             : label(label), memory(memory), language(language), type(type), popularity(popularity) {}
//
//     // Getter methods for class members (optional)
//     string getLabel() const { return label; }
//     int getMemory() const { return memory; }
//     string getLanguage() const { return language; }
//     string getType() const { return type; }
//     double getPopularity() const { return popularity; }
//
//     // Deploy the model to a device
//     int modelLoad(string device) {
//         // Implement model loading logic here
//         return 1; // Example return value, modify as needed
//     }
//
//     // Calculate model-device affinity
//     double modelDeviceAffinity(string device) {
//         // Implement model-device affinity calculation here
//         double modelDeviceAffinity = 0.75; // Example value, modify as needed
//         return modelDeviceAffinity;
//     }
//
//     // Calculate model-inference affinity
//     double modelInferenceAffinity(string inference) {
//         // Implement model-inference affinity calculation here
//         double modelInferenceAffinity = 0.85; // Example value, modify as needed
//         return modelInferenceAffinity;
//     }
//
// private:
//     string label;
//     int memory;
//     string language;
//     string type;
//     double popularity;
// };

#endif // GLSA_MODEL_H