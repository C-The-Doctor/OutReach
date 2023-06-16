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

    conn = create_connection("./static/Databases/backup.db")

    sql = ''' INSERT INTO StudentClassProfiles(AdmissionNo ,FullName , EmailAddress  ,Gender ,  Course ,  Level  , Stage  , PhoneNumber  , AlternativeNumber , UserID , SecureID , Status , ProfilePath )
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, TransitCredential)
        conn.commit()
        conn.close
    return "Success"
   



def Update_StudentClassProfiles(conn, ClassProfiles):
    """
    update priority, begin_date, and end date of a StudentClassProfiless
    :param conn:
    :param StudentClassProfiless:
    :return: project id
    """
    conn = create_connection("./static/Databases/backup.db")
    sql = ''' UPDATE StudentClassProfiles
              SET AdmissionNo = ? ,
                  FullName = ? ,
                  EmailAddress  = ? , 
                  Gender  = ?, 
                  Course  = ?, 
                  Level  = ?,
                  Stage  = ?,
                  PhoneNumber  = ?,
                  AlternativeNumber   = ?,
                  UserID  = ? , 
                  SecureID = ? , 
                  Status = ? ,
                  ProfilePath  = ? ,  
              WHERE UserID = ?'''


    cur = conn.cursor()
    cur.execute(sql, ClassProfiles)
    conn.commit()
    


def Retreive_User_Profiles(conn):
    """
    Query all Credential in the StudentClassProfilesss table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM StudentClassProfiles ")

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_User_ID(conn):
    """
    Query StudentClassProfiless by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT UserID FROM StudentClassProfiles" )

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential 


def Query_User_Existence(conn, UserID):
    """
    Query StudentClassProfilesss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT UserID FROM StudentClassProfiles WHERE UserID=?", (UserID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

def Query_CryptoHash_Existence(conn, SecureID):
    """
    Query StudentClassProfilesss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT SecureID FROM StudentClassProfiles WHERE SecureID=?", (SecureID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;






def Remove_User_Profile(conn, UserID):
    """
    Delete a StudentClassProfiless by StudentClassProfiless id
    :param conn:  Connection to the SQLite database
    :param id: id of the StudentClassProfiless
    :return:
    """
    sql = 'DELETE FROM StudentClassProfiles WHERE UserID = ?'
    cur = conn.cursor()
    cur.execute(sql, ( UserID ,))
    conn.commit()




conn = create_connection("./static/Databases/backup.db")

#Retreive_AllUser_Profiles(conn)


Alpha =( "435435-XDK-9S90" , "Clyde Javis" , "Ahoya", "Test" ,"Test", "Test", "Test" , "Test" , "Test", "Test", "Test", "Active", "Test")
Create_UserProfile(conn , Alpha )

#Remove_User_Profile(conn , "435435-XDK-9S90")

