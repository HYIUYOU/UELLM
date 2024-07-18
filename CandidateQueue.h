#ifndef GLSA_MODEL_H
#define GLSA_MODEL_H

#include <iostream>
#include <string>
#include "InferenceQuery.h"
#include <vector>
#include "ToInferenceQuery.h"

using namespace std;

struct CandidateQueue
{
    int id;
    vector<InferenceQuery> candidateQueue;
};

#endif // GLSA_MODEL_H