#include <mysql/mysql.h>
#include <iostream>

// Query based on prompt and model
auto query_By_Prompt_Model(std::string Prompt, std::string Model)
{
    MYSQL *conn;
    MYSQL_RES *res = nullptr;
    MYSQL_ROW row;

    // Initializing the connection
    conn = mysql_init(NULL);

    // Connecting to the database
    if (mysql_real_connect(conn, "localhost", "root", "", "glsa", 0, NULL, 0) == NULL)
    {
        std::cerr << "mysql_real_connect() failed: " << mysql_error(conn) << std::endl;
        return res;
    }

    std::string sql = "SELECT * FROM profileseq WHERE prompt='" + Prompt + "' AND Model='" + Model + "'";

    // Query based on prompt and model
    if (mysql_query(conn, sql.c_str()))
    {
        std::cerr << "SELECT * FROM your_table failed: " << mysql_error(conn) << std::endl;
        mysql_close(conn);
        return res;
    }

    // Get query results
    return mysql_store_result(conn);
}

// Query according to prompt
auto query_By_Prompt(std::string Prompt)
{
    MYSQL *conn;
    MYSQL_RES *res = nullptr;
    MYSQL_ROW row;

    // Initializing the connection
    conn = mysql_init(NULL);

    // Connecting to the database
    if (mysql_real_connect(conn, "localhost", "root", "", "glsa", 0, NULL, 0) == NULL)
    {
        std::cerr << "mysql_real_connect() failed: " << mysql_error(conn) << std::endl;
        return res;
    }

    std::string sql = "SELECT * FROM profileseq WHERE prompt='" + Prompt + "'";
    // Query according to prompt
    if (mysql_query(conn, sql.c_str()))
    {
        std::cerr << "SELECT FROM your_table failed: " << mysql_error(conn) << std::endl;
        mysql_close(conn);
        return res;
    }

    // Get query results
    return mysql_store_result(conn);
}

int main()
{
    MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;

    // // Initializing the connection
    // conn = mysql_init(NULL);

    // // Connecting to the database
    // if (mysql_real_connect(conn, "localhost", "root", "", "glsa", 0, NULL, 0) == NULL) {
    //     std::cerr << "mysql_real_connect() failed: " << mysql_error(conn) << std::endl;
    //     return 1;
    // }

    // Execute a query
    // if (mysql_query(conn, "SELECT * FROM profileseq")) {
    //     std::cerr << "SELECT * FROM your_table failed: " << mysql_error(conn) << std::endl;
    //     mysql_close(conn);
    //     return 1;
    // }
    // Query according to prompt
    // if (mysql_query(conn, "SELECT * FROM profileseq WHERE prompt='Talk about the relationship between Fourier transform and Fourier series'")) {
    //     std::cerr << "SELECT * FROM your_table failed: " << mysql_error(conn) << std::endl;
    //     mysql_close(conn);
    //     return 1;
    // }

    // //Query based on prompt and model
    // if (mysql_query(conn, "SELECT * FROM profileseq WHERE prompt='Talk about the relationship between Fourier transform and Fourier series' AND Model='1'")) {
    //     std::cerr << "SELECT * FROM your_table failed: " << mysql_error(conn) << std::endl;
    //     mysql_close(conn);
    //     return 1;
    // }

    // // Get query results
    // res = mysql_store_result(conn);j

    res = query_By_Prompt_Model("Talk about the relationship between Fourier transform and Fourier series", "1");

    if (res)
    {
        while ((row = mysql_fetch_row(res)))
        {
            std::cout << "Column 1: " << row[0] << " , Column 2: " << row[1] << " , Column 3:" << row[3] << " , Column 4:" << row[4] << std::endl;
        }

        mysql_free_result(res);
    }
    else
    {
        std::cerr << "mysql_store_result() failed: " << mysql_error(conn) << std::endl;
    }

    // Close the connection
    mysql_close(conn);

    return 0;
}
