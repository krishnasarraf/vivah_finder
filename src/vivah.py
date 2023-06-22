import mysql.connector
import datetime
import json
def check_and_create_table(cursor, table_name, colums):
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    table_exists = cursor.fetchone()
    if not table_exists:
        create_table_query = f'''
        CREATE TABLE {table_name} (
            {colums}
        )
        '''
        cursor.execute(create_table_query)
        print() 
    else:
        print() 


# full_name = input("Enter Full Name: ")
# email_id = input("Enter Email_id: ")
# password = input("Enter Password: ") 
# phone_no = int(input("Enter Phone Number: "))
# privacy_proof = input("Enter Privacy Proof: ")
# about_self = input("Tell Something About Profile: ")
# connection = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="Root@123",
#  )
# cursor = connection.cursor()
# cursor.execute("SHOW DATABASES LIKE 'login'")
# database_exists = cursor.fetchone()
# if not database_exists:
#    cursor.execute("CREATE DATABASE login")
#    print() 
# else:
#    print() 
# cursor.execute('USE login')
# check_and_create_table(cursor, 'login_details_confidential', 'full_name varchar(998), email_id varchar(445), password varchar(8787), phone_number varchar(445), privacy varchar(445), about_self varchar(78)')
# cursor.execute("INSERT INTO login_details_confidential VALUES (%s, %s, %s, %s, %s, %s)",
# (full_name, email_id, password, phone_no, privacy_proof, about_self))
# connection.commit()

def login_start():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@123",
    )
    cursor = connection.cursor()

    login = input("Do You Have Your Vivah_Maker Account? (Yes/No) ")

    if login.lower() == "yes":
        full_name_get = input("Enter Full Name: ")
        email_id_get = input("Enter Email_id: ")
        password_get = input("Enter Password: ")
        phone_no_get = int(input("Enter Phone Number: "))
        privacy_proof_get = input("Enter Privacy Proof: ")
        about_self_get = input("Tell Something About Profile: ")

        cursor.execute('USE login')
        cursor.execute("SELECT * FROM login_details_confidential WHERE email_id = %s AND password = %s",
                       (email_id_get, password_get))
        result = cursor.fetchall()

        if len(result) > 0:
            for row in result:
                email_id = row[1]
                password = row[2]
            if email_id_get == email_id and password_get == password:
                print()
                print()
                print("Logged In")
                cursor.execute('USE vivah')
                cursor.execute("SELECT * FROM reccomend_profile WHERE full_name = %s",(full_name_get,))  
                result = cursor.fetchall()
                if len(result) > 0:
                  for row in result:
                    full_name = row[0]
                    age = row[1]
                    height = row[2]
                    gender = row[3]
                    country = row[4]
                    state = row[5]
                    city = row[6]
                    income = row[7]
                    marital_status = row[8]
                    occupation = row[9]
                    highest_education = row[10]
                    mother_tongue = row[11]
                    religion = row[12]
                    caste = row[13]
                    print()
                    print()
                    print("-"*40)
                    print("|","YOUR PROFILE".center(40),"","|")
                    print("-"*40) 
                    if gender.lower() == "female":
                        print("|","    ","`:`","   ",full_name.upper(),",",age," Years",",",height," Cm","","|")
                        print("|"," ","_~~(o)~~_","",occupation.capitalize(),",", highest_education.capitalize(),"","|")
                        print("|","   ","_/|\_"," ",caste.capitalize(),"/",religion.capitalize(),",",income," Lakhs","","|")
                        print("|","    ","! !","  ",state.capitalize(),"&",country.capitalize(),",",marital_status.capitalize(),"","|")   
                    elif gender.lower() == "male":
                        print("|","     ",":","   ",full_name.upper(),",",age," Years",",",height,"Cm","","|")
                        print("|","   ","_(o)_"," ",occupation.capitalize(),",", highest_education.capitalize(),"","|")
                        print("|","  "," ./|\."," ",caste.capitalize(),"/",religion.capitalize(),",",income," Lakhs","","|")
                        print("|","    ","! !","  ",state.capitalize(),"&",country.capitalize(),",",marital_status.capitalize(),"","|")   
                    print()
                    print()
                connection.commit()
            else:
                print("Invalid email or password")
                quit()
        else:
            print("Invalid email or password")
            quit()
    elif login.lower() == "no":
        full_name = input("Enter Full Name: ")
        email_id_get = input("Enter Email_id: ")
        password_get = input("Enter Password: ")
        phone_no = int(input("Enter Phone Number: "))
        privacy_proof = input("Enter Privacy Proof: ")
        about_self = input("Tell Something About Profile: ")

        cursor.execute("SHOW DATABASES LIKE 'login'")
        database_exists = cursor.fetchone()

        if not database_exists:
            cursor.execute("CREATE DATABASE login")
            print()
        else:
            print()

        cursor.execute('USE login')
        check_and_create_table(cursor, 'login_details_confidential',
                               'full_name varchar(998), email_id varchar(445), password varchar(8787), phone_number varchar(445), privacy varchar(445), about_self varchar(78)')
        cursor.execute("INSERT INTO login_details_confidential VALUES (%s, %s, %s, %s, %s, %s)",
                       (full_name, email_id_get, password_get, phone_no, privacy_proof, about_self))
        connection.commit()
        print("Logged in")

    cursor.close()
    connection.close()

login_start()
     
# WHERE full_name = %s",(full_name_get,))
reg_for=input('''
You want to make profile for your -:
    ==> Father
    ==> Mother
    ==> Sister
    ==> Brother
    ==> Self
    ==> Son
    ==> Daughter
    ==> Friend
    ==> Relative 

(IT IS NECESSARY TO FILL ALL THE DETAILS IF ANY DETAIL NOT TO BE FILLED LEAVE EMPTY PRESS ENTER)

 \n''')
def default_gender():
    if reg_for.lower() == 'son' or reg_for.lower() == 'brother' or reg_for.lower() == 'father':
        user_data["gender"] = "male"
    elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
        user_data["gender"] = "female"
def comdtional_keys(questions):
    if reg_for.lower() == "self" or reg_for.lower() == "friend" or reg_for.lower() == "relative":
        questions.insert(6,{"key": "gender", "question": f"What's {provide_pronoun()} Gender", "question": f"Enter {provide_pronoun()} Gender"})    
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
    else:
        return 'his/her'
def dahej_pronoun():
    if reg_for.lower() == 'self':
        return 'You'
    elif reg_for.lower() == 'son' or reg_for.lower() == 'father' or reg_for.lower() == 'brother':
        return 'He'
    elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
        return 'She'
    else:
        return 'He/She'
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
        return 'he had/she had'
def partener_pronoun():
    if reg_for.lower() == 'son' or reg_for.lower() == 'brother' or reg_for.lower() == 'father':
        return 'her'
    elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
         return 'his'
    else:
        return 'his/her'
def capture_user_info():
    questions = [
        # {"key": "full_name", "question": f"Enter {provide_pronoun()} full name", "heading":f"Creating {provide_pronoun()} login details : "},
        # {"key": "email_id", "question": f"Enter {provide_pronoun()} email id"},
        # {"key": "password", "question": f"Enter {provide_pronoun()} email id's password"},
        # {"key": "phone_number", "question": f"Enter {provide_pronoun()} phone number"},
        # {"key": "privacy", "question": "Contact privacy setting show to all or hide from all or show to interested people "},
        # {"key": "about_self", "question": f"Tell something about {detail_pronoun()}"},
        {"key": "full_name", "question": f"What's {provide_pronoun()} full name", "heading":f"Enter {provide_pronoun()} details : "},
        {"key": "date_of_birth", "question": f"{provide_pronoun()} date of birth"},
        {"key": "age", "question": f"Enter {provide_pronoun()} age (write age in number for example your age is 69 years then write 69)"},
        {"key": "height", "question": f"Enter {provide_pronoun()} Height in cm (for example you height is 129 cm or 4.23 foot write 129)", "heading": f"Let's start with {genearte_heading_pronoun()} basics."},
        {"key": "country", "question": f"Enter {provide_pronoun()} Country"},
        {"key": "state", "question": f"Enter {provide_pronoun()} State"},
        {"key": "city", "question": f"Enter {provide_pronoun()} City"},
        {"key": "highest_education", "question": f"Enter {provide_pronoun()} Highest Education", "heading": f"Let's Talk about {provide_pronoun()} education and career : "},
        {"key": "work_expierence", "question": f"Enter {provide_pronoun()} Work Expierence"},
        {"key": "employed_in", "question": f"Enter where {emplyment_pronoun()} Employed in"},
        {"key": "occupation", "question": f"Enter {provide_pronoun()} Occupation"},
        {"key": "income", "question": f"Enter {provide_pronoun()} Income in lakhs annually (for exmaple your salary is 30 lakhs write 30)"},
        {"key": "marital_status", "question": f"Enter {provide_pronoun()} marital Status", "heading": f"Tell us about {detail_pronoun()} Social status : "},
        {"key": "children_having", "question": "Enter number of children having after marriage"},
        {"key": "mother_tongue", "question": f"Enter {provide_pronoun()} Mother Tounge"},
        {"key": "religion", "question": f"Enter {provide_pronoun()} Religion"},
        {"key": "caste", "question": f"Enter {provide_pronoun()} Caste"},
        {"key": "caste_no_bar", "question": "Caste no bar(open to marry with any caste)(yes/no)"},
        {"key": "horoscope_marriage", "question": f"Enter {provide_pronoun()} horoscope marriage"},
        {"key": "manglik", "question": f"Enter {provide_pronoun()} manglik"},
        {"key": "dowry", "question": f"{dahej_pronoun()} want dowry or not?(yes or no)"},
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
        {"key": "family_country", "question": f"Enter their country", "heading":"Family based out of : "},
        {"key": "gothra", "question": f"Enter their gothra"},
        {"key": "partner_min_age", "question": f"Enter {partener_pronoun()} min age (write age in number for example your age is 69 years then write 69) you want(if not write none)", "heading": "Partner prefferences : "},
        {"key": "partner_max_age", "question": f"Enter {partener_pronoun()} max age (write age in number for example your age is 69 years then write 69) you want(if not write none)"},
        {"key": "partner_gender", "question": "Enter gender you want(if not write none)"},
        {"key": "partner_minheight", "question": f"Enter {partener_pronoun()} min height in cm (for example you height is 129 cm or 4.23 foot write 129) you want(if not write none)"},
        {"key": "partner_maxheight", "question": f"Enter {partener_pronoun()} max height in cm (for example you height is 129 cm or 4.23 foot write 129) you want(if not write none)"},
        {"key": "partner_country", "question": f"Enter {partener_pronoun()} country you want(if not write none)"},
        {"key": "partner_address", "question": f"Enter {partener_pronoun()} address you want(if not write none)"},
        {"key": "partner_marital_status", "question": f"Enter {partener_pronoun()} marital status you want(if not write none)"},
        {"key": "partner_marital_children", "question": "Enter number of child/children having you want(if not write none)"},
        {"key": "partner_religion", "question": f"Enter {partener_pronoun()} religion you want(if not write none)"},
        {"key": "partner_caste", "question": f"Enter {partener_pronoun()} caste you want(if not write none)"},
        {"key": "Partner_mother_tongue", "question": f"Enter {partener_pronoun()} mother tongue you want(if not write none)"},
        {"key": "partner_manglik", "question": f"Enter {partener_pronoun()} manglik you want(if not write none)"},
        {"key": "partner_education", "question": f"Enter {partener_pronoun()} education you want(if not write none)"},
        {"key": "partner_occupation", "question": f"Enter {partener_pronoun()} occupation you want(if not write none)"},
        {"key": "partner_min_income", "question": f"Enter {partener_pronoun()} min income (for exmaple your salary is 30 lakhs write 30) you want(if not write none)"},
        {"key": "partner_max_income", "question": f"Enter {partener_pronoun()} max income (for exmaple your salary is 30 lakhs write 30) you want(if not write none)"},
    ]
    comdtional_keys(questions)
    user_info = {}
    for question in questions:
        if "heading" in question:
            print(question["heading"])
            print()
        user_input = input("\t"+ question["question"] + ": ")
        print()
        if question["key"] in ["age", "height","income","partner_min_age","partner_max_age","partner_minheight","partner_maxheight","partner_min_income","partner_max_income"]:
            try:
                user_input = int(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                return capture_user_info()
        user_info[question["key"]] = user_input
    return json.dumps(user_info)
user_data_str = capture_user_info()
print(user_data_str)
user_data = json.loads(user_data_str)
# def provide_pronoun():
#     if reg_for.lower() == 'self':
#         return 'your'
#     elif reg_for.lower() == 'son' or reg_for.lower() == 'father' or reg_for.lower() == 'brother':
#         return 'his'
#     elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
#         return 'her'
#     elif reg_for.lower() == 'friend' or reg_for.lower()=='relative':
#          if user_data["gender"].lower()=="male":
#             return 'he had'
#          elif user_data["female"].lower()=="female":
#              return 'she had'
# def detail_pronoun():
#     if reg_for.lower() == 'son' or reg_for.lower() == 'brother' or reg_for.lower() == 'father':
#         return 'him'
#     elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
#          return 'her'
#     elif reg_for.lower() == 'friend' or reg_for.lower()=='relative':
#          if user_data["gender"].lower()=="male":
#             return 'her'
#          elif user_data["female"].lower()=="female":
#             return 'her'
# def emplyment_pronoun():
#     if reg_for.lower() == 'son' or reg_for.lower() == 'brother' or reg_for.lower() == 'father':
#         return 'he had'
#     elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
#          return 'she had'
#     elif reg_for.lower() == 'self':
#          return 'you had'
#     elif reg_for.lower() == 'friend' or reg_for.lower()=='relative':
#          if user_data["gender"].lower()=="male":
#             return 'he had'
#          elif user_data["female"].lower()=="female":
#              return 'she had' 
# def partener_pronoun():
#     if reg_for.lower() == 'son' or reg_for.lower() == 'brother' or reg_for.lower() == 'father':
#         return 'her'
#     elif reg_for.lower() == 'daughter' or reg_for.lower() == 'mother' or reg_for.lower() == 'sister':
#          return 'his'
#     elif reg_for.lower() == 'friend' or reg_for.lower()=='relative':
#          if user_data["gender"].lower()=="male":
#             return 'he had'
#          elif user_data["female"].lower()=="female":
#              return 'she had'
if user_data["dowry"].lower() == 'yes':
    print()
    print()
    print("calling 112...... ".upper())
    print()
    print()
    quit()
if user_data["age"] <= 21:
    print()
    print()
    print("Sorry This Website Is not For you Go or Study for your exams.".upper())
    print()
    print()
    quit()
    
def check_and_create_table(cursor, table_name, colums):
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    table_exists = cursor.fetchone()
    if not table_exists:
        create_table_query = f'''
        CREATE TABLE {table_name} (
            {colums}
        )
        '''
        cursor.execute(create_table_query)
        print() 
    else:
        print() 


def create_and_use_db():
    connector = mysql.connector.connect(
    host='localhost',            
    user='root',                   
    password='Root@123',           
    )
    cursor = connector.cursor()
    cursor.execute("SHOW DATABASES LIKE 'vivah'")
    database_exists = cursor.fetchone()
    if not database_exists:
        cursor.execute("CREATE DATABASE vivah")
        print() 
    else:
        print() 
    cursor.execute('USE vivah')
    check_and_create_table(cursor, 'introduction', 'full_name varchar(98), gender VARCHAR(20), date_of_birth VARCHAR(20), age varchar(65), height varchar(20), country varchar(30), state varchar(34), city varchar(34)')  
    cursor.execute("INSERT INTO introduction VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
           (user_data["full_name"], user_data.get("gender", f"{default_gender()}"), user_data["date_of_birth"], user_data["age"], user_data["height"], user_data["country"], user_data["state"], user_data["city"]))
    
    check_and_create_table(cursor, 'education', 'highest_education varchar(44), work_expierence varchar(44), employed_in varchar(444), occupation varchar(444), income varchar(44)')  
    cursor.execute("INSERT INTO education VALUES (%s, %s, %s, %s, %s)",
           (user_data["highest_education"], user_data["work_expierence"], user_data["employed_in"], user_data["occupation"], user_data["income"]))
    
    check_and_create_table(cursor, 'social_status', 'marital_status varchar(44), children_having varchar(44), mother_tongue varchar(44), religion varchar(44), caste varchar(44), caste_no_bar varchar(67), horoscope_marriage varchar(44), manglik varchar(44)')  
    cursor.execute("INSERT INTO social_status VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
           (user_data["marital_status"], user_data["children_having"], user_data["mother_tongue"], user_data["religion"], user_data["caste"], user_data["caste_no_bar"], user_data["horoscope_marriage"], user_data["manglik"]))
    
    # check_and_create_table(cursor, 'login_details', 'full_name varchar(998), email_id varchar(445), password varchar(8787), phone_number varchar(445), privacy varchar(445), about_self varchar(78)')
    # cursor.execute("INSERT INTO login_details VALUES (%s, %s, %s, %s, %s, %s)",
    #            (user_data["full_name"], user_data["email_id"], user_data["password"], user_data["phone_number"], user_data["privacy"], user_data["about_self"]))

    check_and_create_table(cursor, 'family_details', 'family_status varchar(44), family_values varchar(44), family_type varchar(44), family_income varchar(44), father_occupation varchar(44), mother_occupation varchar(44), brothers varchar(44), brothers_married varchar(44), sisters varchar(44), sisters_married varchar(44), family_country varchar(44), gothra varchar(44)')
    cursor.execute("INSERT INTO family_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               (user_data["family_status"], user_data["family_values"], user_data["family_type"], user_data["family_income"], user_data["father_occupation"], user_data["mother_occupation"], user_data["brothers"], user_data["brothers_married"], user_data["sisters"], user_data["sisters_married"], user_data["family_country"], user_data["gothra"]))
    
    check_and_create_table(cursor, 'partner_preferences', 'partner_min_age varchar(445), partner_max_age varchar(445), partner_gender varchar(445), partner_minheight varchar(989), partner_maxheight varchar(445), partner_country varchar(445), partner_address varchar(445), partner_marital_status varchar(445), partner_marital_children varchar(445), partner_religion varchar(445), partner_caste varchar(445), Partner_mother_tongue varchar(445), partner_manglik varchar(445), partner_education varchar(445), partner_occupation varchar(445), partner_min_income varchar(445), partner_max_income varchar(445)')
    cursor.execute("INSERT INTO partner_preferences VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               (user_data["partner_min_age"], user_data["partner_max_age"], user_data["partner_gender"], user_data["partner_minheight"], user_data["partner_maxheight"], user_data["partner_country"], user_data["partner_address"], user_data["partner_marital_status"], user_data["partner_marital_children"], user_data["partner_religion"], user_data["partner_caste"], user_data["Partner_mother_tongue"], user_data["partner_manglik"], user_data["partner_education"], user_data["partner_occupation"], user_data["partner_min_income"], user_data["partner_max_income"])) 
    
    check_and_create_table(cursor, 'reccomend_profile', 'full_name varchar(98), age varchar(65), height varchar(20), gender varchar(34), country varchar(30), state varchar(34), city varchar(34), income varchar(79), marital_status varchar(89), occupation varchar(76), highest_education varchar(889), mother_tongue varchar(8989), religion varchar(77), caste varchar(98) ')  
    cursor.execute("INSERT INTO reccomend_profile VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
           (user_data["full_name"], user_data["age"], user_data["height"], user_data.get("gender", f"{default_gender()}"), user_data["country"], user_data["state"], user_data["city"], user_data["income"], user_data["marital_status"], user_data["occupation"], user_data["highest_education"], user_data["mother_tongue"], user_data["religion"], user_data["caste"]))
    
    check_and_create_table(cursor, 'whole_profile_detail', 'full_name varchar(98), gender VARCHAR(20), date_of_birth VARCHAR(20), age varchar(65), height varchar(20), country varchar(30), state varchar(34), city varchar(34),highest_education varchar(44), work_expierence varchar(44), employed_in varchar(444), occupation varchar(444), income varchar(44), marital_status varchar(44), children_having varchar(44), mother_tongue varchar(44), religion varchar(44), caste varchar(44), caste_no_bar varchar(67), horoscope_marriage varchar(44), manglik varchar(44), family_status varchar(44), family_values varchar(44), family_type varchar(44), family_income varchar(44), father_occupation varchar(44), mother_occupation varchar(44), brothers varchar(44), brothers_married varchar(44), sisters varchar(44), sisters_married varchar(44), family_country varchar(44), gothra varchar(44), partner_min_age varchar(445), partner_max_age varchar(445), partner_gender varchar(445), partner_minheight varchar(989), partner_maxheight varchar(445), partner_country varchar(445), partner_address varchar(445), partner_marital_status varchar(445), partner_marital_children varchar(445), partner_religion varchar(445), partner_caste varchar(445), Partner_mother_tongue varchar(445), partner_manglik varchar(445), partner_education varchar(445), partner_occupation varchar(445), partner_min_income varchar(445), partner_max_income varchar(445)')  
    cursor.execute("INSERT INTO whole_profile_detail VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)",
           (user_data["full_name"], user_data.get("gender", f"{default_gender()}"), user_data["date_of_birth"], user_data["age"], user_data["height"], user_data["country"], user_data["state"], user_data["city"], user_data["highest_education"], user_data["work_expierence"], user_data["employed_in"], user_data["occupation"], user_data["income"], user_data["marital_status"], user_data["children_having"], user_data["mother_tongue"], user_data["religion"], user_data["caste"], user_data["caste_no_bar"], user_data["horoscope_marriage"], user_data["manglik"], user_data["family_status"], user_data["family_values"], user_data["family_type"], user_data["family_income"], user_data["father_occupation"], user_data["mother_occupation"], user_data["brothers"], user_data["brothers_married"], user_data["sisters"], user_data["sisters_married"], user_data["family_country"], user_data["gothra"], user_data["partner_min_age"], user_data["partner_max_age"], user_data["partner_gender"], user_data["partner_minheight"], user_data["partner_maxheight"], user_data["partner_country"], user_data["partner_address"], user_data["partner_marital_status"], user_data["partner_marital_children"], user_data["partner_religion"], user_data["partner_caste"], user_data["Partner_mother_tongue"], user_data["partner_manglik"], user_data["partner_education"], user_data["partner_occupation"], user_data["partner_min_income"], user_data["partner_max_income"]))
    connector.commit()

    cursor.execute("SELECT * FROM reccomend_profile WHERE gender = %s AND country = %s AND age > %s AND age < %s AND income > %s AND income < %s AND height > %s AND height < %s AND marital_status = %s AND occupation = %s AND highest_education = %s AND mother_tongue = %s AND religion = %s AND caste = %s",
               (user_data["partner_gender"], user_data['partner_country'], user_data['partner_min_age'], user_data['partner_max_age'], user_data['partner_min_income'], user_data['partner_max_income'], user_data['partner_minheight'], user_data['partner_maxheight'], user_data["partner_marital_status"], user_data["partner_occupation"], user_data['partner_education'], user_data["Partner_mother_tongue"], user_data["partner_religion"], user_data["partner_caste"]))
    result = cursor.fetchall()
    matches_found = False
    for row in result:
       if not matches_found:
        print("Matches for you".upper())
        matches_found = True
       print(row)
    if not matches_found:
        print("Sorry, no matches found.".upper())

    cursor.execute("SELECT * FROM reccomend_profile WHERE gender = %s AND country = %s AND age > %s AND age < %s AND income > %s AND income < %s AND height > %s AND height < %s AND marital_status = %s AND occupation = %s AND highest_education = %s AND mother_tongue = %s AND religion = %s AND caste = %s",
      (user_data["partner_gender"], user_data['partner_country'], user_data['partner_min_age'], user_data['partner_max_age'], user_data['partner_min_income'], user_data['partner_max_income'], user_data['partner_minheight'], user_data['partner_maxheight'], user_data["partner_marital_status"], user_data["partner_occupation"], user_data['partner_education'], user_data["Partner_mother_tongue"], user_data["partner_religion"], user_data["partner_caste"]))
    result = cursor.fetchall()
    if len(result) > 0:
      for row in result:
        full_name = row[0]
        age = row[1]
        height = row[2]
        gender = row[3]
        country = row[4]
        state = row[5]
        city = row[6]
        income = row[7]
        marital_status = row[8]
        occupation = row[9]
        highest_education = row[10]
        mother_tongue = row[11]
        religion = row[12]
        caste = row[13]
        print()
        print()
        print()
        print()
        print("*"*40)
        print("RECOMMENDED MATCHES FOR YOU".center(40))
        print("*"*40) 
        if gender.lower() == "female":
            print("    ","`:`","   ",full_name.upper(),",",age," Years",",",height," Cm")
            print(" ","_~~(o)~~_","",occupation.capitalize(),",", highest_education.capitalize())
            print("   ","_/|\_"," ",caste.capitalize(),"/",religion.capitalize(),",",income," Lakhs")
            print("    ","! !","  ",state.capitalize(),"&",country.capitalize(),",",marital_status.capitalize())   
        elif gender.lower() == "male":
            print("     ",":","   ",full_name.upper(),",",age," Years",",",height,"Cm")
            print("   ","_(o)_"," ",occupation.capitalize(),",", highest_education.capitalize())
            print("  "," ./|\."," ",caste.capitalize(),"/",religion.capitalize(),",",income," Lakhs")
            print("    ","! !","  ",state.capitalize(),"&",country.capitalize(),",",marital_status.capitalize())   
        print()
        print()
        print()
        print()


    cursor.close() 
    connector.close()      
create_and_use_db()
def art_condition():
 if user_data["gender"].lower() == "female":
  print("    ","`:`","   ",user_data["full_name"].upper(),",",user_data["age"]," Years",",",user_data["height"]," Cm")
  print(" ","_~~(o)~~_","",user_data["occupation"].capitalize(),",", user_data["highest_education"].capitalize())
  print("   ","_/|\_"," ",user_data["caste"].capitalize(),"/",user_data["religion"].capitalize(),",",user_data["income"]," Lakhs")
  print("    ","! !","  ",user_data["state"].capitalize(),"&",user_data["country"].capitalize(),",",user_data["marital_status"].capitalize())   
 elif user_data["gender"].lower() == "male":
  print("     ",":","   ",user_data["full_name"].upper(),",",user_data["age"]," Years",",",user_data["height"],"Cm")
  print("   ","_(o)_"," ",user_data["occupation"].capitalize(),",", user_data["highest_education"].capitalize())
  print("  "," ./|\."," ",user_data["caste"].capitalize(),"/",user_data["religion"].capitalize(),",",user_data["income"]," Lakhs")
  print("    ","! !","  ",user_data["state"].capitalize(),"&",user_data["country"].capitalize(),",",user_data["marital_status"].capitalize())
  current_datetime = datetime.datetime.now()
  current_datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
  profile_created = "Profile created on:", current_datetime_str   
  print()
  print()
  print(profile_created)
print()
print()
print()
print()
print("*"*40)
print("YOUR PROFILE".center(40))
print("*"*40) 
art_condition()
print()
print()
print()
print()



    # check_and_create_table(cursor, 'whole_profile_detail', 'full_name varchar(98), gender VARCHAR(20), date_of_birth VARCHAR(20), age varchar(65), height varchar(20), country varchar(30), state varchar(34), city varchar(34),highest_education varchar(44), work_expierence varchar(44), employed_in varchar(444), occupation varchar(444), income varchar(44), marital_status varchar(44), children_having varchar(44), mother_tongue varchar(44), religion varchar(44), caste varchar(44), caste_no_bar varchar(67), horoscope_marriage varchar(44), manglik varchar(44), full_name varchar(998), email_id varchar(445), phone_number varchar(445), privacy varchar(445), about_self varchar(78), family_status varchar(44), family_values varchar(44), family_type varchar(44), family_income varchar(44), father_occupation varchar(44), mother_occupation varchar(44), brothers varchar(44), brothers_married varchar(44), sisters varchar(44), sisters_married varchar(44), family_country varchar(44), gothra varchar(44), partner_min_age varchar(445), partner_max_age varchar(445), partner_gender varchar(445), partner_minheight varchar(989), partner_maxheight varchar(445), partner_country varchar(445), partner_address varchar(445), partner_marital_status varchar(445), partner_marital_children varchar(445), partner_religion varchar(445), partner_caste varchar(445), Partner_mother_tongue varchar(445), partner_manglik varchar(445), partner_education varchar(445), partner_occupation varchar(445), partner_min_income varchar(445), partner_max_income varchar(445)')  
    # cursor.execute("INSERT INTO whole_profile_detail VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)",
    #        (user_data["full_name"], user_data.get("gender", f"{default_gender()}"), user_data["date_of_birth"], user_data["age"], user_data["height"], user_data["country"], user_data["state"], user_data["city"], user_data["highest_education"], user_data["work_expierence"], user_data["employed_in"], user_data["occupation"], user_data["income"], user_data["marital_status"], user_data["children_having"], user_data["mother_tongue"], user_data["religion"], user_data["caste"], user_data["caste_no_bar"], user_data["horoscope_marriage"], user_data["manglik"], user_data["full_name"], user_data["email_id"], user_data["phone_number"], user_data["privacy"], user_data["about_self"], user_data["family_status"], user_data["family_values"], user_data["family_type"], user_data["family_income"], user_data["father_occupation"], user_data["mother_occupation"], user_data["brothers"], user_data["brothers_married"], user_data["sisters"], user_data["sisters_married"], user_data["family_country"], user_data["gothra"], user_data["partner_min_age"], user_data["partner_max_age"], user_data["partner_gender"], user_data["partner_minheight"], user_data["partner_maxheight"], user_data["partner_country"], user_data["partner_address"], user_data["partner_marital_status"], user_data["partner_marital_children"], user_data["partner_religion"], user_data["partner_caste"], user_data["Partner_mother_tongue"], user_data["partner_manglik"], user_data["partner_education"], user_data["partner_occupation"], user_data["partner_min_income"], user_data["partner_max_income"]))



import subprocess

def export_database(source_host, source_user, source_password, source_database, export_path):
    # Construct the mysqldump command
    command = f"mysqldump -h {source_host} -u {source_user} -p{source_password} {source_database} > {export_path}"

    try:
        # Execute the command
        subprocess.run(command, shell=True, check=True)
        print("Database export completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during database export: {e}")

# Example usage
source_host = "localhost"
source_user = "source_user"
source_password = "source_password"
source_database = "source_database"
export_path = "path/to/exported/database.sql"

export_database(source_host, source_user, source_password, source_database, export_path)
