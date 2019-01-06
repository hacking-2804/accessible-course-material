import re

def findBetween(s, first, last ):
	start_index = s.find(first)
	end_index = start_index + len(first)
	last_index = s.find(last)

	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
		return ""

def findBetweenIndex(s, first, lastI ):

	try:
		start = s.index(first) + len(first)
		return s[start:lastI]
	except ValueError:
		return ""

#[Chapter][Section][Subsection]
def BreakIntoChunks(file,num):
    ChapterFile = open(file,"r")
    ChapterString = ChapterFile.read()
    Section = 1
    Subsection = 1

    #pull intro


    #pull 
    while "\section" in ChapterString:
        if ChapterString.count("\section") > 1:
            #print("Section "+str(Section))
            Section+=1
            SectionString = findBetween(ChapterString,"\section","\section")  
             
            print("SECTIONSTRING:")
            #print(SectionString)
            '''
            while "\subsection" in SectionString:
               
                if SectionString.count("\subsection") > 1:
                    print("Section "str(Section))
                    print("Subsection "+str(Subsection))
                    Subsection += 1
                    SubsectionString = findBetween(ChapterString,"\subsection","\subsection")
                    print("SubsectionString:")
                    print(SubsectionString)
                    #create subssection Page
                    #cut subsectionstring from chapter string
                    ChapterString = str.replace(ChapterString,SubsectionString+"\subsection","") 
                    SectionString = str.replace(SectionString,SubsectionString+"\subsection","") 
                else:
                    print("Subsection "+str(Section))
                    Subsection = 1
                    SubsectionString = findBetweenIndex(ChapterString,"\section",len(SectionString)) 
                    #create subssection Page
                    #cut subsectionstring from chapter string 
                    ChapterString = str.replace(ChapterString,SubsectionString+"\subsection","") 
                    SectionString = str.replace(SectionString,SubsectionString+"\subsection","") 
            '''
            #create section Page
            #cut sectionstring from chapter string 
            ChapterString = str.replace(ChapterString,SectionString+"\section","") 
        else:
            '''
            while "\subsection" in SectionString:
                if SectionString.count("\subsection") > 1:
                    print("Subsection "+str(Section))
                    Subsection += 1
                    SubsectionString = findBetween(ChapterString,"\subsection","\subsection")
                    #create subssection Page
                    #cut subsectionstring from chapter string 
                    ChapterString = str.replace(ChapterString,SubsectionString+"\subsection","") 
                    SectionString = str.replace(SectionString,SubsectionString+"\subsection","") 
                else:
                    print("Subsection "+str(Section))
                    Subsection = 1
                    SubsectionString = findBetweenIndex(ChapterString,"\section",len(SectionString))
                    #create subssection Page
                    #cut subsectionstring from chapter string 
                    ChapterString = str.replace(ChapterString,SubsectionString+"\subsection","") 
                    SectionString = str.replace(SectionString,SubsectionString+"\subsection","") 
            '''
            Section = 1
            #create section Page
            #cut sectionstring from chapter string 
            ChapterString = str.replace(ChapterString,SectionString,"") 

BreakIntoChunks("ChapterCounting.tex",1)

