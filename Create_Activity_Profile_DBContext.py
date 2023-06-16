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
def Create_Activity_Data_Profiles(conn , TransitCredential):
    """
    Create a new Activity_Data_Profile into the Activity_Data_Profiles table
    :param conn:
    :param Activity_Data_Profile:
    :return: Activity_Data_Profile id
    """



    sql = ''' INSERT INTO  Activity_Data_Profile(ActivityID , ActivityName , AddInformation, Venue, StartTime , EndTime , DisplayStatus  , OwnerID  , ActivityStatus  )
    VALUES(?,?,?,?,?,?,?,?,?) '''

    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, TransitCredential)
        conn.commit()
        conn.close
    return "Success"




def Retreive_Activity_Data_Profiles(conn):
    """
    Query all Credential in the Activity_Data_Profiles table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Activity_Data_Profile ")

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_Activity_By_Gid(conn, Res):
    """
    Query Group_Data_Profiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Activity_Data_Profile WHERE ActivityID IN (?)", (Res,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

    return list(Credential)


def Retreive_Personal_Activity(conn , TagID):
    """
    Query Activity_Data_Profile by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Activity_Data_Profile WHERE ActivityID=?", (TagID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_Group_Activity(conn, Grp_ID ):
    """
    Query Activity_Owner_Profiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Activity_Data_Profile WHERE ActivityID=?", (Grp_ID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

def Retrieve_Activities_Status(conn, ActivityState):
    """
    Query Activity_Data_Profiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM Activity_Data_Profile WHERE ActivityStatus=?", (ActivityState,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;






def Remove_Activity_Data_Profile(conn, ResID):
    """
    Delete a Activity_Data_Profile by Activity_Data_Profile id
    :param conn:  Connection to the SQLite database
    :param id: id of the Activity_Data_Profile
    :return:
    """
    sql = 'DELETE FROM Activity_Data_Profile WHERE ActivityID = ?'
    cur = conn.cursor()
    cur.execute(sql, ( ResID ,))
    conn.commit()




conn = create_connection("./static/Databases/backup.db")

#Retreive_Activity_Data_Profiles(conn)


#Alpha =( "34534533434" , "Skunking Till Midnight " ," Channelling Your Inner Self Thru Smoke   " , "Cimbitido's Den", "12/02/3014:Thursday" ,"4/52/3024:Friday" , "Present" , "Felicia" , "Completed")
#Create_Activity_Data_Profiles(conn , Alpha )

#Remove_Activity_Data_Profile(conn , "435435-XDK-9S90")
