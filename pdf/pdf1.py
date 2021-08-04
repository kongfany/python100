"""
----------------------------------------
    File Name: pdf1
    Author: Kong
    Date: 2021/7/31
    Description: 
----------------------------------------
"""
import PyPDF2

reader = PyPDF2.PdfFileReader('test.pdf')
page = reader.getPage(0)
print(page.extractText())