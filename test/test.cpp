#include <iostream>
#include <mysql/mysql.h>

int main()
{
    MYSQL *conn;
    MYSQL_RES *res, res1;
    MYSQL_ROW row;

    // Initializing the connection
    conn = mysql_init(NULL);

    // Connecting to the database
    if (mysql_real_connect(conn, "localhost", "root", "", "glsa", 0, NULL, 0) == NULL)
    {
        std::cerr << "mysql_real_connect() failed: " << mysql_error(conn) << std::endl;
        return 1;
    }
    else
    {
        std::cout << "connect success" << std::endl;
    }

    //    Execute a query
    if (mysql_query(conn, "SELECT * FROM profileseq"))
    {
        std::cerr << "SELECT * FROM your_table failed: " << mysql_error(conn) << std::endl;
        mysql_close(conn);
        return 1;
    }
    else
    {
        std::cout << "query success" << std::endl;
    }

    if (mysql_query(conn, "SELECT * FROM profileseq"))
    {
        std::cerr << "SELECT * FROM your_table failed: " << mysql_error(conn) << std::endl;
        mysql_close(conn);
        return 1;
    }
    else
    {
        std::cout << "query success" << std::endl;
    }
    //    // Query according to prompt
    //     if (mysql_query(conn, "SELECT * FROM profileseq WHERE prompt='Talk about the relationship between Fourier transform and Fourier series'")) {
    //         std::cerr << "SELECT * FROM your_table failed: " << mysql_error(conn) << std::endl;
    //         mysql_close(conn);
    //         return 1;
    //     }else{
    //         std::cout<<"query success"<<std::endl;
    //     }

    // Get query results
    // res = mysql_store_result(conn);
    // res1 = mysql_store_result(conn);

    // res = mysql_store_result(conn);

    // auto res1 = query_By_Prompt_Model("Talk about the relationship between Fourier transform and Fourier series","1");

    // if (res) {
    //     while ((row = mysql_fetch_row(res))) {
    //         std::cout << "Column 1: " << row[0] << " , Column 2: " << row[1] <<" , Column 3:"<< row[3] <<" , Column 4:" << row[4]<< std::endl;
    //     }

    //     mysql_free_result(res);
    // } else {
    //     std::cerr << "mysql_store_result() failed: " << mysql_error(conn) << std::endl;
    // }

    // Close the connection
    mysql_close(conn);

    return 0;
}