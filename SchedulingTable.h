#ifndef GLSA_SCHEDULINGTABLE_H
#define GLSA_SCHEDULINGTABLE_H

#include <iostream>
#include <unordered_map>
#include <vector>

#include "Model.h"
#include "InferenceQuery.h"

/// Define routing table management class
class QueryTable
{
public:
    // SchedulingTable() {}

    // Add the mapping relationship between Model and InferenceQuery to the routing table
    void add(const InferenceQuery &query, const Model &model)
    {
        routingTable[query.label] = model;
    }

    // Query the InferenceQuery corresponding to the Model
    const Model findModel(const InferenceQuery &inferenceQuery) const
    {
        auto it = routingTable.find(inferenceQuery.label);
        if (it != routingTable.end())
        {
            return it->second;
        }
        else
        {
            // Returns a default constructed InferenceQuery, or throws an exception, as appropriate.
            return Model();
        }
    }

    // Output the contents of the routing table
    void printTable()
    {
        for (const auto &entry : routingTable)
        {
            const string &query = entry.first;
            const Model &model = entry.second;

            std::cout << "------------------------------------------------------------------------------------------------------" << std::endl;
            std::cout << "Query: " << query << ", Model: " << model.label << std::endl;
            std::cout << "Model Memory: " << model.memory << std::endl;
            std::cout << "Model Language: " << model.language << std::endl;
            std::cout << "Model Type: " << model.type << std::endl;
            std::cout << "Model Popularity: " << model.popularity << std::endl;
            std::cout << "------------------------------------------------------------------------------------------------------" << std::endl;
        }
    }

private:
    std::unordered_map<string, Model> routingTable;
};

// int main() {
//     QueryTable queryTable;

//     // Create some inference queries and models
//     InferenceQuery query1 = {"Query1", "SLO1", "English", "NLP", "Prompt1"};
//     Model model1 = {"Model1", 1024, "English", "NLP", 5};

//     InferenceQuery query2 = {"Query2", "SLO2", "Spanish", "CV", "Prompt2"};
//     Model model2 = {"Model2", 2048, "Spanish", "CV", 3};

//     // Add inference queries and models to the query table
//     queryTable.addPair(query1, model1);
//     queryTable.addPair(query2, model2);

//     // Query the model corresponding to the inference query
//     Model resultModel = queryTable.findModel(query1);
//     std::cout << "Query1 is associated with Model: " << resultModel.label << std::endl;

//     return 0;
// }

#endif // GLSA_SCHEDULINGTABLE_H
