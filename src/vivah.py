import mysql.connector
import datetime
import json
reg_for=input('''
You want to make profile for your -:
    --> Father
    --> Mother
    --> Sister
    --> Brother
    --> Self
    --> Son
    --> Daughter
    --> Friend \n''')
def default_gender():
    if reg_for.lower() == 'son' or reg_for.lower() == 'brother' or reg_for.lower() == 'father':
        user_data["gender"] = "male"
    elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
        user_data["gender"] = "female"
def comdtional_keys(questions):
    if reg_for.lower() == "self" or reg_for.lower() == "friend" or reg_for.lower() == "relative":
        questions.insert(2,{"key": "gender", "question": f"What's {provide_pronoun()} Gender", "question": f"Enter {provide_pronoun()} Gender"})    
def genearte_heading_pronoun():
    if reg_for.lower() == 'self': 
        return 'your'
    else:
        return 'your\'s ' + str(reg_for)
def provide_pronoun():
    if reg_for.lower() == 'self':
        return 'your'
    elif reg_for.lower() == 'son' or reg_for.lower() == 'father' or reg_for.lower() == 'brother':
        return 'his'
    elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
        return 'her'
    elif reg_for.lower() == 'friend':
        return "his/her"
def detail_pronoun():
    if reg_for.lower() == 'son' or reg_for.lower() == 'brother' or reg_for.lower() == 'father':
        return 'him'
    elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
         return 'her'
    else:
        return 'him/her'
def emplyment_pronoun():
    if reg_for.lower() == 'son' or reg_for.lower() == 'brother' or reg_for.lower() == 'father':
        return 'he had'
    elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
         return 'she had'
    elif reg_for.lower() == 'self':
         return 'you had'
    else:
         return 'he/she had' 
def partener_pronoun():
    if reg_for.lower() == 'son' or reg_for.lower() == 'brother' or reg_for.lower() == 'father':
        return 'her'
    elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
         return 'his'
    else:
        return 'his/her'
def capture_user_info():
    questions = [
        {"key": "name", "question": f"What's {provide_pronoun()} first name"},
        {"key": "date_of_birth", "question": f"{provide_pronoun()} date of birth"},
        {"key": "age", "question": f"Enter {provide_pronoun()} age"},
        {"key": "height", "question": f"Enter {provide_pronoun()} Height", "heading": f"Let's start with {genearte_heading_pronoun()} basics."},
        {"key": "country", "question": f"Enter {provide_pronoun()} Country"},
        {"key": "state", "question": f"Enter {provide_pronoun()} State"},
        {"key": "city", "question": f"Enter {provide_pronoun()} City"},
        {"key": "highest_education", "question": f"Enter {provide_pronoun()} Highest Education", "heading": f"Let's Talk about {provide_pronoun()} education and career : "},
        {"key": "work_expierence", "question": f"Enter {provide_pronoun()} Work Expierence"},
        {"key": "employed_in", "question": f"Enter where {emplyment_pronoun()} Employed in"},
        {"key": "occupation", "question": f"Enter {provide_pronoun()} Occupation"},
        {"key": "income", "question": f"Enter {provide_pronoun()} Income"},
        {"key": "martial_status", "question": f"Enter {provide_pronoun()} Martial Status", "heading": f"Tell us about {detail_pronoun()} Social status : "},
        {"key": "children_having", "question": "Enter number of children having after marriage"},
        {"key": "mother_tongue", "question": f"Enter {provide_pronoun()} Mother Tounge"},
        {"key": "religion", "question": f"Enter {provide_pronoun()} Religion"},
        {"key": "caste", "question": f"Enter {provide_pronoun()} Caste"},
        {"key": "caste_no_bar", "question": "Caste no bar(open to marry with any caste)(yes/no)"},
        {"key": "horoscope_marriage", "question": f"Enter {provide_pronoun()} horoscope marriage"},
        {"key": "manglik", "question": f"Enter {provide_pronoun()} manglik"},
        {"key": "full_name", "question": f"Enter {provide_pronoun()} full name", "heading":f"Create {provide_pronoun()} login details : "},
        {"key": "email_id", "question": f"Enter {provide_pronoun()} email id"},
        {"key": "phone_number", "question": f"Enter {provide_pronoun()} phone number"},
        {"key": "privacy", "question": "Contact privacy setting show to all or hide from all or show to interested people : "},
        {"key": "about_self", "question": f"Tell something about {detail_pronoun()}"},
        {"key": "family_status", "question": f"Enter {provide_pronoun()} family status", "heading": "Family details : "},
        {"key": "family_values", "question": f"Enter {provide_pronoun()} family values"},
        {"key": "family_type", "question": f"Enter {provide_pronoun()} family types"},
        {"key": "family_income", "question": f"Enter {provide_pronoun()} family income"},
        {"key": "father_occupation", "question": f"Enter {provide_pronoun()} father's occupation"},
        {"key": "mother_occupation", "question": f"Enter {provide_pronoun()} mother's occupation"},
        {"key": "brothers", "question": f"Enter {provide_pronoun()} brother(s)"},
        {"key": "brothers_married", "question": f"Enter {provide_pronoun()} brother(s) married"},
        {"key": "sisters", "question": f"Enter {provide_pronoun()} sister(s)"},
        {"key": "sisters_married", "question": f"Enter {provide_pronoun()} sister(s) married"},
        {"key": "family_country", "question": f"Enter {provide_pronoun()} country", "heading":"Family based out of : "},
        {"key": "gothra", "question": f"Enter {provide_pronoun()} gothra"},
        {"key": "partner_min_age", "question": f"Enter {partener_pronoun()} min age you want(if not write none)", "heading": "Partner prefferences : "},
        {"key": "partner_max_age", "question": f"Enter {partener_pronoun()} max age you want(if not write none)"},
        {"key": "partner_gender", "question": "Enter gender you want(if not write none)"},
        {"key": "partner_minheight", "question": f"Enter {partener_pronoun()} min height you want(if not write none)"},
        {"key": "partner_maxheight", "question": f"Enter {partener_pronoun()} max height you want(if not write none)"},
        {"key": "partner_country", "question": f"Enter {partener_pronoun()} country you want(if not write none)"},
        {"key": "partner_address", "question": f"Enter {partener_pronoun()} address you want(if not write none)"},
        {"key": "partner_martial_status", "question": f"Enter {partener_pronoun()} martial status you want(if not write none)"},
        {"key": "partner_martial_children", "question": "Enter number of child/children having you want(if not write none)"},
        {"key": "partner_religion", "question": f"Enter {partener_pronoun()} religion you want(if not write none)"},
        {"key": "partner_caste", "question": f"Enter {partener_pronoun()} caste you want(if not write none)"},
        {"key": "Partner_mother_tongue", "question": f"Enter {partener_pronoun()} mother tongue you want(if not write none)"},
        {"key": "partner_manglik", "question": f"Enter {partener_pronoun()} manglik you want(if not write none)"},
        {"key": "partner_education", "question": f"Enter {partener_pronoun()} education you want(if not write none)"},
        {"key": "partner_occupation", "question": f"Enter {partener_pronoun()} occupation you want(if not write none)"},
        {"key": "partner_min_income", "question": f"Enter {partener_pronoun()} min income you want(if not write none)"},
        {"key": "partner_max_income", "question": f"Enter {partener_pronoun()} max income you want(if not write none)"},
    ]

    comdtional_keys(questions)

    user_info = {}

    for question in questions:
        if "heading" in question:
            print(question["heading"])
            print()

        user_input = input("\t"+ question["question"] + ": ")
        print()
        user_info[question["key"]] = user_input

    return json.dumps(user_info)
user_data_str = capture_user_info()
print(user_data_str)
user_data = json.loads(user_data_str)
if user_data["age"] <= '18':
    print()
    print()
    print("Sorry This Website Is not For you Go and Study for your exams.".upper())
    print()
    quit() 
def check_and_create_table(cursor, table_name, colums):
    # Check if the table exists
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    table_exists = cursor.fetchone()

    # Create the table if it doesn't exist
    if not table_exists:
        create_table_query = f'''
        CREATE TABLE {table_name} (
            {colums}
        )
        '''
        cursor.execute(create_table_query)
        print() #f"Table '{table_name}' created successfully"
    else:
        print() #f"Table '{table_name}' already exists"
def create_and_use_db():
    connector = mysql.connector.connect(
    host='localhost',            
    user='root',                   
    password='Root@123',           
    )
    cr = connector.cursor()

    # Check if the database exists
    cr.execute("SHOW DATABASES LIKE 'vivah'")
    database_exists = cr.fetchone()

    # Create the database if it doesn't exist
    if not database_exists:
        cr.execute("CREATE DATABASE vivah")
        print() #"Database 'vivah' created successfully"
    else:
        print() #"Database 'vivah' already exists"

    cr.execute('USE vivah')

    check_and_create_table(cr, 'introduction', 'name varchar(98), gender VARCHAR(20), date_of_birth VARCHAR(20), age varchar(65), height varchar(20), country varchar(30), state varchar(34), city varchar(34)')  
    cr.execute("INSERT INTO introduction VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
           (user_data["name"], user_data.get("gender", f"{default_gender()}"), user_data["date_of_birth"], user_data["age"], user_data["height"], user_data["country"], user_data["state"], user_data["city"]))
    
    
    check_and_create_table(cr, 'education', 'highest_education varchar(44), work_expierence varchar(44), employed_in varchar(444), occupation varchar(444), income varchar(44)')  
    cr.execute("INSERT INTO education VALUES (%s, %s, %s, %s, %s)",
           (user_data["highest_education"], user_data["work_expierence"], user_data["employed_in"], user_data["occupation"], user_data["income"]))
    
    check_and_create_table(cr, 'social_status', 'martial_status varchar(44), children_having varchar(44), mother_tongue varchar(44), religion varchar(44), caste varchar(44), caste_no_bar varchar(67), horoscope_marriage varchar(44), manglik varchar(44)')  
    cr.execute("INSERT INTO social_status VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
           (user_data["martial_status"], user_data["children_having"], user_data["mother_tongue"], user_data["religion"], user_data["caste"], user_data["caste_no_bar"], user_data["horoscope_marriage"], user_data["manglik"]))
    
    check_and_create_table(cr, 'login_details', 'full_name varchar(998), email_id varchar(445), phone_number varchar(445), privacy varchar(445), about_self varchar(78)')
    cr.execute("INSERT INTO login_details VALUES (%s, %s, %s, %s, %s)",
               (user_data["full_name"], user_data["email_id"], user_data["phone_number"], user_data["privacy"], user_data["about_self"]))

    check_and_create_table(cr, 'family_details', 'family_status varchar(44), family_values varchar(44), family_type varchar(44), family_income varchar(44), father_occupation varchar(44), mother_occupation varchar(44), brothers varchar(44), brothers_married varchar(44), sisters varchar(44), sisters_married varchar(44), family_country varchar(44), gothra varchar(44)')
    cr.execute("INSERT INTO family_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               (user_data["family_status"], user_data["family_values"], user_data["family_type"], user_data["family_income"], user_data["father_occupation"], user_data["mother_occupation"], user_data["brothers"], user_data["brothers_married"], user_data["sisters"], user_data["sisters_married"], user_data["family_country"], user_data["gothra"]))
    
    check_and_create_table(cr, 'partner_preferences', 'partner_min_age varchar(445), partner_max_age varchar(445), partner_gender varchar(445), partner_minheight varchar(989), partner_maxheight varchar(445), partner_country varchar(445), partner_address varchar(445), partner_martial_status varchar(445), partner_martial_children varchar(445), partner_religion varchar(445), partner_caste varchar(445), Partner_mother_tongue varchar(445), partner_manglik varchar(445), partner_education varchar(445), partner_occupation varchar(445), partner_min_income varchar(445), partner_max_income varchar(445)')
    cr.execute("INSERT INTO partner_preferences VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               (user_data["partner_min_age"], user_data["partner_max_age"], user_data["partner_gender"], user_data["partner_minheight"], user_data["partner_maxheight"], user_data["partner_country"], user_data["partner_address"], user_data["partner_martial_status"], user_data["partner_martial_children"], user_data["partner_religion"], user_data["partner_caste"], user_data["Partner_mother_tongue"], user_data["partner_manglik"], user_data["partner_education"], user_data["partner_occupation"], user_data["partner_min_income"], user_data["partner_max_income"])) 
    
    check_and_create_table(cr, 'reccomend_profile', 'name varchar(98), age varchar(65), height varchar(20), country varchar(30), state varchar(34), city varchar(34), income varchar(79), martial_status varchar(89), occupation varchar(76), highest_education varchar(889), mother_tongue varchar(8989), religion varchar(77), caste varchar(98) ')  
    cr.execute("INSERT INTO reccomend_profile VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
           (user_data["name"], user_data["age"], user_data["height"], user_data["country"], user_data["state"], user_data["city"], user_data["income"], user_data["martial_status"], user_data["occupation"], user_data["highest_education"], user_data["mother_tongue"], user_data["religion"], user_data["caste"]))
    

    check_and_create_table(cr, 'whole_profile_detail', 'name varchar(98), gender VARCHAR(20), date_of_birth VARCHAR(20), age varchar(65), height varchar(20), country varchar(30), state varchar(34), city varchar(34),highest_education varchar(44), work_expierence varchar(44), employed_in varchar(444), occupation varchar(444), income varchar(44), martial_status varchar(44), children_having varchar(44), mother_tongue varchar(44), religion varchar(44), caste varchar(44), caste_no_bar varchar(67), horoscope_marriage varchar(44), manglik varchar(44), full_name varchar(998), email_id varchar(445), phone_number varchar(445), privacy varchar(445), about_self varchar(78), family_status varchar(44), family_values varchar(44), family_type varchar(44), family_income varchar(44), father_occupation varchar(44), mother_occupation varchar(44), brothers varchar(44), brothers_married varchar(44), sisters varchar(44), sisters_married varchar(44), family_country varchar(44), gothra varchar(44), partner_min_age varchar(445), partner_max_age varchar(445), partner_gender varchar(445), partner_minheight varchar(989), partner_maxheight varchar(445), partner_country varchar(445), partner_address varchar(445), partner_martial_status varchar(445), partner_martial_children varchar(445), partner_religion varchar(445), partner_caste varchar(445), Partner_mother_tongue varchar(445), partner_manglik varchar(445), partner_education varchar(445), partner_occupation varchar(445), partner_min_income varchar(445), partner_max_income varchar(445)')  
    cr.execute("INSERT INTO whole_profile_detail VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)",
           (user_data["name"], user_data.get("gender", f"{default_gender()}"), user_data["date_of_birth"], user_data["age"], user_data["height"], user_data["country"], user_data["state"], user_data["city"], user_data["highest_education"], user_data["work_expierence"], user_data["employed_in"], user_data["occupation"], user_data["income"], user_data["martial_status"], user_data["children_having"], user_data["mother_tongue"], user_data["religion"], user_data["caste"], user_data["caste_no_bar"], user_data["horoscope_marriage"], user_data["manglik"], user_data["full_name"], user_data["email_id"], user_data["phone_number"], user_data["privacy"], user_data["about_self"], user_data["family_status"], user_data["family_values"], user_data["family_type"], user_data["family_income"], user_data["father_occupation"], user_data["mother_occupation"], user_data["brothers"], user_data["brothers_married"], user_data["sisters"], user_data["sisters_married"], user_data["family_country"], user_data["gothra"], user_data["partner_min_age"], user_data["partner_max_age"], user_data["partner_gender"], user_data["partner_minheight"], user_data["partner_maxheight"], user_data["partner_country"], user_data["partner_address"], user_data["partner_martial_status"], user_data["partner_martial_children"], user_data["partner_religion"], user_data["partner_caste"], user_data["Partner_mother_tongue"], user_data["partner_manglik"], user_data["partner_education"], user_data["partner_occupation"], user_data["partner_min_income"], user_data["partner_max_income"]))
    
    connector.commit()
 


# Create a cursor object

    '''cr.execute("SELECT * FROM reccomend_profile WHERE country = '%s' and age >= %s AND age <= %s and income >= %s AND income <= %s and height >= %s and height<= %s and martial_status = '%s' and occupation = '%s' and highest_education = '%s' and mother_tongue = '%s' and religion = '%s' and caste = '%s' or age = 'none' or height = 'none' or country = 'none' or martial_status = 'none' or religion = 'none' or caste = 'none' or mother_tongue = 'none' or highest_education  = 'none' or occupation = 'none' or income = 'none';" , (user_data['partner_country'],user_data['partner_min_age'], user_data['partner_max_age'],user_data['partner_min_income'], user_data['partner_max_income'], user_data['partner_minheight'], user_data['partner_maxheight'], user_data["partner_martial_status"], user_data["partner_occupation"] , user_data['partner_education'], user_data["Partner_mother_tongue"] , user_data["partner_religion"], user_data["partner_caste"]))
    result = cr.fetchall()

# Print the result
    for row in result:
        print("matches for you".upper())
        print(row)'''


    
# Assuming you have established the MySQL connection and created a cursor object

# Define the SQL query with named placeholders
    query = """
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
 }

# Execute the query with the provided parameters
    cr.execute(query, placeholders)

# Fetch the result
    result = cr.fetchall()
    print("matches for u".upper())
# Print the result
    for row in result:
       print(row)

    cr.close()
    connector.close()


create_and_use_db()

def art_condition():
 if user_data["gender"].lower() == "female":
  print("     ",":","   ",user_data["name"].upper(),",",user_data["age"].capitalize(),"Years",",",user_data["height"].capitalize())
  print("  ","_~(o)~_","",user_data["occupation"].capitalize(),",", user_data["highest_education"].capitalize())
  print("   ","_/|\_"," ",user_data["caste"].capitalize(),"/",user_data["religion"].capitalize(),",",user_data["income"].capitalize())
  print("    ","! !","  ",user_data["state"].capitalize(),"&",user_data["country"].capitalize(),",",user_data["martial_status"].capitalize())   
 elif user_data["gender"].lower() == "male":
  print("     ",":","   ",user_data["name"].upper(),",",user_data["age"].capitalize(),"Years",",",user_data["height"].capitalize())
  print("   ","_(o)_"," ",user_data["occupation"].capitalize(),",", user_data["highest_education"].capitalize())
  print("  "," ./|\."," ",user_data["caste"].capitalize(),"/",user_data["religion"].capitalize(),",",user_data["income"].capitalize())
  print("    ","! !","  ",user_data["state"].capitalize(),"&",user_data["country"].capitalize(),",",user_data["martial_status"].capitalize())   

print()
print()
print()
print()
print("*"*45)
print("Your Profile".center(45))
print("*"*45) 
art_condition()
print()
print()
print()
print()