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

    sql = ''' INSERT INTO ReceiverAccount(AdmNumber , FullName , PhoneContact , AltContact , Gender , Certification  , Course  , Module , UserID  , SecureID  , Verification  , AccountStatus )
              VALUES(?,?,?,?,?,?,?,?,?,?,?,"Active") '''
    with app.app_context():
        cur = conn.cursor()
    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, TransitCredential)
        conn.commit()
        conn.close
    return "Success"




def Update_ReceiverAccount(conn, ClassProfiles):
    """
    update priority, begin_date, and end date of a ReceiverAccounts
    :param conn:
    :param ReceiverAccounts:
    :return: project id
    """
    conn = create_connection("./static/Databases/backup.db")
    sql = ''' UPDATE ReceiverAccount
              SET AdmNumber = ? ,
                  FullName = ? ,
                  PhoneContact  = ? ,
                  AltContact  = ?,
                  Gender  = ?,
                  Certification  = ?,
                  Course  = ?,
                  Module  = ?,
                  UserID   = ?,
                  SecureID  = ? ,
                  Verification = ? ,
                  AccountStatus  = ? ,
              WHERE UserID = ?'''


    cur = conn.cursor()
    cur.execute(sql, ClassProfiles)
    conn.commit()



def Retreive_User_Profiles(conn):
    """
    Query all Credential in the ReceiverAccountss table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ReceiverAccount ")

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_Personal_Profile(conn , UserID):
    """
    Query ReceiverAccounts by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM ReceiverAccount WHERE AdmNumber=?", (UserID,))
    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_Certification_Field(conn , UserID):
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT Certification  FROM ReceiverAccount WHERE AdmNumber=?", (UserID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return str(Credential)



def Query_Persona_Schema(conn , Certificate , CourseWork , Semester , Criteria):
    """
    Query ReceiverAccounts by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM ReceiverAccount WHERE Certification=? AND Course=? AND Module=? AND AccountStatus=? ", (Certificate,CourseWork,Semester,Criteria))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return list(Credential)




def Retreive_Course_Field(conn , UserID):
    """
    Query ReceiverAccounts by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT Course  FROM ReceiverAccount WHERE AdmNumber=?", (UserID,))
    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return str(Credential)





def Retreive_Semester_Field(conn , UserID):
    """
    Query ReceiverAccounts by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT Module FROM ReceiverAccount WHERE AdmNumber=?", (UserID,))
    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return str(Credential)
def Query_User_Existence(conn, UserID):
    """
    Query ReceiverAccountss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT UserID FROM ReceiverAccount WHERE UserID=?", (UserID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

def Query_CryptoHash_Existence(conn, SecureID):
    """
    Query ReceiverAccountss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT SecureID FROM ReceiverAccount WHERE SecureID=?", (SecureID,))

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
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT Verification FROM ReceiverAccount WHERE Verification=?", (SecureString,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;




def Remove_User_Profile(conn, UserID):
    """
    Delete a ReceiverAccounts by ReceiverAccounts id
    :param conn:  Connection to the SQLite database
    :param id: id of the ReceiverAccounts
    :return:
    """
    sql = 'DELETE FROM ReceiverAccount WHERE UserID = ?'
    cur = conn.cursor()
    cur.execute(sql, ( UserID ,))
    conn.commit()




conn = create_connection("./static/Databases/backup.db")

#Retreive_User_Profiles(conn)
##Retreive_Education_Profile(conn , "merlin")
#Query_Persona_Schema(conn ,"All" , "All" , 3 , "Active")
#Alpha =( "435435-XDK-9S90" , "Clyde Javis" , "Ahoya", "Test" ,"Test", "Test", "Test" , "Test" , "Test", "Test", "Test" )
#Create_UserProfile(conn , Alpha )

#Remove_User_Profile(conn , "435435-XDK-9S90")
