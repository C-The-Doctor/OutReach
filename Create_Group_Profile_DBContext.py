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
def Create_Group_Data_Profiles(conn , TransitCredential):
    """
    Create a new Group_Data_Profile into the Group_Data_Profiles table
    :param conn:
    :param Group_Data_Profile:
    :return: Group_Data_Profile id
    """



    sql = ''' INSERT INTO  Group_Data_Profile(GroupID , GroupName , GroupOwner, GroupDescription , GroupCategory , TimeStamp , Activities , Files  , Associates )
    VALUES(?,?,?,?,?,?,0,0,0) '''

    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, TransitCredential)
        conn.commit()
        conn.close
    return "Success"




def Retreive_Group_Data_Profiles(conn):
    """
    Query all Credential in the Group_Data_Profiles table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Group_Data_Profile ")

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential



def Retreive_Groups_By_Owner(conn , Res_Owner):
    """
    Query all Credential in the Group_Data_Profiles table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Group_Data_Profile WHERE GroupOwner=?", (Res_Owner,))


    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential

def Retreive_Group_Size(conn , Res):
    """
    Query all Credential in the Group_Data_Profiles table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT Associates FROM Group_Data_Profile WHERE GroupID=?", (Res,))


    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential

def Retreive_Group_Creation(conn , Res):
    """
    Query all Credential in the Group_Data_Profiles table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT TimeStamp FROM Group_Data_Profile WHERE GroupID=?", (Res,))


    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return str(Credential).strip("[]()','")

def Retreive_Group_Token(conn , Shaft):
    """
    Query Group_Data_Profile by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT GroupName FROM Group_Data_Profile WHERE GroupID=?", (Shaft,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return str(Credential).strip("[]()','")


def Retreive_Group_Record(conn, Res):
    """
    Query Group_Data_Profiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn.row_factory = lambda cursor , row : row    
    cur = conn.cursor()
    cur.execute("SELECT * FROM Group_Data_Profile WHERE GroupID IN (?)", (Res,))

    Credential = cur.fetchall()\

    for DataChunk in Credential:
        print(DataChunk)

    return str(Credential)

def Retrieve_User_Group(conn, Owner_Profile):
    """
    Query Group_Data_Profiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM Group_Data_Profile WHERE GroupOwner=?", (Owner_Profile,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;




def Retreive_Group_Data(conn, ResData):

    """
    Delete a Group_Data_Profile by Group_Data_Profile id
    :param conn:  Connection to the SQLite database
    :param id: id of the Group_Data_Profile
    :return:
    """
    sql = 'SELECT * FROM  Group_Data_Profile WHERE GroupID IN (?)'
    cur = conn.cursor()
    cur.execute(sql, (str(ResData),))
    conn.commit()



def Remove_Single_Data_Profile(conn, ResID):
    """
    Delete a Group_Data_Profile by Group_Data_Profile id
    :param conn:  Connection to the SQLite database
    :param id: id of the Group_Data_Profile
    :return:
    """
    sql = 'DELETE FROM Group_Data_Profile WHERE GroupID = ?'
    cur = conn.cursor()
    cur.execute(sql, ( ResID ,))
    conn.commit()




conn = create_connection("./static/Databases/backup.db")

#Retreive_Group_Data(conn  , "DNA-001"  )

#Retreive_Group_Data_Profiles(conn)
#Alpha =( "4s35-sd-asdS90" , " Javis" , "Ahoya", "Test"est","6:03:45 PM")
#Create_Group_Data_Profiles(conn , Alpha )

#Remove_Group_Data_Profile(conn , "435435-XDK-9S90")
d = 'DXB-2345'
Retreive_Group_Record(conn , d  )
