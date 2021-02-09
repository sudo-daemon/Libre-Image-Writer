# Importing required modules
from tkinter import *
from tkinter import filedialog
import os

# Defining a variable used later
success_token = False

# Finding the required ISO file
def find_iso():
    global isoFile, iso_location
    isoFile = filedialog.askopenfilename(
        initialdir='./', title='Find the ISO file',
        filetypes=(("Image files", "*.iso"), ("All files", "*.*"))
    )
    iso_location = str(isoFile)


# Finds the required drive to burn to
def find_drive():
    global drive_location, drive_rough_location, \
        drive_instructions_for_rough_location, verify_token, finderDrive
    drive_instructions_for_rough_location = Label(text="Enter the drive location, "
                                                       "[should be in the format '/dev/sdx']: ")
    drive_instructions_for_rough_location.pack()
    drive_rough_location = Entry(root)
    drive_rough_location.pack()
    finderDrive = Button(root, text="Submit", command=lambda: collect_drive_input())
    finderDrive.pack()

# Ensuring that the drive path matches the '/dev/' format, to make sure the output location is a drive, not another directory
def setting_drive_path():
    global drive_location, verify_token
    if verify_drive == True:
        drive_location = str(one_drive)
        verify_token = True
        dd()
    else:
        verify_token = False
        error_message = Label(root, text="Sorry. You didn't enter a valid drive path. Try again. ")
        error_message.pack()
    
    
# Setting the text input to a variable
def collect_drive_input():
    global verify_drive, one_drive
    one_drive = drive_rough_location.get()
    verify_drive = one_drive.startswith("/dev/")
    setting_drive_path()
    

# Runs the 'dd' command with the correct input and output locations
def warning():
    warning_message = Label(root, text="Warning! You cannot cancel the operation or remove the drive.")
    warning_message.pack()
    finderISO.destroy()
    drive_rough_location.destroy()
    drive_instructions_for_rough_location.destroy()
    finderDrive.destroy()
    wait_message_during_dd = Label(root, text="Burning ISO. Please wait...")
    wait_message_during_dd.pack()
    # print("Hello world")

# Executing the dd command with the correct parameters
def dd():
    warning()
    os.system('dd if=' + str(iso_location) + " of=" + str(drive_location) + ">> ./.success_verification.txt ")
    # print('dd if=' + str(iso_location) + " of=" + str(drive_location))
    #os.system('echo Good luck! >> ./.success_verification.txt')
    success_message_file = open('./.success_verification.txt', 'r')
    success_message = success_message_file.read()
    # The ultimate goal is to show this success message on the GUI by creating another 'Label' element containing the output of the dd command
    print(success_message)

# Creating actual window
root = Tk()
root.geometry("600x400")
root.geometry("+450+200")

# Title
root.title("USB Image Burner")

# Creating a dropdown file browser to locate the ISO file
finderISO = Button(root, text="Find the ISO file", command=lambda: find_iso())
finderISO.pack()

# Calling the function to import and act on the user input in the 'Drive Location" text input field
find_drive()

# Keeping window running constantly
root.mainloop()
