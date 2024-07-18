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
