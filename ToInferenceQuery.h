#ifndef GLSA_TOINFERENCEQUERY_H
#define GLSA_TOINFERENCEQUERY_H

#include <string>
#include <vector>
#include <iostream>
#include "Profiler/LabelBuilder.h"
#include "jsoncpp-0.10.7/dist/jsoncpp.cpp"
#include "Profiler/LanguageDetector.h"

#include "InferenceQuery.h"

using namespace std;

InferenceQuery ToInferenceQuery(const char *str)
{
    // Function implementation
    // ...
    // Note: Functions defined in header files should be short and efficient
    // Avoid defining complex, time-consuming functions in header files
    InferenceQuery query;
    Json::Reader reader;
    Json::Value root;
    // Convert a json into an inferencequery structure
    if (reader.parse(str, root)) //
    {
        // The reader parses the Json string to root, which will contain all the child elements in the Json
        query.prompt = root["prompt"].asString();
        // TODO
        // 1. Generate label 2. Detect language 3. Detect type 4. Generate SLO (profile)
        // Use the current time as label
        // query.label = getTime();
        query.label = GenerateLabel();
        query.language = languageDetector(root["prompt"].asString());
    }

    return query;
}

#endif // GLSA_TOINFERENCEQUERY_H
