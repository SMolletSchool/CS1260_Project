#!/usr/bin/env python
# coding: utf-8

# In[6]:

#REPLACE
fileHandle = open("C:\\Users\\ayesh\\Downloads\\test.csv","r")#to copy file path, hold shift and then right click file. open(file path, mode, buffering). 
#Cannot use string as file path, either put 'r' before file path, "\\" to read every escape character, or replace every "\" with "/"
for line in fileHandle:
    print(line)
fileHandle.close()#always close after opening
#WITH
#def read_file(user_input):
#    file = open(user_input)
#    file_contents = []
#    for line in file:
#        file_contents.append(line)
#    return file_contents


# In[ ]:




