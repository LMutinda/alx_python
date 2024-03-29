import MySQLdb
import sys

def search_states(username, password, database, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to retrieve states information based on user input
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY states.id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check if correct number of command line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name> <state_name>")
    else:
        # Get command line arguments
        username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

        # Call the function to search for states based on user input
        search_states(username, password, database, state_name)
