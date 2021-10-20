#!/usr/bin/env python
# coding: utf-8

# In[13]:


#user_input = input(("Input file path: (ex. \"C:\\Users\\insertusernamehere\\Downloads\\test.csv)\"\n"))#to copy file path, hold shift and then right click file. open(file path, mode, buffering). 
#Cannot use string as file path, either put 'r' before file path, "\\" to read every escape character, or replace every "\" with "/"
    

def read_file():   
   # user_input = input(("Input file path: (ex. \"C:\\\\Users\\\\usernamehere\\\\Location\\\\test.csv)\"\n"))#this function takes in user_input as an argument (file path)
    fileHandle = open(input(("Input file path: (ex. \"C:\\\\Users\\\\usernamehere\\\\Location\\\\test.csv)\"\n")),"r")         
    file_data = []              #empty list to be written to
    for line in fileHandle:             
        file_data.append(line) #writing data of csv to empty list
    if __name__ == "__main__":   
        print(file_data)
    
    fileHandle.close() 
    return file_data   

if __name__ == "__main__":
    read_file()

 #call to read_file passing user_input as argument
#pathfinder() #call to pathfinder function
                         


# In[ ]:





# In[ ]:





# In[ ]:




