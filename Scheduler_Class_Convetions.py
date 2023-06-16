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
def Create_SchedulerProfiles(conn , TransitCredential):
    """
    Create a new SchedulerProfile into the SchedulerProfiles table
    :param conn:
    :param SchedulerProfile:
    :return: SchedulerProfile id
    """



    sql = ''' INSERT INTO    SchedulerProfile(ScheduleName,ParentCourse,CourseLevel,CoursePeriod,AdmissionTime,StartTime,Expiration ,ScheduleAuthor,ResponseFreq ,ProcessStart,ProcessInterval,ProcessFinish,DataFallBack)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    
    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, TransitCredential)
        conn.commit()
        conn.close
    return "Success"
   



def Update_SchedulerProfiles(conn, ClassProfiles):
    """
    update priority, begin_date, and end date of a SchedulerProfile
    :param conn:
    :param SchedulerProfile:
    :return: project id
    """
    sql = ''' UPDATE SchedulerProfile
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
    


def Retreive_SchedulerProfiles(conn):
    """
    Query all Credential in the SchedulerProfiles table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM SchedulerProfile ")

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_User_ID(conn):
    """
    Query SchedulerProfile by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT UserID FROM SchedulerProfile" )

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential 


def Query_User_Existence(conn, UserID):
    """
    Query SchedulerProfiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT UserID FROM SchedulerProfile WHERE UserID=?", (UserID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

def Query_CryptoHash_Existence(conn, SecureID):
    """
    Query SchedulerProfiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT SecureID FROM SchedulerProfile WHERE SecureID=?", (SecureID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;






def Remove_SchedulerProfile(conn, UserID):
    """
    Delete a SchedulerProfile by SchedulerProfile id
    :param conn:  Connection to the SQLite database
    :param id: id of the SchedulerProfile
    :return:
    """
    sql = 'DELETE FROM SchedulerProfile WHERE UserID = ?'
    cur = conn.cursor()
    cur.execute(sql, ( UserID ,))
    conn.commit()




conn = create_connection("./static/Databases/backup.db")

#Retreive_AllSchedulerProfiles(conn)


Alpha =( "435435-XDK-9S90" , "Clyde Javis" , "Ahoya", "Test" ,"Test", "Test", "Test" , "Test" , "Test", "Test", "Test", "Test" , "Gerd")
Create_SchedulerProfiles(conn , Alpha )

#Remove_SchedulerProfile(conn , "435435-XDK-9S90")

