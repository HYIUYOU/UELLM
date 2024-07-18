#include <iostream>
#include <string>
#include <mysql/mysql.h>
#include "SchedulingTable.h"
#include "InferenceQuery.h"
#include "VHA.h"
#include "HA.h"
#include "Model.h"
#include "Batch.h"
#include "ToInferenceQuery.h"
#include "Profiler/GPUInfoList.h"
#include "Profiler/MysqlFunction.h"

MYSQL *conn;
MYSQL_RES *res;
MYSQL_ROW row;

int main()
{
    // Example usage of the VHA class
    VHA vha(1, 101, 1024, 512);

    std::cout << "VHA & HA mapping" << endl;
    std::cout << "------------------------------------------------------------------------------------------------------" << std::endl;

    std::cout << "VHA ID: " << vha.getId() << endl;
    std::cout << "Hardware ID: " << vha.getHardwareId() << endl;
    std::cout << "Total Vmem: " << vha.getAllVmem() << endl;
    std::cout << "Left Vmem: " << vha.getLeftVmem() << endl;

    // Perform mapping and loading operations
    int result1 = vha.mapping();
    int result2 = vha.load();

    std::cout << "Mapping Result: " << result1 << endl;
    std::cout << "Load Result: " << result2 << endl;

    std::cout << "------------------------------------------------------------------------------------------------------" << std::endl;

    QueryTable schedulingTable;

    InferenceQuery query1 = {"Query1", "SLO1", "English", "NLP", "Prompt1"};
    Model model1 = {"ChatGLM-6B", 1024, "Chinese", "NLP", 2};

    InferenceQuery query2 = {"Query2", "SLO2", "Spanish", "CV", "Prompt2"};
    Model model2 = {"ChatGLM2-6B", 1724, "Chinese", "NLP", 6};

    // Add inference queries and models to the query table
    schedulingTable.add(query1, model1);
    schedulingTable.add(query2, model2);
    std::cout << "Print SchedulingTable" << std::endl;
    // Output the contents of the query table.
    schedulingTable.printTable();

    // Query the model corresponding to the inference query.
    Model resultModel = schedulingTable.findModel(query1);
    std::cout << "find Query1 in SchedulingTable:" << std::endl;
    std::cout << "Query1 is associated with Model: " << resultModel.label << std::endl;

    Batch batch;

    InferenceQuery query3 = {"Query3", "SLO3", "Chinese", "CV", "Prompt3"};
    Model model3 = {"ChatGLM2-6B", 1724, "Chinese", "NLP", 6};

    std::cout << "------------------------------------------------------------------------------------------------------" << std::endl;

    cout << "batch function test" << endl;

    cout << "batch is empty:" << batch.isEmpty() << endl;
    std::cout << "------------------------------------------------------------------------------------------------------" << std::endl;

    cout << "add query1, query2,query3 in to batch" << endl;
    batch.add(query1);
    batch.add(query2);
    batch.add(query3);

    batch.printbatch();
    std::cout << "------------------------------------------------------------------------------------------------------" << std::endl;

    cout << "delete the position 0 query in  batch" << endl;
    batch.deletequery(0);

    batch.printbatch();

    std::cout << "------------------------------------------------------------------------------------------------------" << std::endl;

    cout << "ToInferenceQuery Function test" << endl;

    cout << "get a Json j: \n{\"\n"
            "                      \"    \\\"prompt\\\": \\\"Hello\\\",\\n\"\n"
            "                      \"    \\\"history\\\": []\\n\"\n"
            "                      \"}\n and return a Inference query q"
         << endl;
    // char* str = "{\n"
    //                   "    \"prompt\": \"hello\",\n"
    //                   "    \"history\": []\n"
    //                   "}";

    const char *str = "{\n"
                      "    \"prompt\": \"Hello\",\n"
                      "    \"history\": []\n"
                      "}";

    InferenceQuery q = ToInferenceQuery(str);
    // string lang = languageDetector(q.prompt);

    cout << "inference q.prompt:" << q.prompt << endl;
    cout << "inference q.Lable:" << q.label << endl;
    cout << "inference q.language:" << q.language << endl;

    GPUInfoList gpuInfoList = getGpuInfoList();
    std::cout << "The number of detected GPUs is: " << gpuInfoList.gpuNumber << std::endl;
    for (auto &gpuInfo : gpuInfoList.gpuInfoList)
    {
        std::cout << "Detected GPU is " << gpuInfo.id << " , its utilization rate: " << gpuInfo.utilization << " , remaining graphics memory: " << gpuInfo.freeMemory << " , total graphics memory: " << gpuInfo.totalMemory << std::endl;
    }

    // mysql test
    std::cout << "------------------------------------------------------------------------------------------------------" << std::endl;
    std::cout << "mysql test" << std::endl;

    res = query_By_Prompt_Model("Talk about the relationship between Fourier transform and Fourier series.", "1");

    std::cout << "prompt :Talk about the relationship between Fourier transform and Fourier series, model:1 , search result: " << std::endl;

    if (res)
    {
        while ((row = mysql_fetch_row(res)))
        {
            std::cout << "ID: " << row[0] << " , prompt: " << row[1] << " , SUM: " << row[2] << " , MEM_change: " << row[3] << ", time_seconds: " << row[4] << " , is it a continuous question: " << row[5] << ", model: " << row[6] << std::endl;
        }

        mysql_free_result(res);
    }
    else
    {
        std::cerr << "mysql_store_result() failed: " << mysql_error(conn) << std::endl;
    }

    // Close the connection.
    mysql_close(conn);

    return 0;
}