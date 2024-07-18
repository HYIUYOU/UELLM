#include <iostream>
#include <string>
#include <cstdio>

int main()
{
    // Execute Python script and get output
    FILE *pipe = popen("python3 python_script.py", "r");
    if (!pipe)
    {
        std::cerr << "Unable to open pipe!" << std::endl;
        return 1;
    }

    char buffer[128];
    std::string result = "";

    // std::cout<<feof(pipe)<<std::endl;
    while (!feof(pipe))
    {
        if (fgets(buffer, 128, pipe) != NULL)
            result += buffer;
        // std::cout<<"buffer:"<<buffer<<std::endl;
        // std::cout<<"result:"<<result<<std::endl;
    }
    // std::cout<<feof(pipe)<<std::endl;
    pclose(pipe);

    // Output the return value of the Python script
    // std::cout << "Return value from Python script: " << result << std::endl;
    std::cout << "Return value from Python script: " << result << std::endl;

    return 0;
}
