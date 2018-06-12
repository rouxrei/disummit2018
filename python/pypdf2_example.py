# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 13:12:18 2018

@author: rouxrei
"""
import PyPDF2

# creating an object 
file = open(r'.\data\input_pdf\Tanzania_SummarySheet_English.pdf', 'rb')

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)

# print the number of pages in pdf file
print(fileReader.numPages)

# print text on all the pages
for page in fileReader.pages:
    print(page.extractText())

# close the file-stream
file.close()
