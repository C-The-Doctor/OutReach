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
def Create_Request_Data_Profiles(conn , TransitCredential):
    """
    Create a new Request_Data_Profile into the Request_Data_Profiles table
    :param conn:
    :param Request_Data_Profile:
    :return: Request_Data_Profile id
    """



    sql = ''' INSERT INTO  Request_Data_Profile(RequestID , OwnerID ,  OwnerProfile  , OwnerContact,  RequestHandle ,  TimeStamp)
    VALUES(?,?,?,?,?,?) '''

    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, TransitCredential)
        conn.commit()
        conn.close
    return "Success"




def Retreive_Request_Data_Profiles(conn):
    """
    Query all Credential in the Request_Data_Profiles table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Request_Data_Profile ")

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_Request_ID(conn):
    """
    Query Request_Data_Profile by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT RequestID FROM Request_Data_Profile" )

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_Single_Request(conn, UserID ):
    """
    Query Request_Data_Profiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT RequestID FROM Request_Data_Profile WHERE RequestID=?", (UserID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

def Retrieve_Block_Activities(conn, Creator_Profile):
    """
    Query Request_Data_Profiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM Request_Data_Profile WHERE RequestCreator=?", (Creator_Profile,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;






def Remove_Request_Data_Profile(conn, ResID):
    """
    Delete a Request_Data_Profile by Request_Data_Profile id
    :param conn:  Connection to the SQLite database
    :param id: id of the Request_Data_Profile
    :return:
    """
    sql = 'DELETE FROM Request_Data_Profile WHERE RequestID = ?'
    cur = conn.cursor()
    cur.execute(sql, ( ResID ,))
    conn.commit()




#conn = create_connection("./static/Databases/backup.db")

#Retreive_Request_Data_Profiles(conn)

#Alpha =( "4fdf5-dS" , "Kike Himenez" , "Jimenez", "Test" ,"Battle Hardened In Nebraska For Some Hot Pussy " , "Tester")
#Create_Request_Data_Profiles(conn , Alpha )

#Remove_Request_Data_Profile(conn , "435435-XDK-9S90")
