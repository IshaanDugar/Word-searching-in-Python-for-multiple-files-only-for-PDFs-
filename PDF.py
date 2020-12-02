import os			#OS module connects your system to python
import PyPDF2		#PyPDF2 is a library for PDF reading and editing

path = input('Directory: ') # ENTER THE PATH TO THE LOCATION LIKE 'C:/USER/path-to-folder'

os.chdir(path)	#changes the directory to the path entered

search = input('WORD OR PHRASE YOU ARE SEARCHING: ')	#The string you are searching for

for r,d,f in os.walk(top='.'):							#Iterates through all the files, folders and directories in the path specified
	for name in f:
		if name.endswith('.pdf'):						#Since this only works for PDF files, we want to check only PDF files to prevent errors
			file = open(name, 'rb')
			reader = PyPDF2.PdfFileReader(file)
			pgs = reader.numPages

			for i in range(pgs):
				pg = reader.getPage(i)
				text_pg = pg.extractText()
				if search in text_pg:
					print(f'PDF {name}: Page {i + 1}')