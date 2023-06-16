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
def Record_Dispatch_Events(conn , DataUtility ):
    """
    Create a new Dispatch into the Dispatch table
    :param conn:
    :param Dispatch:
    :return: Dispatch id
    """

    conn = create_connection("./static/Databases/backup.db")

    sql = ''' INSERT INTO MessageLogs(MID , Platform  , MessAuthor , TargetDepartment , TargetCourse , TargetCertification   , TargetYear , AccountState , Attachments , Message , TimeStamp ,  OperationTally , OperationStatus )
              VALUES(?,?,?,?,?,?,?,?,?,?, "23-4-2023 12;00" ,"100", "Running") '''
    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, DataUtility)
        conn.commit()

    return "Success"




def Retreive_Dispatch_Events(conn):
    """
    Query all Credential in the MessageLogsss table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM MessageLogs ")

    Credential = cur.fetchall()


    return Credential


def Retreive_Dispatch_Handles(conn):
    """
    Query MessageLogss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM MessageLogs" )

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Query_Event_Existence(conn, MessageID):
    """
    Query MessageLogsss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT MID FROM MessageLogs WHERE MID=?", (MessageID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

def Retreive_Parent_Dispatch(conn, MessageAdmin):
    """
    Query MessageLogsss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM MessageLogs WHERE MessAuthor=?", (MessageAdmin,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

# Collatting Returns a Tuple , We Need A Different Way  To Hold Tge Returned Items
# We Could , Retreive Each Record Independententlu ThenStitch Into A List
def Retreive_Dispatch_Relative(conn, Certification , Course , Year):
    """
    Query MessageLogsss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM MessageLogs WHERE (TargetCertification=? AND TargetCourse=? AND TargetYear=?)", (Certification , Course, Year,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return list(Credential);







def Delete_Dispatch_Events(conn, MessageID):
    """
    Delete a MessageLogss by MessageLogss id
    :param conn:  Connection to the SQLite database
    :param id: id of the MessageLogs
    :return:
    """
    sql = 'DELETE FROM MessageLogs WHERE MID = ?'
    cur = conn.cursor()
    cur.execute(sql, ( MessageID ,))

    conn.commit()




conn = create_connection("./static/Databasesbackup.db")



#Retreive_Dispatch_Handles(conn)
#Retreive_Dispatch_Relative(conn , "All"  , "All" , "5")
#Alpha =( "ksksdhhshshdhs" , "Clyde Javis" , "Ahoya", "Test" ,"Test", "Test", "Test" , "Test", "Test", "Test3" , "Test4" , "Roader","Test4", "Testesj" )
#Record_Dispatch_Events(conn , Alpha )

#Remove_User_Profile(conn , "435435-XDK-9S90")
