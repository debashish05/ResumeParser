""""
The way PDF Miner reads in PDF is line by line. Thus, the text from the left and right
sections will be combined together if they are found to be on the same line. 
Therefore, as you could imagine, it will be harder for you to extract information in the 
subsequent steps. On the other hand, pdftree will omit all the "new line" characters, 
so the text extracted will be something like a chunk of text. 
Thus, it is difficult to separate them into multiple sections.
But since Apache TikaTM REST, will be an external dependecny and will depend on the 
availablity of server. I have decided to use PDFMiner.six.
"""

from pdfminer.high_level import extract_text
import re

Parser = ""
skills = {}
college_name = {}
disciplanes	= {}
degree = {}
designation = {}
company_names = {} 
email=""
mobile_number = ""
attribute={}

def loadDataSet(dict,filePath):
	""" 
		Load dataset in the file, If you want to add new skills just enter the parameter 
		in Dataset/file_Name
	"""
	fin = open(filePath, "r")
	inputFile = fin.readlines()
	
	for lines in inputFile:
		lines=lines[0:len(lines)-1].lower() #remove new line which is extra added in dataset
		if lines not in dict:
			dict[lines]=True
	
	fin.close()


def extractEmail(Parser):
	"""
		Extract email from Text of type str
	"""
	emailMatch = re.findall(r"([^@|\s]+@[^@]+\.[^@|\s|\n]+)", Parser)
	# any no character except @ or space then @ then no @ then  .  then no @ and space
	# + means than any no. of character.

	if emailMatch:
		try:
			email=emailMatch[0].split()[0].strip(';')
		except IndexError:
			email=""
	
	return email


def extractKeyWords(Parser):

	attribute.clear()
	attribute["skills"]=set()
	attribute["college_name"]=set()
	attribute["disciplanes"]=set()
	attribute["degree"]=set()
	attribute["designation"]=set()

	for i in range(0,len(Parser)):
		word=""
		for j in range(i,min(len(Parser),i+50)):
			word+=Parser[j]
			if word in skills:
				attribute["skills"].add(word)
			if len(attribute["college_name"])<1 and word in college_name:
				# to avoid internship and other trainings / certifications from iit
				# to add in the college name section. Usually first name of college
				# is the most recent college name
				attribute["college_name"].add(word)
			if word in disciplanes:
				attribute["disciplanes"].add(word)
			if word in degree:
				attribute["degree"].add(word)
			if word in designation:
				attribute["designation"].add(word)


def loadData(filePath):
	"""
			Load all the dataset for parsing
	"""
	loadDataSet(skills,"Dataset/new_skills.txt")
	loadDataSet(college_name,"Dataset/college.txt")
	loadDataSet(disciplanes,"Dataset/disciplanes.txt")
	loadDataSet(degree,"Dataset/degree.txt")
	loadDataSet(designation,"Dataset/designation.txt")
	#loadDataSet(company_names,"Dataset/company.txt") #giving very wrong output
	Parser = extract_text(filePath).lower()
	mobile_number = re.findall(r"\b[789]\d{9}\b", Parser)
	email = extractEmail(Parser)
	return Parser,mobile_number,email


if __name__ == '__main__':
	"""
		Take resume filepath as input and parse it and print attributes of resume
		like  skills, college, disciplanes, degree, designation
	"""
	filePath='Sample_Resume/Debashish_Resume.pdf'
	Parser,mobile_number,email=loadData(filePath)
	extractKeyWords(Parser)
	attribute["mobile_number"]=mobile_number
	attribute["email"]=email
	#attribute["Resume"]=Parser

	for key,values in attribute.items():
		print(key," : ",values)
