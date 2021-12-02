"""
	Script to preprocess skills based on requirement
"""


import re

def ConveretEntryToNewLine():
	"""
		Place each new words which are related in new line
	"""
	fin = open("Dataset/skills.txt", "r")
	inputFile = fin.read()
	#a="H 	T  G R"
	outputFile = re.split(' \t|  ',inputFile)
	fout=open("new_skills.txt","w")
	for word in outputFile:
		word+='\n'
		fout.write(word)


def removeDupplicate(fileName):
	"""
		Remove dupplicate lines
	"""
	fin = open(fileName, "r")
	inputFile = fin.readlines()
	fout=open("Dataset/company.txt","w")
	dict={}

	for lines in inputFile:
		lines=lines.lower()
		if lines not in dict:
			dict[lines]=True
	
	for keys in dict:
		fout.write(keys)

	fin.close()
	fout.close()
	

if __name__ == '__main__':
	#removeDupplicate("Dataset/companies.txt")

