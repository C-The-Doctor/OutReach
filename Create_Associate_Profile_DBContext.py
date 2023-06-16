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
def Create_Associate_Data_Profiles(conn , TransitCredential):
    """
    Create a new Associate_Data_Profile into the Associate_Data_Profiles table
    :param conn:
    :param Associate_Data_Profile:
    :return: Associate_Data_Profile id
    """



    sql = ''' INSERT INTO  Associate_Data_Profile(AssociateID , GroupID ,  AccountType  ,TimeStamp)
    VALUES(?,?,?,?) '''

    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql,TransitCredential)
        conn.commit()
        conn.close
    return "Success"




def Retreive_Associate_Data_Profiles(conn):
    """
    Query all Credential in the Associate_Data_Profiles table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Associate_Data_Profile ")

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_Associate_ID(conn):
    """
    Query Associate_Data_Profile by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT AssociateID FROM Associate_Data_Profile" )

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_Group_Listings(conn, UsrID ):
    """
    Query Associate_Data_Profiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT GroupID FROM Associate_Data_Profile WHERE AssociateID=?", (UsrID,))

    Credential = cur.fetchall()
    for DataChunk in Credential:
        print(DataChunk)

    return Credential;

def Retreive_Group_Members(conn, Grp_ID):
    """
    Query Associate_Data_Profiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM Associate_Data_Profile WHERE GroupID=?", (Grp_ID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

    return Credential;






def Remove_Associate_Data_Profile(conn, ResID):
    """
    Delete a Associate_Data_Profile by Associate_Data_Profile id
    :param conn:  Connection to the SQLite database
    :param id: id of the Associate_Data_Profile
    :return:
    """
    sql = 'DELETE FROM Associate_Data_Profile WHERE AssociateID = ?'
    cur = conn.cursor()
    cur.execute(sql, ( ResID ,))
    conn.commit()




conn = create_connection("./static/Databases/backup.db")

#Retreive_Associate_Data_Profiles(conn)
#Retreive_Group_Listings(conn , "merlin")
#Alpha =( "Devld" , "345sds2334" , "Member", "2:34:38 PM 2023")
#Create_Associate_Data_Profiles(conn , Alpha )

#Remove_Associate_Data_Profile(conn , "435435-XDK-9S90")
