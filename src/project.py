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













    
# Assuming you have established the MySQL connection and created a cursor object

# Define the SQL query with named placeholders
'''    query = """
     SELECT *
     FROM reccomend_profile
     WHERE age >= %(min_age)s
         AND age <= %(max_age)s
         AND height >= %(min_height)s
         AND height <= %(max_height)s
         AND country = %(country)s
         AND martial_status = %(martial_status)s
         AND religion = %(religion)s
         AND caste = %(caste)s
         AND mother_tongue = %(mother_tongue)s
         AND highest_education = %(highest_education)s
         AND occupation = %(occupation)s
         AND income >= %(min_income)s
         AND income <= %(max_income)s
         
 """

# Define the values for the named placeholders
    placeholders = {
     'min_age': user_data['partner_min_age'],
     'max_age': user_data['partner_max_age'],
     'min_height': user_data['partner_minheight'],
     'max_height': user_data['partner_maxheight'],
     'country': user_data['partner_country'],
     'martial_status': user_data['partner_martial_status'],
     'religion': user_data['partner_religion'],
     'caste': user_data['partner_caste'],
     'mother_tongue': user_data['Partner_mother_tongue'],
     'highest_education': user_data['partner_education'],
     'occupation': user_data['partner_occupation'],
     'min_income': user_data['partner_min_income'],
     'max_income': user_data['partner_max_income']
# }

# Execute the query with the provided parameters
#    cursor.execute(query, placeholders)'''



















def provide_pronoun():
    if reg_for.lower() == 'self':
        return 'your'
    elif reg_for.lower() == 'son' or reg_for.lower() == 'father' or reg_for.lower() == 'brother':
        return 'his'
    elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
        return 'her'
    elif reg_for.lower() == 'friend' or reg_for.lower()=='relative':
         if user_data["gender"].lower()=="male":
            return 'he had'
         elif user_data["female"].lower()=="female":
             return 'she had'
def detail_pronoun():
    if reg_for.lower() == 'son' or reg_for.lower() == 'brother' or reg_for.lower() == 'father':
        return 'him'
    elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
         return 'her'
    elif reg_for.lower() == 'friend' or reg_for.lower()=='relative':
         if user_data["gender"].lower()=="male":
            return 'her'
         elif user_data["female"].lower()=="female":
            return 'her'
def emplyment_pronoun():
    if reg_for.lower() == 'son' or reg_for.lower() == 'brother' or reg_for.lower() == 'father':
        return 'he had'
    elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
         return 'she had'
    elif reg_for.lower() == 'self':
         return 'you had'
    elif reg_for.lower() == 'friend' or reg_for.lower()=='relative':
         if user_data["gender"].lower()=="male":
            return 'he had'
         elif user_data["female"].lower()=="female":
             return 'she had' 
def partener_pronoun():
    if reg_for.lower() == 'son' or reg_for.lower() == 'brother' or reg_for.lower() == 'father':
        return 'her'
    elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
         return 'his'
    elif reg_for.lower() == 'friend' or reg_for.lower()=='relative':
         if user_data["gender"].lower()=="male":
            return 'he had'
         elif user_data["female"].lower()=="female":
             return 'she had'

