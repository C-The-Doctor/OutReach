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
def Create_Survey_Data_Profiles(conn , TransitCredential):
    """
    Create a new Survey_Data_Profile into the Survey_Data_Profiles table
    :param conn:
    :param Survey_Data_Profile:
    :return: Survey_Data_Profile id
    """



    sql = ''' INSERT INTO  Survey_Data_Profile(SurveyID , SurveyType , TagDepartment , TagCourse , TagCertification , TagModule , Gender , SurveyQ1 , SurveyQ2 , SurveyQ3 , SurveyQ4 , SurveyQ5 , SurveyOwner , StartTime , Endtime , OperationStatus  )
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,"Not-Determined", "Running") '''

    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, TransitCredential)
        conn.commit()
        conn.close
    return "Success"




def Retreive_Survey_Data_Profiles(conn , OwnerID ):
    """
    Query all Credential in the Survey_Data_Profiles table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Survey_Data_Profile WHERE SurveyOwner=?", (OwnerID,))
    DataChunk = []
    Credential = cur.fetchall()
    for x in Credential:
        DataChunk.append(x)
    return DataChunk


def Retreive_Survey_ID(conn):
    """
    Query Survey_Data_Profile by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT SurveyID FROM Survey_Data_Profile" )

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Query_User_Existence(conn, SurveyID):
    """
    Query Survey_Data_Profiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT SurveyID FROM Survey_Data_Profile WHERE SurveyID=?", (SurveyID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

def Retrieve_User_Survey(conn, Owner_Profile):
    """
    Query Survey_Data_Profiles by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM Survey_Data_Profile WHERE SurveyOwner=?", (Owner_Profile,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;






def Remove_Survey_Data_Profile(conn, SurveyID):
    """
    Delete a Survey_Data_Profile by Survey_Data_Profile id
    :param conn:  Connection to the SQLite database
    :param id: id of the Survey_Data_Profile
    :return:
    """
    sql = 'DELETE FROM Survey_Data_Profile WHERE SurveyID = ?'
    cur = conn.cursor()
    cur.execute(sql, ( SurveyID ,))
    conn.commit()




conn = create_connection("./static/Databases/backup.db")

Retreive_Survey_Data_Profiles(conn , "max")


#Alpha =( "435435-XDK-9sdS90" , "Clyde Javis" , "Ahoya", "Test" ,"Test", "Test", "Test" ,  "Test", "Test", "Test" , "Gerd" , "sdjsd" , "yuaisa" , "sdksd")
#Create_Survey_Data_Profiles(conn , Alpha )

#Remove_Survey_Data_Profile(conn , "435435-XDK-9S90")
