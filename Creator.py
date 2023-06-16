import os


File_Modes = [ "r+" , "w+" , "a+" , "r" , "w" , "a" ]

# Path Declarations



# Liquid Configurations


def Create_Dir_Object(Filepath , Dirname ):
	# Checking File Path
	PathHandle = os.path.normpath(Filepath)
	HandleName = os.chdir(PathHandle)
	os.mkdir(str(Dirname))
	return "Dirname + Created Successfully "


def Create_File_Object(Filepath , Filename , Data ):
	# Checking File Path
	PathHandle = os.path.normpath(Filepath)
	HandleName = os.path.join (PathHandle , Filename )
	ModeHandle = File_Modes[1]

	with open(HandleName , ModeHandle) as Stream_Creator:
		Stream_Creator.writelines(Data)
		Stream_Creator.writelines("\n")





def Append_File_Object( Filepath ,Filename , Data ):
	# Checking File Path
	PathHandle = os.path.normpath(Filepath)
	HandleName = os.path.join (PathHandle , Filename )
	ModeHandle = File_Modes[2]

	with open(HandleName , ModeHandle) as Stream_Creator:
		Stream_Creator.writelines(Data)
		Stream_Creator.writelines("\n")



#Create_File_Object(r"C:\Users\Deathlock\Desktop\Wave-main\static\Data\Upload_Links" , "Rihanna.txt" ,  "Whats My Name , Teamo Exclussive , Diamonds ")


#Append_File_Object("." , "Rihanna.txt" ,  "Runs The World  , Nobody talks  , Shine Bright Diamonds ")
