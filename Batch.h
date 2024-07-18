#ifndef GLSA_BATCH_H
#define GLSA_BATCH_H

#include <utility>
#include <vector>
#include <string>
#include <iostream>
#include "InferenceQuery.h"
#include <stdio.h>

int MAX_BATCH_SIZE = 10;

using namespace std;
struct Batch
{

    vector<InferenceQuery> batchQueue;
    int size;

    void add(InferenceQuery query)
    {
        batchQueue.push_back(query);
        size++;
    }

    void clear()
    {
        batchQueue.erase(batchQueue.begin(), batchQueue.end());
        size = 0;
    }

    bool isEmpty()
    {
        if (batchQueue.size() == 0)
            return true;
        else
            return false;
    }

    void deletequery(int index)
    {
        batchQueue.erase(batchQueue.begin() + index);

        size--;
    }

    bool isFull()
    {
        if (batchQueue.size() == 10)
            return true;
        else
            return false;
    }

    void printbatch()
    {
        int size = batchQueue.size();
        for (int i = 0; i < size; i++)
            std::cout << batchQueue[i].label << endl;
    }
};

#endif // GLSA_BATCH_H