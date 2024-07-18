#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>

using namespace std;
string languageDetector(const string &prompt)
{
    // Build a command that calls a Python script and passes prompt arguments

    string command = "python3 LanguageDetector.py \"" + prompt + "\"";

    cout << "Excuting an order: " << command << endl;
    // Execute Python script and get output
    FILE *pipe = popen(command.c_str(), "r");
    if (!pipe)
    {
        cerr << "Unable to open pipe!" << endl;
        return "error";
    }

    char buffer[128];
    string result = "";

    while (!feof(pipe))
    {
        if (fgets(buffer, 128, pipe) != nullptr)
        {
            result += buffer;
        }
    }

    pclose(pipe);

    // Remove the trailing newline character
    result.erase(result.find_last_not_of(" \n\r\t") + 1);

    return result;
}

// Assume this is another function that returns a string
std::string getPrompt()
{
    return "Hello World!"; // This can be any logic that returns a string
}

int main()
{
    std::string prompt = getPrompt(); // Get the prompt string
    std::string detectedLanguage = languageDetector(prompt);
    std::cout << "The detected languages ​​are: " << detectedLanguage << std::endl;
    return 0;
}
