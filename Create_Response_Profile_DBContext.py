import sqlite3
from sqlite3 import Error
from flask import *

app=Flask(__name__)

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

    conn = create_connection("./static/Databases/backup.db")
def Create_Response_Data_Profiles(conn , TransitCredential):
    """
    Create a new Response_Data_Profile into the Response_Data_Profiles table
    :param conn:
    :param Response_Data_Profile:
    :return: Response_Data_Profile id
    """



    sql = ''' INSERT INTO  Response_Data_Profile(ResponseID , ResponseType , OwnerID , ResponseQ1 , ResponseQ2 , ResponseQ3 , ResponseQ4 , ResponseQ5  , Status , Timestamp )
    VALUES(?,?,?,?,?,?,?,?,?,?) '''
    
    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, TransitCredential)
        conn.commit()
        conn.close
    return "Success"
   



def Retreive_Response_Data_Profiles(conn):
    """
    Query all Credential in the Response_Data_Profiles table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Response_Data_Profile ")

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_Response_ID(conn):
    """
    Query Response_Data_Profile by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT ResponseID FROM Response_Data_Profile" )

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential 


def Query_User_Existence(conn, ResID):
    """
    Query Response_Data_Profiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT ResponseID FROM Response_Data_Profile WHERE ResponseID=?", (ResID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

def Retrieve_User_Response(conn, Owner_Profile):
    """
    Query Response_Data_Profiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM Response_Data_Profile WHERE ResponseOwner=?", (Owner_Profile,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;






def Remove_Response_Data_Profile(conn, ResID):
    """
    Delete a Response_Data_Profile by Response_Data_Profile id
    :param conn:  Connection to the SQLite database
    :param id: id of the Response_Data_Profile
    :return:
    """
    sql = 'DELETE FROM Response_Data_Profile WHERE ResponseID = ?'
    cur = conn.cursor()
    cur.execute(sql, ( ResID ,))
    conn.commit()




#conn = create_connection("./static/Databases/backup.db")

#Retreive_Response_Data_Profiles(conn)


#Alpha =( "435435-sd-as9sdS90" , "Clyde Javis" , "Ahoya", "Test" ,"Test", "Test", "Test" , "dssd" "sdjsd" , "yuaisa" , "sdksd")
#Create_Response_Data_Profiles(conn , Alpha )

#Remove_Response_Data_Profile(conn , "435435-XDK-9S90")

