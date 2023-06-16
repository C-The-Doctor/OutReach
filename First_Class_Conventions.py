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

    conn = create_connection("./backup.db")
def Create_UserProfile(conn , TransitCredential):
    """
    Create a new UserProfile into the UserProfiles table
    :param conn:
    :param UserProfile:
    :return: UserProfile id
    """



    sql = ''' INSERT INTO FirstClassProfiles(FirstName ,LastName , EmailAddress  ,Gender ,  Designation ,  Department  , Course  , PhoneNumber  , AlternativeNumber , UserID , SecureID ,  ProfilePath )
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''
    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, TransitCredential)
        conn.commit()
        conn.close
    return "Success"
   



def Update_FirstClassProfiles(conn, ClassProfiles):
    """
    update priority, begin_date, and end date of a FirstClassProfiles
    :param conn:
    :param FirstClassProfiles:
    :return: project id
    """
    sql = ''' UPDATE FirstClassProfiles
              SET FirstName = ? ,
                  LastName = ? ,
                  EmailAddress  = ? , 
                  Gender  = ?, 
                  Designation  = ?, 
                  Department  = ?,
                  Course  = ?,
                  PhoneNumber  = ?,
                  AlternativeNumber   = ?,
                  UserID  = ? , 
                  SecureID = ? , 
               
                  ProfilePath  = ? ,  
              WHERE UserID = ?'''


    cur = conn.cursor()
    cur.execute(sql, ClassProfiles)
    conn.commit()
    


def Retreive_User_Profiles(conn):
    """
    Query all Credential in the FirstClassProfiless table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM FirstClassProfiles ")

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_User_ID(conn):
    """
    Query FirstClassProfiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT UserID FROM FirstClassProfiles" )

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential 


def Query_User_Existence(conn, UserID):
    """
    Query FirstClassProfiless by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT UserID FROM FirstClassProfiles WHERE UserID=?", (UserID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

def Query_CryptoHash_Existence(conn, SecureID):
    """
    Query FirstClassProfiless by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT SecureID FROM FirstClassProfiles WHERE SecureID=?", (SecureID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;






def Remove_User_Profile(conn, UserID):
    """
    Delete a FirstClassProfiles by FirstClassProfiles id
    :param conn:  Connection to the SQLite database
    :param id: id of the FirstClassProfiles
    :return:
    """
    sql = 'DELETE FROM FirstClassProfiles WHERE UserID = ?'
    cur = conn.cursor()
    cur.execute(sql, ( UserID ,))
    conn.commit()




conn = create_connection("./backup.db")

#Retreive_AllUser_Profiles(conn)


#Alpha =( "435435-XDK-9S90" , "Clyde Javis" , "Ahoya", "Test" ,"Test", "Test", "Test" , "Test" , "Test", "Test",  "Test" , "Test")
#Create_UserProfile(conn , Alpha )

#Remove_User_Profile(conn , "435435-XDK-9S90")

