""""
The way PDF Miner reads in PDF is line by line. Thus, the text from the left and right sections will 
be combined together if they are found to be on the same line. Therefore, as you could imagine, 
it will be harder for you to extract information in the subsequent steps.
On the other hand, pdftree will omit all the ‘\n’ characters, so the text extracted will be something 
like a chunk of text. Thus, it is difficult to separate them into multiple sections.
"""



#Tika-Python is Python binding to the Apache TikaTM REST 
#services allowing tika to be called natively in python language.

# Tika is written in Java, so you need a java(7 or 7+) runtime installed
						
"""
# import parser object from tike
from tika import parser

# opening pdf file
parsed_pdf = parser.from_file("Project-Manager-Resume-Template-converted.pdf")

#paresed_pdf is a dict having key metadata content status

# saving content of pdf
# you can also bring text only, by parsed_pdf['text']
# parsed_pdf['content'] returns string
data = parsed_pdf['content']



# Printing of content
print(data)
#print(parsed_pdf['status'],type(parsed_pdf['status'] )) # server, 200 for success 
# <class 'str'>
#print(type(data))


"""



#pdf2txt.py Debashish_Resume.pdf 

"""
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

import pdfminer
from pdfminer.high_level import extract_text
#print(pdfminer.__version__)  
with open('Debashish_Resume.pdf','rb') as f:
    text = extract_text(f)
#text=convert_pdf_to_txt('Debashish_Resume.pdf')
print(repr(text))
#https://github.com/OmkarPathak/pyresparser

"""
"""
from pyresparser import ResumeParser
data = ResumeParser("Debashish_Resume.pdf").get_extracted_data()
print(data)
print(type(data))

for key,value in data.items():
	print(key)

"""

"""
from pdfminer.high_level import extract_text
text = extract_text('Debashish_Resume.pdf')
#print(repr(text))
print(text)
"""
# source project/bin/activate
import re
fin = open("Dataset/skills.txt", "r")
inputFile = fin.read()
#a="H 	T  G R"
outputFile = re.split(' \t|  ',inputFile)
fout=open("new_skills.txt","w")
for word in outputFile:
	word+='\n'
	fout.write(word)