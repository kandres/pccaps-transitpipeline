import pymysql

from config import options as opt


def connect_to_db():
    """
    Connect to the database, return cursor object.
    """
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
		
		
def get_app_users(cursor):
    cursor.execute('SELECT id, first_name, last_name, email, created_on FROM transit_pipeline_db.app_users')
    return cursor.fetchall()  
    
        
if __name__ == '__main__':
    cursor = connect_to_db()
    
    users = get_app_users(cursor)
    
    for user in users:
        print('User first name: ', user[1])