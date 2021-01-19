import PyPDF2  
import requests 

link = "hard_copy.pdf"

pdfFileObj = open(link, 'rb')   
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  
pageObj = pdfReader.getPage(0)  
print(pageObj.extractText())  
pdfFileObj.close()  