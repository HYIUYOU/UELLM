#ifndef GLSA_PROFILE_H
#define GLSA_PROFILE_H

#include <string>
#include "Profiler/LanguageDetector.h"
#include "Profiler/TypeDetector.h"

using namespace std;

#define GLSA_PROFILE_VERSION "1.0.0"

#define GLSA_PROFILE_NAME "GLSA Profile"

string getSLO(string prompt, int timestamp)
{
    // TODO
    // search SLO from Inference database;
    return "";
}

string getLanguage(string prompt)
{
    // TODO
    // inference from a model
    return LanguageDetector(prompt);
}

string getType(string prompt)
{
    // TODO
    // inference from a model
    return TypeDetector(prompt);
}

string getlLable(string prompt, int timestamp)
{
    // TODO
    // Use prompt and timestamp generate a lable
    // The same logo is represented as a contextual connection
    return "";
}

#endif // GLSA_PROFILE_H
