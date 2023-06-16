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
def Import_Explorer_Object(conn , DataUtility ):
    """
    Create a new Explorer into the Explorer table
    :param conn:
    :param Explorer:
    :return: Explorer id
    """

    conn = create_connection("./static/Databases/backup.db")

    sql = ''' INSERT INTO Explorer(FileID , FileName, FileType , FileHook , FileAdmin , FilePath, FileCount , TimeStamp , FileSize)
              VALUES(?,?,?,?,?,?,0,?,?) '''
    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, DataUtility)
        conn.commit()
       
    return "Success"
   
   


def Generate_Download_Link(conn , FileName ):
    """
    Query all Credential in the Explorerss table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT FilePath FROM Explorer WHERE  FileName = ? " , (FileName,))

    Credential = cur.fetchall()

   
    return Credential


def Extract_Explorer_Handles(conn):
    """
    Query Explorers by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Explorer" )

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential 


def Query_Object_Admin(conn, FileAdmin):
    """
    Query Explorerss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT FileName FROM Explorer WHERE FileAdmin=?", (FileAdmin,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

def Extract_Object_Associations(conn, FileType):
    """
    Query Explorerss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Explorer WHERE FileType=?", (FileType,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;






def Delete_Explorer_Object(conn, FileName):
    """
    Delete a Explorers by Explorers id
    :param conn:  Connection to the SQLite database
    :param id: id of the Explorers
    :return:
    """
    sql = 'DELETE FROM Explorer WHERE FileName = ?'
    cur = conn.cursor()
    cur.execute(sql, ( FileName ,))
    conn.commit()




conn = create_connection("./static/Databases/backup.db")




TestData  = ( "43543$-6t7ajajj9" , "Cl&-yde Javis" , "Ahoya", "Test" ,"Test", "Test" , "Test" , "Test")

#Import_Explorer_Object(conn , TestData )

#Delete_Explorer_Object(conn ,"435435-XDK-9S90")

