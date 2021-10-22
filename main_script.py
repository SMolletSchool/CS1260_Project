#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv_reading_ahhad
import classify_gau

file_data = csv_reading_ahhad.read_file()

print(file_data)

flower_no = 0
sepal_length = 0.0
sepal_width = 0.0
petal_length = 0.0
petal_width = 0.0
char_buffer = '' #define a character buffer to wring out the commas
section = 0 #section variable to choose section
flower_type = ''

for line in file_data: #for each line of data
    if line != "flower no.,sepal length (cm),sepal width (cm),petal length (cm),petal width (cm)": #skip the header
        for character in line: #for each letter in the string
            if character != ',': #if it's a number...
                char_buffer += character #add it to the buffer
            else: #if it's not a number, then it's a comma or newline, add it to a section, that section being...
                if section == 0: #flower number
                    flower_no = int(char_buffer)
                    section += 1 #increment the section
                if section == 1: #sepal length
                    sepal_length = float(char_buffer) #hilarious that this variable is never needed according to the documentation
                    section += 1 #increment the section
                if section == 2: #sepal width
                    sepal_width = float(char_buffer)
                    section += 1 #increment the section
                if section == 3: #petal length
                    petal_length = float(char_buffer)
                    section += 1 #increment the section
                if section == 4: #petal width (also the last parameter)
                    petal_width = float(char_buffer)
                    flower_type = classify_gau.classify(sepal_width,petal_length,petal_width)
                    print("Flower number {} is a {} flower".format(flower_no, flower_type)) #print the flower type to the console
                    char_buffer = '' #empty the buffer
                    section = 0 #reset the section