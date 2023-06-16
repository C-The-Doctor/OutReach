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



    sql = ''' INSERT INTO MasterAccount(FullName , PhoneContact  , AltContact  , Department , Course  , Designation , UserID , SecureID , Verification )
              VALUES(?,?,?,?,?,?,?,?,?) '''
    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, TransitCredential)
        conn.commit()
        conn.close
    return "Success"
   



def Update_MasterAccount(conn, ClassProfiles):
    """
    update priority, begin_date, and end date of a MasterAccount
    :param conn:
    :param MasterAccount:
    :return: project id
    """
    sql = ''' UPDATE MasterAccount
              SET FullName = ? ,
                  PhoneContact = ? ,
                  AltContact  = ? , 
                  Department  = ?, 
                  Course  = ?, 
                  Designation  = ?,
                  UserID  = ?,
                  SecureID  = ?,
                  Verification   = ?,
              WHERE UserID = ?'''


    cur = conn.cursor()
    cur.execute(sql, ClassProfiles)
    conn.commit()
    


def Retreive_User_Profiles(conn):
    """
    Query all Credential in the MasterAccounts table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM MasterAccount ")

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_User_ID(conn):
    """
    Query MasterAccount by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT UserID FROM MasterAccount" )

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential 


def Query_User_Existence(conn, UserID):
    """
    Query MasterAccounts by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT UserID FROM MasterAccount WHERE UserID=?", (UserID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

def Query_CryptoHash_Existence(conn, SecureID):
    """
    Query MasterAccounts by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT SecureID FROM MasterAccount WHERE SecureID=?", (SecureID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;



def Confirm_Verification_Status(conn, SecureString):
    """
    Query MasterAccounts by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT Verification FROM MasterAccount WHERE Verification=?", (SecureString,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;



def Remove_User_Profile(conn, UserID):
    """
    Delete a MasterAccount by MasterAccount id
    :param conn:  Connection to the SQLite database
    :param id: id of the MasterAccount
    :return:
    """
    sql = 'DELETE FROM MasterAccount WHERE UserID = ?'
    cur = conn.cursor()
    cur.execute(sql, ( UserID ,))
    conn.commit()




conn = create_connection("./static/Databases/backup.db")

#Retreive_User_Profiles(conn)


#Alpha =( "435435-XDK-9S90" , "Clyde Javis" , "Ahoya", "Test" ,"Test", "Test", "Test" , "Test" , "Test") 
#Create_UserProfile(conn , Alpha )

#Remove_User_Profile(conn , "435435-XDK-9S90")
