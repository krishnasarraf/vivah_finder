import mysql.connector

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(
    host='localhost',           # Replace with your host
    user='root',       # Replace with your username
    password='Root@123',   # Replace with your password
    database='vivah_finder'    # Replace with your database name
)

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Execute a query
query = "SELECT * FROM test"  # Replace with your table name
cursor.execute(query)

# Fetch and print all the rows returned by the query
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
cnx.close()




or age = "none"
         or height = "none"
         or country = "none"
         or martial_status = "none"
         or religion = "none"
         or caste = "none"
         or mother_tongue = "none"
         or highest_education  = "none"
         or occupation = "none"
         or income = "none"
