from flask import Flask  , url_for , render_template , request , redirect
from flask.views import View
from flask import g
#from twilio.rest import Client
import os , random , string
from werkzeug.utils  import secure_filename
import time
import sqlite3
from sqlite3 import Error
import uuid
import datetime
import TimeCop as Generate_Timestamp
import Creator as File_Stream_Handle

import Create_ReceiverAccount_DBContext as Register_New_Receiver
import Create_MasterAccount_DBContext as Register_New_Master
import Dispatch_Class_Conventions as Access_Dispatch_Stream
import Create_Link_DBContext as Register_Upload_Link
import Create_Group_Profile_DBContext as Group_Profile_Handler
import Create_Survey_Profile_DBContext as Survey_Profile_Handler
import Create_Request_Profile_DBContext as Request_Profile_Handler
import Create_Associate_Profile_DBContext as Associate_Profile_Handler
import Create_Activity_Profile_DBContext as Activity_Profile_Handler

import Twilio_Content_Provider as Twilio_Service

app=Flask(__name__)


# Global Attributes & Containers
Operator_Storage_Handle= os.path.join(app.static_folder , "") + "Data\Explorer\Operator-Container"
Receiver_Storage_Handle = os.path.join(app.static_folder , "") + "Data\Explorer\Receiver-Container"
Public_Storage_Handle = os.path.join(app.static_folder , "") + "Data\Explorer"
Private_Storage_Handle = os.path.join(app.static_folder , "") + "Data\Explorer\Receiver-Container"
Message_Dispatch = os.path.join(app.static_folder , "") + "/Explorer/DispatchStreams"
Operator_Storage_Hook = os.path.join(app.static_folder , "") + "/Data/Explorer/Operator-Container/"
Submission_Storage_Hook = os.path.join(app.static_folder , "") + "/Data/Upload_Links/"
TableStorage =os.path.join(app.static_folder , "") + "/Explorer/Table.txt"
Unfinished_Data_Scheme = os.path.join(app.static_folder , "") + "/images/beef"


# Liquid Configurations

app.config['Operator']=Operator_Storage_Handle
app.config['Receiver']=Receiver_Storage_Handle
app.config['Private']=Private_Storage_Handle
app.config['Public']=Public_Storage_Handle
app.config['DispatchStorage']=Message_Dispatch
app.config['Operator_Storage_Path']=Operator_Storage_Hook
app.config['Submission_Storage_Path']=Submission_Storage_Hook
#Get - User Data Location
def DestinationUser(Handle ,Username):
    String =os.path.join(Handle , Username  )
    Expanded_String = os.path.join(String , "Pool-Resources")
    return str(Expanded_String)


def Public_Storage(Handle):
    String =str(Handle)
    Expanded_String = os.path.join(String , "Public-Storage-Container")
    return str(Expanded_String)



def Private_Storage(Handle , Username):
    Basepath = str("Security-Wallet")
    String =os.path.join(Handle , Username )
    Expanded_String = os.path.join(String , Basepath)
    return str(Expanded_String)





def Submission_Storage(Handle , LinkID):
    Expanded_String =os.path.join(Handle , LinkID )
    return str(Expanded_String)

def Generate_Secure_Token():
   Token_Hash = uuid.uuid4()
   return str(Token_Hash)


def Return_Twilio_Balance():
    client = Client()
    balance_data = client.api.v2010.balance.fetch()
    balance = float(balance_data.balance)
    currency = balance_data.currency

    AccountBalance = f'Your account has {balance:.2f}{currency} left.'

# app name
@app.errorhandler(404)

# inbuilt function which takes error as parameter
def not_found(e):

# defining function
  return render_template("404.html")



@app.route("/Link/<string:UniqueID>")
def Link(UniqueID):
    Connection_Manager  =  Register_Upload_Link.create_connection("./static/Databases/backup.db")
    ObjectData = Register_Upload_Link.Query_Link_Existence(Connection_Manager , UniqueID )
    return render_template("LinkInformation.html" , ObjectData=ObjectData )



@app.route("/UploadBin/<string:UniqueID>")
def UploadBin(UniqueID):
    Session_Profile = UniqueID
    return render_template("Upload_Police.html" , Session_Profile = Session_Profile  )




@app.route("/Submission/<string:UniqueID>")
def Submission(UniqueID):
    Session_Profile = UniqueID
    return render_template("Submission_Link_Plate.html" , Session_Profile = Session_Profile  )


@app.route("/Surveys/<string:UniqueID>")
def Surveys(UniqueID):
    Session_Profile = UniqueID
    Connection_Manager  =  Survey_Profile_Handler.create_connection("./static/Databases/backup.db")
    Survey_Data = Survey_Profile_Handler.Retreive_Survey_Data_Profiles(Connection_Manager , Session_Profile  )
    Survey_Limit = int(len(Survey_Data))
    return render_template("Survey_Listings.html" , Survey_Data=Survey_Data , Session_Profile = Session_Profile )



@app.route("/Links/<string:UniqueID>")
def Links(UniqueID):
    Session_Profile = UniqueID
    Connection_Manager  =  Register_Upload_Link.create_connection("./static/Databases/backup.db")
    Link_Data_Tree=Register_Upload_Link.Query_Link_Owner(Connection_Manager , Session_Profile)
    Link_Limit = int(len(Link_Data_Tree))
    return render_template('Captive_Links_View.html' , Link_Data_Tree = Link_Data_Tree ,  Link_Limit = Link_Limit , Session_Profile = Session_Profile )






@app.route("/GroupSend/<string:UniqueID>")
def GroupSend(UniqueID):
    Connection_Manager  =  Register_Upload_Link.create_connection("./static/Databases/backup.db")
    Session_Profile = UniqueID
    Explorer_Data = Register_Upload_Link.Query_Link_Existence(Connection_Manager , UniqueID )
    return render_template("Group_Send_Options.html" , Explorer_Data=Explorer_Data ,Session_Profile=Session_Profile  )



@app.route("/Explorer/<string:UniqueID>")
def Explorer(UniqueID):
    Session_Profile = UniqueID
    Data_Layer = DestinationUser(Operator_Storage_Handle ,UniqueID)
    Data_Links = os.listdir(Data_Layer)
    print(Data_Layer)
    for x in Data_Links:
        print(x)
    Data_Length = int(len(Data_Links))

    return render_template("Explorer_3D.html" , Session_Profile = Session_Profile , Data_Links = Data_Links , Data_Length = Data_Length  )



@app.route("/PublicPool/<string:UniqueID>")
def PublicPool(UniqueID):
    Session_Profile = UniqueID
    Data_Layer = Public_Storage(Public_Storage_Handle)
    Data_Links = os.listdir(Data_Layer)
    print(Data_Layer)
    for x in Data_Links:
        print(x)
    Data_Length = int(len(Data_Links))

    return render_template("Explorer_3D.html" , Session_Profile = Session_Profile , Data_Links = Data_Links , Data_Length = Data_Length  )




@app.route("/Groupings/<string:UniqueID>")
def Groupings(UniqueID):
    Session_Profile = UniqueID
    Connection_Manager  =  Group_Profile_Handler.create_connection("./static/Databases/backup.db")
    Returned = Group_Profile_Handler.Retreive_Groups_By_Owner(Connection_Manager , UniqueID )
    Group_Limit = int(len(Returned))
    return render_template("PublicProfiles.html" , Returned=Returned , Group_Limit=Group_Limit ,  Session_Profile=Session_Profile  )


#Rewrite
#Captive
@app.route("/Group/<string:UniqueID>")
def Group(UniqueID):
    Connection_Manager  =  Register_Upload_Link.create_connection("./static/Databases/backup.db")
    Session_Profile = UniqueID
    ObjectData = Register_Upload_Link.Query_Link_Existence(Connection_Manager , UniqueID )
    return render_template("DefineClubs.html",  ObjectData=ObjectData , Session_Profile=Session_Profile  )


@app.route("/Groups/<string:UniqueID>")
def Groups(UniqueID):
    Session_Profile = UniqueID
    Connection_Manager = Associate_Profile_Handler.create_connection("./static/Databases/backup.db")
    Connection_Manager_Group = Group_Profile_Handler.create_connection("./static/Databases/backup.db")
    Shelve = Associate_Profile_Handler.Retreive_Group_Listings(Connection_Manager , Session_Profile )
    Group_Records = []
    Group_Data_Schema = []
    for Elem in Shelve:
        Group_Records.append(str(Elem).strip("()','"))
    for Schema in Group_Records:
        Sub =Group_Profile_Handler.Retreive_Group_Record(Connection_Manager_Group , Schema)
        Group_Data_Schema.append(Sub)

    print("This Is Elem 1 " , (Group_Data_Schema[0]))
    print("This Is :" , Group_Data_Schema)
    Group_Tally = len(Group_Data_Schema)
    return render_template('GroupProfiles.html' , Group_Data_Schema=Group_Data_Schema , Group_Tally=Group_Tally , Session_Profile =Session_Profile )


@app.route("/JoinLink/<string:UniqueID>")
def JoinLink(UniqueID):
    Connection_Manager  =  Register_Upload_Link.create_connection("./static/Databases/backup.db")
    GroupName =Register_Upload_Link.Query_Link_Existence(Connection_Manager , UniqueID )
    GroupTag = "Path To Image"
    return render_template("QR_Client_Lookup.html" , GroupTag = GroupTag , GroupName=GroupName)



@app.route("/Activities/<string:UniqueID>")
def Activities(UniqueID):
    # Problem UniqueID Has to be the users username , yet im using dna-001 which is a group name , so
    #what if he has multiple groups how will we access , we need to retreive group id based on his memberships then query activities
    #but were getting string issues
    Connection_Manager_Activity =Activity_Profile_Handler.create_connection("./static/Databases/backup.db")
    Activity_Session_Profiles=Activity_Profile_Handler.Retreive_Personal_Activity(Connection_Manager_Activity , UniqueID)
    return render_template("Personal_Activity_Profiles.html" , Activity_Session_Profiles =Activity_Session_Profiles)



@app.route("/Dashboard/<string:UniqueID>")
def Dashboard(UniqueID):
     Session_Profile = UniqueID
     Connection_Manager = Access_Dispatch_Stream.create_connection("./static/Databases/backup.db")
     UserProfile = UniqueID
     Conversation_Data= Access_Dispatch_Stream.Retreive_Dispatch_Events(Connection_Manager)
     Request_Data =Request_Profile_Handler.Retreive_Request_Data_Profiles(Connection_Manager)
     DataStatus = ""
     DataIndex = len(Conversation_Data)
     if DataIndex <  1 :
         DataStatus = "True"

     RequestStatus = ""
     RequestIndex = len(Request_Data)
     if RequestIndex <  1 :
         RequestStatus = "True"

     return render_template('Dashboard.html', UserProfile=UserProfile, Conversation_Data=Conversation_Data , DataStatus=DataStatus , RequestStatus=RequestStatus, Request_Data=Request_Data , Session_Profile = Session_Profile)





@app.route("/TKNP/<string:UniqueID>")
def TKNP(UniqueID):
     Connection_Manager = Group_Profile_Handler.create_connection("./static/Databases/backup.db")
     Connection_Manager_v5 = Register_New_Receiver.create_connection("./static/Databases/backup.db")
     Connection_Manager_V2 = Access_Dispatch_Stream.create_connection("./static/Databases/backup.db")
     Connection_Manager_Listings = Associate_Profile_Handler.create_connection("./static/Databases/backup.db")
     Connection_Manager_Profile = Register_New_Receiver.create_connection("./static/Databases/backup.db")
     Connection_Manager_Activity =Activity_Profile_Handler.create_connection("./static/Databases/backup.db")

     Group_Data_Schema = Group_Profile_Handler.Retreive_Group_Data_Profiles(Connection_Manager)
     Certification= Register_New_Receiver.Retreive_Certification_Field(Connection_Manager_v5 , UniqueID)
     Course= Register_New_Receiver.Retreive_Course_Field(Connection_Manager_v5 , UniqueID)
     Semester= Register_New_Receiver.Retreive_Semester_Field(Connection_Manager_v5 , UniqueID)
     Cert=str(Certification).strip("[](),''")
     Crs=str(Course).strip("[](),''")
     Sem=str(Semester).strip("[](),''")

     Conversation_Data= Access_Dispatch_Stream.Retreive_Dispatch_Relative(Connection_Manager_V2 , Cert , Crs , 3)
    # for Entry  in Conversation_Data:
        # print(Entry)
    # print(" List Ended Here")
     Subscribed_Activity_List = Activity_Profile_Handler.Retreive_Activity_Data_Profiles(Connection_Manager_Activity)
     print(Subscribed_Activity_List)

     #print(Subscribed_Activity_List)
     Profile_Data = Register_New_Receiver.Retreive_Personal_Profile(Connection_Manager_Profile , UniqueID)
     Session_Profile = UniqueID
     MessageData=[1,2,3,4,5,6,7,8,9]
     return render_template('Captive_Profile_Dashboard.html', Session_Profile=Session_Profile, MessageData=MessageData , Group_Data_Schema=Group_Data_Schema , Conversation_Data = Conversation_Data  , Profile_Data = Profile_Data , Subscribed_Activity_List = Subscribed_Activity_List )




@app.route("/DisplayClubs/<string:UniqueID>")
def DisplayClubs(UniqueID):
     Connection_Manager =Group_Profile_Handler.create_connection("./static/Databases/backup.db")
     Connection_Manager_Pipe =Associate_Profile_Handler.create_connection("./static/Databases/backup.db")
     Connection_Manager_Activity =Activity_Profile_Handler.create_connection("./static/Databases/backup.db")
     Session_Profile = "Devld"
     Group_Data_Array=Group_Profile_Handler.Retreive_Group_Record(Connection_Manager , UniqueID)

     Member_Data=Associate_Profile_Handler.Retreive_Group_Members(Connection_Manager_Pipe , UniqueID)


     Group_Token=Group_Profile_Handler.Retreive_Group_Token(Connection_Manager , UniqueID)
     Group_Size=Group_Profile_Handler.Retreive_Group_Size(Connection_Manager , UniqueID)
     Group_Creation=Group_Profile_Handler.Retreive_Group_Creation(Connection_Manager , UniqueID)

     Activity_Profiles=Activity_Profile_Handler.Retreive_Group_Activity(Connection_Manager , UniqueID)
     return render_template('Associate.html',Session_Profile=Session_Profile , Group_Data_Array=Group_Data_Array, Group_Token=Group_Token,Group_Size =Group_Size, Group_Creation=Group_Creation, Member_Data=Member_Data , Activity_Profiles=Activity_Profiles)







# CLASS BASED VIEW DECLARATIONS



class Master_Records_Verification(View):

    def dispatch_request(self):
        Session_Profile = "Devld"
        return render_template('Verify_Master_Record.html', Session_Profile=Session_Profile)




class Operator_Link_View_Full(View):
    def dispatch_request(self):
        Session_Profile = "Devld"
        Connection_Manager  =  Register_Upload_Link.create_connection("./static/Databases/backup.db")
        Link_Data_Tree=Register_Upload_Link.Retreive_Upload_Links(Connection_Manager)
        return render_template('Operator_Link_View_Full.html' , Link_Data_Tree = Link_Data_Tree , Session_Profile = Session_Profile )



class Verification_Trial_Master(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        Session_Profile = "Devld"
        Connection_Manager = Register_New_Master.create_connection("./static/Databases/backup.db")
        SuppliedString = ""
        if request.method == 'POST':
            Key1 =request.form.get("Capture")

            print(SuppliedString)
            ConceptProof = Register_New_Master.Confirm_Verification_Status(Connection_Manager, Key1  )
            if ConceptProof != None :
                return redirect(url_for('Login'))

        return render_template('Verify_Master_Record.html', Session_Profile=Session_Profile)



class Load_Receiver(View):
    methods = ['GET','POST']
    def dispatch_request(self):
        Session_Profile = "Devld"
        if request.method == "POST":
            Certification = request.form.get("Certification")
            Course = request.form.get("CourseProfile")
            Semester = request.form.get("Semester")
            Criteria = request.form.get("Criteria")
            Connection_Manager = Register_New_Receiver.create_connection("./static/Databases/backup.db")
            Receiver_Data =Register_New_Receiver.Query_Persona_Schema(Connection_Manager , Certification ,  Course , Semester , Criteria  )
            Message_Handles =Access_Dispatch_Stream.Retreive_Dispatch_Relative(Connection_Manager , Certification ,  Course , Semester  )
            print(Receiver_Data[0])
            return render_template('Conversation_Foward.html' , Receiver_Data=Receiver_Data , Message_Handles=Message_Handles ,  Session_Profile=Session_Profile  )
        return render_template("Single_Send_Option.html")


class Verification_Trial_Captive(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        Session_Profile = "Devld"
        Connection_Manager = Register_New_Receiver.create_connection("./static/Databases/backup.db")
        SuppliedString = ""
        if request.method == 'POST':
            Key1 =request.form.get("Capture")
            print(SuppliedString)
            ConceptProof = Register_New_Receiver.Confirm_Verification_Status(Connection_Manager, Key1  )
            if ConceptProof != None :
                return redirect(url_for('Auth'))

        return render_template('Verify_Captive_Record.html', Session_Profile=Session_Profile)




class Upload_Link_Moderator(View):
    methods = ["POST" ,"GET"]


    def dispatch_request(self):
        Connection_Manager = Register_Upload_Link.create_connection("./static/Databases/backup.db")
        Session_Profile = "Devld"
        Session_Profile = "Devld"
        Link_Data  = request.form
        LinkPeriod = str("Alien")
        LinkSpan = str("Alien")
        SessionCount = str("Alien")
        ExpectedCount = str("Alien")
        LinkStatus = str("Alien")
        LinkAdmin = str("Alien")
        LinkProfile = str("Alien")
        Upload_Link_Data  = list(Link_Data.values())



        Upload_Link_Data.append(SessionCount)
        Upload_Link_Data.append(ExpectedCount)
        Upload_Link_Data.append(LinkStatus)
        Upload_Link_Data.append(LinkAdmin)
        Upload_Link_Data.append(LinkProfile)


        Register_Upload_Link.Create_UploadLinks(Connection_Manager, Upload_Link_Data)
        Path_Located = Submission_Storage(Submission_Storage_Hook , Upload_Link_Data[0])
        print(Path_Located)
        # Starting Oerations For The Mkdir Creation Master Process
        # This Function Was Causing Our Db To breal and return err:
        # for now will just stick with a naked block of expressions
        # Our Chdir Function Prints At Root Path Try Creating A Folder By passing Its whole path 
        os.mkdir(str(Upload_Link_Data[0]))
        return redirect(url_for("Links" , UniqueID = Session_Profile ))



class FinancialAccounting(View):

    def dispatch_request(self):
        Session_Profile = "Devld"
        return render_template('BillingProfile.html', Session_Profile=Session_Profile)



class Conversation_Foward(View):

    def dispatch_request(self):
        Session_Profile = "Devld"
        Receiver_Data = []
        return render_template('Conversation_Foward.html', Session_Profile=Session_Profile , Receiver_Data=Receiver_Data)


class SurveyCenter(View):

    def dispatch_request(self):
        Session_Profile = "Devld"
        return render_template('Survey-Consolidated.html', Session_Profile=Session_Profile)



class Trigger_Survey_Template(View):

    def dispatch_request(self):
        Session_Profile = "Devld"
        return render_template('Trigger_Survey_Creation.html', Session_Profile=Session_Profile , Generate_Secure_Token = Generate_Secure_Token  )



class SurveyProcessing(View):
    methods = ["POST" ,"GET"]
    def dispatch_request(self):
        Connection_Manager = Survey_Profile_Handler.create_connection("./static/Databases/backup.db")
        Session_Profile = "Devld"
        CreationTime = "24/5/34 13:56 "
        if request.method == 'POST':
            Survey_Content = request.form
            Optimized_Content = list(Survey_Content.values())
            Optimized_Content.append(CreationTime)

            Survey_Profile_Handler.Create_Survey_Data_Profiles(Connection_Manager, Optimized_Content)
        return redirect (url_for('Dashboard' , UniqueID = "Devld "))


class Incomming_Group(View):
    methods = ["POST" ,"GET"]
    def dispatch_request(self):
        Connection_Manager = Group_Profile_Handler.create_connection("./static/Databases/backup.db")
        Session_Profile = "Devld"
        CreationTime = "24/5/34 13:56 "
        if request.method == 'POST':
            Group_Content = request.form
            Group_Data_Content = list(Group_Content.values())
            Group_Data_Content.append(CreationTime)

            Group_Profile_Handler.Create_Group_Data_Profiles(Connection_Manager, Group_Data_Content)
        return redirect (url_for('Clubs'))




class Departmental(View):

    def dispatch_request(self):
        Session_Profile = "Devld"
        return render_template('Departments.html', Session_Profile=Session_Profile)


class LinkCreator(View):

    def dispatch_request(self):
        Session_Profile = "Devld"
        return render_template('Upload_Link_Creator.html', Session_Profile=Session_Profile , Generate_Secure_Token = Generate_Secure_Token )


class InfoTrack(View):

    def dispatch_request(self):
        Session_Profile = "Devld"
        return render_template('InformationTracking.html', Session_Profile=Session_Profile)



class LinkGenerator(View):

    def dispatch_request(self):
        Session_Profile = "Merlin"
        UniqueID = Session_Profile
        Connection_Manager = Register_Upload_Link.create_connection("./static/Databases/backup.db")
        Certification= Register_New_Receiver.Retreive_Certification_Field(Connection_Manager , UniqueID)
        Course= Register_New_Receiver.Retreive_Course_Field(Connection_Manager , UniqueID)
        Semester= Register_New_Receiver.Retreive_Semester_Field(Connection_Manager, UniqueID)
        Cert=str(Certification).strip("[](),''")
        Crs=str(Course).strip("[](),''")
        Sem=str(Semester).strip("[](),''")

        Link_Data_Schema=Register_Upload_Link.Retreive_Link_Quota(Connection_Manager, "all" , "all" , 3)
        # for Entry  in Conversation_Data:
            # print(Entry)
        # print(" List Ended Here")
        Link_Limit = int(len(Link_Data_Schema))
        return render_template('Operator_Link_View.html', Session_Profile=Session_Profile , Link_Data_Schema = Link_Data_Schema , Link_Limit = Link_Limit )




class SinkStore(View):
    def dispatch_request(self):
        Session_Profile = "merlin"
        Connection_Manager = Access_Dispatch_Stream.create_connection("./static/Databases/backup.db")
        Connection_Manager_V4 = Request_Profile_Handler.create_connection("./static/Databases/backup.db")
        MessageData=Access_Dispatch_Stream.Retreive_Parent_Dispatch(Connection_Manager, Session_Profile)
        MessageLimit = len(MessageData)
        RequestData=Request_Profile_Handler.Retreive_Request_Data_Profiles(Connection_Manager_V4)


        return render_template('WaveLogs.html', Session_Profile=Session_Profile , MessageData=MessageData , RequestData=RequestData  , MessageLimit = MessageLimit)


class Operator_Upload_Hook(View):
    methods = ["POST" ,"GET"]
    def dispatch_request(self):
        Session_Profile = "Merlin"
        Positional_Cache = "Pool-Resources"
        if request.method == 'POST':
            Content = request.form
            FileID = Generate_Secure_Token()
            file = request.files['UploadContent']
            if file:
                file.save(os.path.join(app.config['Operator_Storage_Path'] , Session_Profile , Positional_Cache , file.filename ))
        return redirect(url_for('Explorer' , UniqueID = Session_Profile))




class Upload_Link_Hook(View):
    methods = ["POST" ,"GET"]
    def dispatch_request(self):
        Session_Profile = "Merlin"
        Link_Storage_Path = ""
        Positional_Cache = ""
        if request.method == 'POST':
            Content = request.form
            LinkID = request.form.get('LinkID')
            Positional_Cache = LinkID
            file = request.files['UploadContent']
            if file:
                file.save(os.path.join(app.config['Submission_Storage_Path'] ,  Positional_Cache , file.filename ))
        return redirect(url_for('ViewLinks' ))


class Operator_Club_Listings_Full(View):

    def dispatch_request(self):
        Connection_Manager = Group_Profile_Handler.create_connection("./static/Databases/backup.db")
        Group_Data_Schema = Group_Profile_Handler.Retreive_Group_Data_Profiles(Connection_Manager)
        Session_Profile = "Devld"
        Group_Limit = int(len(Group_Data_Schema))
        return render_template("ClubListings.html" , Group_Data_Schema = Group_Data_Schema , Group_Limit = Group_Limit  , Session_Profile = Session_Profile)




class Group_Profile_Creator(View):

    def dispatch_request(self):

        Session_Profile = "Devld"
        return render_template("Trigger_Group_Creation.html")



class AllUserProfiles(View):

    def dispatch_request(self):
        Session_Profile = "Devld"
        return render_template('User_Center.html')


class Conversations(View):

    def dispatch_request(self):
        Session_Profile = "Devld"
        return render_template('Talkpage.html')



class PowerBank(View):

    def dispatch_request(self):
        Session_Profile = "Devld"
        return render_template('PowerInformation.html')


class Captive_Activity_Listings(View):

    def dispatch_request(self):
        Session_Profile = "Devld"
        Connection_Manager= Activity_Profile_Handler.create_connection("./static/Databases/backup.db")
        Activity_Session_Profiles = Activity_Profile_Handler.Retreive_Activity_Data_Profiles(Connection_Manager)
        #Associate_Profile_Handler.Retreive_Group_Data_Profiles(Connection_Manager)
        #print(Shelve)
        #Activity_Records = []
        #Activity_Session_Profiles = []
        #for Elem in Shelve:
            #Activity_Records.append(str(Elem).strip("()[]','"))
        #for Entry in Activity_Records:
            #Sub=Activity_Profile_Handler.Retreive_Activity_By_Gid(Connection_Manager, Entry)
            #Version = str(Sub).strip("()[]','")
            #Activity_Session_Profiles.append(Version)
            #print("Track 1" , Activity_Session_Profiles)
        Activity_Limit = int(len(Activity_Session_Profiles))
        return render_template('Captive_Activity_Listings.html' , Activity_Session_Profiles = Activity_Session_Profiles , Activity_Limit = Activity_Limit)


class Captive_Communication_Listings(View):

    def dispatch_request(self):
        Session_Profile = "Devld"
        Connection_Manager = Access_Dispatch_Stream.create_connection("./static/Databases/backup.db")
        Certification= Register_New_Receiver.Retreive_Certification_Field(Connection_Manager , Session_Profile)
        Course= Register_New_Receiver.Retreive_Course_Field(Connection_Manager , Session_Profile)
        Semester= Register_New_Receiver.Retreive_Semester_Field(Connection_Manager , Session_Profile)
        Cert=str(Certification).strip("[](),''")
        Crs=str(Course).strip("[](),''")
        Sem=str(Semester).strip("[](),''")

        Communication_Event= Access_Dispatch_Stream.Retreive_Dispatch_Relative(Connection_Manager , Cert , Crs , 3)
        # for Entry  in Conversation_Data:
            # print(Entry)
        # print(" List Ended Here")
        Communication_Limit = int(len(Communication_Event))

        return render_template('Captive_Communication_Listings.html' , Communication_Event=Communication_Event , Communication_Limit = Communication_Limit , Session_Profile = Session_Profile )

class Captive_Explorer_Pallette(View):

    def dispatch_request(self):
        Session_Profile = "merlin"
        UniqueID = Session_Profile
        Personal_Link_URL = DestinationUser(Receiver_Storage_Handle ,UniqueID)
        Public_Link_URL = Public_Storage(Public_Storage_Handle)
        Private_Link_URL = Private_Storage(Receiver_Storage_Handle , UniqueID )
        Personal_File_Storage = os.listdir(Personal_Link_URL)
        Public_File_Storage = os.listdir(Public_Link_URL)
        Private_File_Storage = os.listdir(Private_Link_URL)
        #print(Data_Layer)
        #for x in Data_Links:
            #print(x)
        Personal_Storage_Length = int(len( Personal_Link_URL))
        Public_Storage_Length = int(len(Public_Link_URL))


        return render_template('Captive_Explorer_Pallette.html' , Personal_File_Storage = Personal_File_Storage , Public_File_Storage = Public_File_Storage , Private_File_Storage = Private_File_Storage , Personal_Storage_Length = Personal_Storage_Length , Public_Storage_Length= Public_Storage_Length , Session_Profile = Session_Profile)



class Captive_Private_Group_Listings(View):
    def dispatch_request(self):
        Session_Profile = "Devld"
        Connection_Manager = Associate_Profile_Handler.create_connection("./static/Databases/backup.db")
        Connection_Manager_Group = Group_Profile_Handler.create_connection("./static/Databases/backup.db")
        Shelve = Associate_Profile_Handler.Retreive_Group_Listings(Connection_Manager , Session_Profile )
        Group_Records = []
        Group_Data_Schema = []
        for Elem in Shelve:
            Group_Records.append(str(Elem).strip("()','"))
        for Schema in Group_Records:
            Sub =Group_Profile_Handler.Retreive_Group_Record(Connection_Manager_Group , Schema)
            Version = str(Sub).strip("[]()''")
            Group_Data_Schema.append(Version)
        print("This Is Elem 1 " , (Group_Data_Schema[0]))
        print("This Is Elem -1 " , Group_Data_Schema[-1])
        Group_Tally = len(Group_Data_Schema)
        return render_template('GroupProfiles.html' , Group_Data_Schema=Group_Data_Schema , Group_Tally=Group_Tally , Session_Profile =Session_Profile )

class Captive_Public_Group_Listings(View):
    def dispatch_request(self):
        Session_Profile = "Devld"
        Connection_Manager = Associate_Profile_Handler.create_connection("./static/Databases/backup.db")
        Connection_Manager_Group = Group_Profile_Handler.create_connection("./static/Databases/backup.db")
        Group_Data_Schema = Group_Profile_Handler.Retreive_Group_Data_Profiles(Connection_Manager)
        Group_Tally = len(Group_Data_Schema)
        return render_template('GroupProfiles.html' , Group_Data_Schema=Group_Data_Schema , Group_Tally=Group_Tally , Session_Profile =Session_Profile )




class PowerHouse(View):
    def dispatch_request(self):
        Session_Profile = "Devld"
        return render_template('PowerProfiles.html')
# Take Emphasis On point Relation

class ReceiverAccount(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        Connection_Manager = Register_New_Receiver.create_connection("./static/Databases/backup.db")
        Verification_Code = "4545"
        if request.method == 'POST':
            HalfIntro = request.form
            CredentialObject = list(HalfIntro.values())
            for x in CredentialObject:
                print(x)
            CredentialObject.append(Verification_Code)
            Register_New_Receiver.Create_UserProfile(Connection_Manager , CredentialObject)
            FormatTrigger = f'<Response><Say> {Verification_Code} </Say> </Response>'
            Twilio_Service.Broadcast_Voice_Notification(FormatTrigger , "+254792619021")

            return redirect(url_for('Security'))
        else:
            Session_Profile = "Devld"
            return render_template('Public_Sign_Up.html')


class Captive_View_Frame(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        Connection_Manager = Register_New_Receiver.create_connection("./static/Databases/backup.db")
        Context_Keys = ('Username' , 'Password')
        Context_Value = "Unknown"
        if request.method == 'POST':
                # - Action Zone
                UserDict = {}
                UserDict = request.form
                for k in UserDict.values():
                    print(k)
                # Database Profiling
                UserID = request.form.get("UserString")

                CryptoIdentifier = request.form.get("CryptoString")
                Security_Captcha = Register_New_Receiver.Query_User_Existence(Connection_Manager, UserID)
                Crypto_Captcha = Register_New_Receiver.Query_CryptoHash_Existence(Connection_Manager, CryptoIdentifier)
                print(Security_Captcha)
                if (Security_Captcha != None ):
                    if(Crypto_Captcha != None):
                        return redirect(url_for('TKNP' , UniqueID = UserID))
                    else:
                        return redirect(url_for('Auth'))
                else:
                    users = " jsdjsd "
                    return  redirect(url_for('Auth'))
        else:
                return render_template('Receiver_View_Controller.html' )



class Master_View_Frame(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        Connection_Manager = Register_New_Master.create_connection("./static/Databases/backup.db")
        Context_Keys = ('Username' , 'Password')
        Context_Value = "Unknown"
        if request.method == 'POST':
                # - Action Zone
                UserDict = {}
                UserDict = request.form
                for k in UserDict.values():
                    print(k)
                # Database Profiling
                UserID = request.form.get("UserString")

                CryptoIdentifier = request.form.get("CryptoString")
                Security_Captcha = Register_New_Master.Query_User_Existence(Connection_Manager, UserID)
                Crypto_Captcha = Register_New_Master.Query_CryptoHash_Existence(Connection_Manager, CryptoIdentifier)
                print(Security_Captcha)
                if (Security_Captcha != None ):
                    if(Crypto_Captcha != None):
                        return redirect(url_for('Dashboard' , UniqueID = UserID))
                    else:
                        return redirect(url_for('Login'))
                else:
                    users = " jsdjsd "
                    return  redirect(url_for('Login'))
        else:
                return render_template('Master_View_Controller.html' )




class MasterAccount(View):
   methods = ['GET', 'POST']
   def dispatch_request(self):
    Connection_Manager = Register_New_Master.create_connection("./static/Databases/backup.db")
    Verification_Code  = "4567"
    if request.method == 'POST':
        Upstream_Feed = request.form
        User =str(request.form.get("Fullname"))
        CredentialObject = list(Upstream_Feed.values())
        CredentialObject.append(Verification_Code)
        Register_New_Master.Create_UserProfile(Connection_Manager , CredentialObject)
        FormatTrigger = f"Welcome To Wave {User} , Your Verification Code is {Verification_Code} \n Thanks And Have A Great Day "
        Twilio_Service.Broadcast_Sms_Notification(FormatTrigger , "+254792619021")

        return redirect(url_for('Verify') )
    else:
        return render_template('Private_Sign_Up.html')





class DispatchEvents(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        Connection_Manager = Access_Dispatch_Stream.create_connection("./static/Databases/backup.db")
        Session_Profile = "Devld"
        if request.method == 'POST':
            DispatchData = request.form
            for d in DispatchData.values():
                print(d)
            # Filters For The Database Entry
            # Independent Uploads To The Database Forced US To Have 2 Upload Chunks
            #A More Efficient Function Will Be Used In The Future
            Data_Frame = request.form
            Resolved_Data = list( Data_Frame.values() )
            Access_Dispatch_Stream.Record_Dispatch_Events(Connection_Manager , Resolved_Data)
            return redirect(url_for("Dashboard" , UniqueID=Session_Profile))
        else:
            Session_Profile = "Devld"
        return render_template('Custom_Send_Options.html', Generate_Secure_Token=Generate_Secure_Token , Session_Profile=Session_Profile )













app.add_url_rule('/Verify/', view_func=Master_Records_Verification.as_view('Verify'))
app.add_url_rule('/SecurityCheck/', view_func=Verification_Trial_Master.as_view('SecurityCheck'))
app.add_url_rule('/Security/', view_func=Verification_Trial_Captive.as_view('Security'))
app.add_url_rule('/Auth/', view_func=Captive_View_Frame.as_view('Auth'))
app.add_url_rule('/Login/', view_func=Master_View_Frame.as_view('Login'))
app.add_url_rule('/CreateAccount/', view_func=MasterAccount.as_view('CreateAccount'))
app.add_url_rule('/Dispatch/', view_func=DispatchEvents.as_view('Dispatch'))
app.add_url_rule('/Links/All/', view_func=Operator_Link_View_Full.as_view('AllLinks'))
app.add_url_rule('/OperatorUpload/', view_func=Operator_Upload_Hook.as_view('OpUpload'))
app.add_url_rule('/Submit/', view_func=Upload_Link_Hook.as_view('Submit'))

app.add_url_rule('/ActivityListings/', view_func=Captive_Activity_Listings.as_view('ActivityListings'))
app.add_url_rule('/Communications/', view_func=Captive_Communication_Listings.as_view('Communications'))
app.add_url_rule('/Captive/Explorer/', view_func=Captive_Explorer_Pallette.as_view('CaptiveExplorer'))
app.add_url_rule('/AllGroups/', view_func=Operator_Club_Listings_Full.as_view('AllGroups'))
app.add_url_rule('/ExecuteSurvey/', view_func=SurveyProcessing.as_view('ExecuteSurvey'))
app.add_url_rule('/CreateSurvey/', view_func=Trigger_Survey_Template.as_view('CreateSurvey'))
app.add_url_rule('/CreateSink/', view_func=ReceiverAccount.as_view('CreateSink'))
#Returning Explorer Container
app.add_url_rule('/LoadProfiles/', view_func=Load_Receiver.as_view('LoadProfiles'))
app.add_url_rule('/Departments/', view_func=Departmental.as_view('Departments'))
app.add_url_rule('/AllSinks/', view_func=SinkStore.as_view('AllSinks'))
app.add_url_rule('/Billing/', view_func=FinancialAccounting.as_view('Billing'))
app.add_url_rule('/UserProfiles/', view_func=AllUserProfiles.as_view('UserProfiles'))
app.add_url_rule('/PowerProfiles/', view_func=PowerHouse.as_view('PowerProfiles'))
app.add_url_rule('/Profile/', view_func=PowerBank.as_view('Profile'))
app.add_url_rule('/GroupCreation/', view_func=Incomming_Group.as_view('GroupCreation'))

app.add_url_rule('/Converse/', view_func=Conversations.as_view('Converse'))
app.add_url_rule('/Survey/', view_func=SurveyCenter.as_view('Survey'))
app.add_url_rule('/ViewLinks/', view_func=LinkGenerator.as_view('ViewLinks'))
app.add_url_rule('/Tracking/', view_func=InfoTrack.as_view('Tracking'))
app.add_url_rule('/CreateLink/', view_func=LinkCreator.as_view('CreateLink'))

app.add_url_rule('/Groups/Available/', view_func=Captive_Public_Group_Listings.as_view('PublicGroupings'))
app.add_url_rule('/Conversation/', view_func=Conversation_Foward.as_view('Conversation'))
app.add_url_rule('/CreateGroup/', view_func=Group_Profile_Creator.as_view('CreateGroup'))
# Manage Uploaded Files Here
# Manage Uploaded Files Here
app.add_url_rule('/CreateUpload/', view_func=Upload_Link_Moderator.as_view('CreateUpload'))



# Main Execution Block
# Rendering With Openssl : ADHOC
# Running This Script Requires The Following
         # Openssl Binary Value Should Be Set To Zero
         # Xml Parser :: Expat Should be of version > 2 Not Lower
         # For Systems With Low Expat Versions :
               #Serialization Is therefore defaulted to Json

if __name__=='__main__':

   # Database Creation Section
  # DB_InitializationWizard("/static/Databases/RentLord_Databases.db")

   app.run("0.0.0.0" , debug="False" )
