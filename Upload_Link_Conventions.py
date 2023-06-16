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
def Create_UploadLinks(conn , TransitCredential):
    """
    Create a new UploadLinks into the UploadLinks table
    :param conn:
    :param UploadLinks:
    :return: UploadLinks id
    """



    sql = ''' INSERT INTO UploadLinks(LinkToken ,LinkID , LinkTarget ,LinkLevel , LinkPeriod ,  LinkLifeSpan ,  SessionLoadCount  , ExpectedLoadCount , LinkStatus , LinkAdmin  , DataProfile )
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, TransitCredential)
        conn.commit()
        conn.close
    return "Success"
   



def Update_UploadLinks(conn, UploadData):
    """
    update priority, begin_date, and end date of a UploadLinks
    :param conn:
    :param UploadLinks:
    :return: project id
    """
    sql = ''' UPDATE UploadLinks
              SET ExpectedLoadCount = ? ,
                  LinkStatus = ? ,  
              WHERE LinkToken = ?'''


    cur = conn.cursor()
    cur.execute(sql, UploadData)
    conn.commit()
    


def Retreive_UploadLinks(conn):
    """
    Query all Credential in the UploadLinks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM UploadLinks ")

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_Link_ID(conn):
    """
    Query UploadLinks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT LinkID FROM UploadLinks" )

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential 


def Query_Link_Existence(conn, LinkID):
    """
    Query UploadLinks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT LinkID FROM UploadLinks WHERE LinkID=?", (LinkID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

def Query_CryptoHash_Existence(conn, SecureID):
    """
    Query UploadLinks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT SecureID FROM UploadLinks WHERE SecureID=?", (SecureID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;






def Remove_UploadLinks(conn, LinkID):
    """
    Delete a UploadLinks by UploadLinks id
    :param conn:  Connection to the SQLite database
    :param id: id of the UploadLinks
    :return:
    """
    sql = 'DELETE FROM UploadLinks WHERE LinkID = ?'
    cur = conn.cursor()
    cur.execute(sql, ( LinkID ,))
    conn.commit()




conn = create_connection("./static/Databases/backup.db")

#Retreive_AllUploadLinks(conn)


#Alpha =( "4354fXDK-9S90" , "Clyde Javis" , "Ahoya", "Test" ,"Test", "Test", "Test" , "Test" , "Test", "Tryout" , "TrexDj" )
#Create_UploadLinks(conn , <div></div>Alpha )

#Remove_UploadLinks(conn , "435435-XDK-9S90")

