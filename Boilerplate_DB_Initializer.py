import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def Database_Init_Override(Masterpath):
    Storage_UNIT = Masterpath

    Receiver_Account_Center  = """ CREATE TABLE IF NOT EXISTS ReceiverAccount(
                                        AdmNumber text NOT NULL,
                                        FullName text NOT NULL,
                                        PhoneContact text NOT NULL,
                                        AltContact text NOT NULL,
                                        Gender text NOT NULL,
                                        Certification text NOT NULL,
                                        Course text NOT NULL,
                                        Module text NOT NULL,
                                        UserID text NOT NULL,
                                        SecureID text NOT NULL,
                                        Verification text NOT NULL ,
                                        AccountStatus text NOT NULL
                                    ); """

    Master_Account_Center  = """CREATE TABLE IF NOT EXISTS MasterAccount(


                                        FullName text NOT NULL ,
                                        PhoneContact text NOT NULL ,
                                        AltContact text NOT NULL ,
                                        Department text NOT NULL ,
                                        Course text NOT NULL ,
                                        Designation text NOT NULL ,
                                        UserID text NOT NULL ,
                                        SecureID text NOT NULL ,
                                        Verification text NOT NULL


                                    );"""



    Link_Manager_Center  = """CREATE TABLE IF NOT EXISTS UploadLinks(

                                        LinkID text NOT NULL,
                                        LinkTitle text NOT NULL ,
                                        TagCertification text NOT NULL,
                                        TagCourse text  NOT NULL,
                                        TagModule text NOT NULL,
                                        Validity text NOT NULL,
                                        Descriptor text NOT NULL,
                                        LinkOwner text NOT NULL,
                                        Timelapse text NOT NULL,
                                        Status text NOT NULL ,
                                        Sharebox text NOT NULL ,
                                        LinkSize text NOT NULL,
                                        JoinLink text NOT NULL
                                    );"""



    Departments_Center  = """CREATE TABLE IF NOT EXISTS DepartmentsProfile(
                                        DepartmentCode text NOT NULL  PRIMARY KEY,
                                        DepartmentName text NOT NULL,
                                        DepartmentAdmin text  NOT NULL

                                    );"""



    Courses_Center     = """CREATE TABLE IF NOT EXISTS CoursesProfile(
                                        CourseCode text NOT NULL PRIMARY KEY,
                                        CourseName text NOT NULL,
                                        DepartmentCode text NOT NULL ,
                                        Modularity text NOT NULL,
                                        Category text NOT NULL

                                    );"""







    Dispatch_Center     = """CREATE TABLE IF NOT EXISTS MessageLogs(
                                        MID text NOT NULL PRIMARY KEY,
                                        Platform text NOT NULL,
                                        MessAuthor text NOT NULL,
                                        TargetDepartment  text NOT NULL ,
                                        TargetCourse text NOT NULL,
                                        TargetCertification text NOT NULL,
                                        TargetYear text NOT NULL,
                                        AccountState text NOT NULL,
                                        Attachments text NOT NULL,
                                        Message text NOT NULL ,
                                        
                                        TimeStamp text NOT NULL ,
                                        OperationTally text NOT NULL ,
                                        OperationStatus text NOT NULL

                                    );"""


    Survey_Center    = """CREATE TABLE IF NOT EXISTS Survey_Data_Profile(
                                        SurveyID text NOT NULL PRIMARY KEY,
                                        SurveyType text NOT NULL,
                                        TagDepartment  text NOT NULL ,
                                        TagCourse  text NOT NULL ,
                                        TagCertification text NOT NULL ,
                                        TagModule text NOT NULL,
                                        Gender text NOT NULL,
                                        SurveyQ1 text NOT NULL ,
                                        SurveyQ2 text NOT NULL ,
                                        SurveyQ3 text NOT NULL ,
                                        SurveyQ4 text NOT NULL ,
                                        SurveyQ5 text NOT NULL ,
                                        SurveyOwner text NOT NULL,
                                        StartTime text NOT NULL,
                                        EndTime text NOT NULL ,
                                        OperationStatus text NOT NULL

                                    );"""


    Response_Center     = """CREATE TABLE IF NOT EXISTS Response_Data_Profile(
                                        ResponseID text NOT NULL PRIMARY KEY,
                                        ResponseType text NOT NULL,
                                        OwnerID  text NOT NULL ,
                                        ResponseQ1  text NOT NULL ,
                                        ResponseQ2  text NOT NULL ,
                                        ResponseQ3  text NOT NULL ,
                                        ResponseQ4  text NOT NULL ,
                                        ResponseQ5  text NOT NULL ,
                                        Status text NOT NULL ,
                                        Timestamp text NOT NULL


                                    );"""

    Group_Center     = """CREATE TABLE IF NOT EXISTS Group_Data_Profile(
                                        GroupID text NOT NULL PRIMARY KEY,
                                        GroupName text NOT NULL,
                                        GroupOwner  text NOT NULL ,
                                        GroupCategory text NOT NULL ,
                                        GroupDescription text NOT NULL,
                                        TimeStamp text NOT NULL ,
                                        Activities int NOT NULL ,
                                        Files int NOT NULL ,
                                        Associates int NOT NULL

                                    );"""




    Activities_Center     = """CREATE TABLE IF NOT EXISTS Activity_Data_Profile(
                                        ActivityID text NOT NULL ,
                                        ActivityName text NOT NULL,
                                        AddInformation  text NOT NULL ,
                                        Venue text NOT NULL ,
                                        StartTime int NOT NULL ,
                                        EndTime text NOT NULL ,
                                        DisplayStatus text NOT NULL ,
                                        OwnerID text NOT NULL ,
                                        ActivityStatus text NOT NULL

                                    );"""



    Associates_Center     = """CREATE TABLE IF NOT EXISTS Associate_Data_Profile(
                                        AssociateID text NOT NULL ,
                                        GroupID text NOT NULL,
                                        AccountType text NOT NULL ,
                                                  Timestamp  text NOT NULL

                                   );"""


    Requests_Center= """CREATE TABLE IF NOT EXISTS Request_Data_Profile(
                                        RequestID text NOT NULL PRIMARY KEY,
                                        OwnerID text NOT NULL,
                                        OwnerProfile text NOT NULL ,
                                        OwnerContact text NOT NULL,
                                        RequestHandle text NOT NULL ,
                                        Timestamp  text NOT NULL

                                    );"""



    # create a database connection
    conn = create_connection(Storage_UNIT)

    if conn is not None:
        # create projects table
        create_table(conn, Receiver_Account_Center )

        # create tasks table
        create_table(conn, Master_Account_Center)

        # create tasks table
        create_table(conn, Link_Manager_Center )

        # create tasks table
        create_table(conn, Departments_Center )

        # create tasks table
        create_table(conn, Courses_Center )

        # create tasks table
        create_table(conn, Dispatch_Center)

         # create tasks table
        create_table(conn, Survey_Center)

         # create tasks table
        create_table(conn, Response_Center)


         # create tasks table
        create_table(conn, Group_Center )


         # create tasks table
        create_table(conn, Activities_Center )


         # create tasks table
        create_table(conn, Associates_Center )

     # create tasks table
        create_table(conn, Requests_Center )







    else:
        print("Error! cannot create the database connection.")

Database_Init_Override("./static/Databases/backup.db")
