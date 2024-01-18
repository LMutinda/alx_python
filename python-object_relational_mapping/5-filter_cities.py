import MySQLdb
import sys

def select_cities(username, password, database, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Use parameterized query to prevent MySQL injection
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

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

        # Call the function to search for cities based on user input
        select_cities(username, password, database, state_name)