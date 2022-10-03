#!/usr/bin/env python
# coding: utf-8



import os  # need access to path functions

#   ask user for storage directory and verifies directory exists
#      input desired storage directory
#      check to see if it exists (create directory if it doesn't exist? -- not for now)
print("Where do you want to store the file? ")
storageDirectory = input()
print(os.path.exists(storageDirectory))  # debugging code
if not os.path.exists(storageDirectory):
    # quit if directory doesn't exist
    exit()

#   asks for name, address, phone number
#      input name     (and store)
#      input address
#      input phone number
name = input("What is your name?  ")
address = input("Where do you live?  ")
phone = input("What is your phone number?  ")
# print(name, address, phone)   # debugging code

#   writes single comma separated value (csv) line to file
#      open a file for writing
#        create string variable to hold filename
#        open filename
#      write the line containing name, address, phone number (using commas to separate values)
#      close the file

fileName = name.replace(" ","_") + ".csv"               # create a filename based on the entered name
# print(fileName)  #debugging code
# print(storageDirectory+"\\"+fileName)  #debugging code (use "\\" to escape the \ character)
fileHandle = open(storageDirectory+"/"+fileName,"w")    # open file for writing, "w" == open for writing / overwriting
                                                        # python natively changes the path separators to correct version
                                                        # for host OS
fileHandle.write(name+","+address+","+phone)            # write the line with explicit commas using "+" for concatenation
fileHandle.close()                                      # close the file

#   reads file
#      open the newly created file for reading  (this implies that we need to create variable with the filename)
#      read the line into a variable (list or a single string)
#      close the file
#   displays line
#      print data

fileHandle = open(storageDirectory+"/"+fileName,"r")    # open file for reading, "r" == open for reading only
print(fileHandle.read())                                # combined reading and writing steps by passing the
                                                        # output from the read function to a print function
fileHandle.close()
