#ifndef GLSA_TIMER_H
#define GLSA_TIMER_H

#include <time.h>
#include <string>
using namespace std;

string getTime() // 2020-09-11 22:00:49 This only lasts for seconds
{
    time_t timep;
    time(&timep);
    char tmp[64];
    strftime(tmp, sizeof(tmp), "%Y-%m-%d %H:%M:%S", localtime(&timep));
    return tmp;
}

#endif // GLSA_TIMER_H