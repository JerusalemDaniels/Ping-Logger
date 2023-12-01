#Ping Logger v2
#by Mark Bolaños

#Logs ALL failed pings


import os
import time
import datetime


# Containing the While loop in a function seems to work well
def pingLogger(hostname):
    #Endless loop that pings the hostname every 3 seconds

    while True:
        response = os.system("ping -n 1 " + str(hostname)) 
        if(response != 0):                                                                                # If the response is not 0, there was an issue pinging
            file1 = open(str(hostname) + " ping log.txt", "a")                                            # Opens the file to allow appending
            file1.write("\nFailed at pinging " + str(hostname) + " " + str(datetime.datetime.now()))      # Writes to the file
            file1.close()                                                                                 # Closes the file to free up resources
        
        time.sleep(3)    
    
#Checks if a file has already been created for a specific hostname
def checkFile(hostname):
    file_path = str(hostname) + " ping log.txt"                                                           #Stores the file path to check

    if os.path.exists(file_path):                                                                         #Checks if the file exists
        pingLogger(hostname)
    else:
        createFile(hostname)

#Creates the new file
def createFile(hostname):
     file1 = open(str(hostname) + " ping log.txt", "x")                                                   #Creates the new log
     file1.close()
     pingLogger(hostname)

#Start method that asks for a hostname to ping
def start():
    print("Enter Hostname: ")
    h = input()
    checkFile(h)
    
    

start()
    