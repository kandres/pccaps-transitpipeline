#Here we are importing the pymysql library, we need this in order to read/write to the database 
import pymysql

#Here we are importing the "options" file as "opt" (just an alias) within our program. The "config" portion indicates the folder that they options file is located in. 
#The goal here is to store common configuration options in a single file so we do not have to copy/paste them all of our code
from config import options as opt


#This method is our database connection method, similar to keeping all of our options in one spot, we also want to keep our connection "steps" in one spot so we don't have to write them all out everytime we need them
#first we connect to the database and store it in the 'db' object (short for databse). then we return the database's cursor, which is our interaction point with the database, we tell the cursor to execute commands for us
def connect_to_db():
    """
    Connect to the database, return cursor object.
    """
    #try/except -> Here we are wrapping the database connection in a try/except block, the reason for this is to improve our code's error handling. We tell it to "try" the instructions within that block of code
    #if they succeed it will complete the method, however if they encounter an error, instead of breaking the program we want to instead "handle" that except (error) and log it. 
    try:
        db = pymysql.connect(
            host=opt.db_host,
            db=opt.db_name,
            user=opt.db_user,
            passwd=opt.db_pass,
            autocommit=True)
        return db.cursor()
    except pymysql.DatabaseError as err:
        err_msg = ("Cannot connect to the database! Please check "
                   "connection details in 'config/options.py' (%s).")
        logging.error(err_msg, err)
		

#Here we created a method to get users from the database table "app_users" within the "transit_pipeline_db" database. We tell the database cursor to execute a "SELECT" statement and indicate what columns we want it to select		
def get_app_users(cursor):
    cursor.execute('SELECT id, first_name, last_name, email, created_on FROM transit_pipeline_db.app_users')
    return cursor.fetchall()  
    

#This is the main program entry point, the starting point when we run this example.py program
if __name__ == '__main__':
    #create an object "cursor" with the database (db) cursor
    cursor = connect_to_db()
    
    #pass that cursor into the "get_app_users" method so that the method can tell the cursor what to retrieve (in this case all the users), store the response in the "users" object
    users = get_app_users(cursor)
    
    #the database response is a list of objects (users), so we want to loop through each of them, read this as "for each user in the users list, do XXX", and in this case XXX is print the users first name, which is in the [1] index of the user object
    for user in users:
        print('User first name: ', user[1])