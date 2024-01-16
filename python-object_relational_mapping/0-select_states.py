import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to MySQL server
    connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = connection.cursor()

    # Execute the SQL query to retrieve states information
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)

    # Fetch all the rows and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    # Check if correct number of command line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
    else:
        # Get command line arguments
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

        # Call the function to list states
        list_states(username, password, database)


