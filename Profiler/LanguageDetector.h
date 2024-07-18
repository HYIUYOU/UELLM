#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>

#define MAX_BUFFER_SIZE 1024

using namespace std;
string languageDetector(const string &prompt)
{
    // Build a command that calls a Python script and passes prompt arguments

    string command = "python /path/to/LanguageDetector.py \"" + prompt + "\"";

    // cout << "Excuting an order: " << command << endl;
    // Execute Python script and get output
    FILE *pipe = popen(command.c_str(), "r");
    if (!pipe)
    {
        cerr << "Unable to open pipe!" << endl;
        return "error";
    }

    char buffer[MAX_BUFFER_SIZE];
    string result = "";

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
