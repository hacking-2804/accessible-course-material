import os
import re
import shutil

#Files##########################################################################

##DiscreteStructures file contains chapter order and edge case formatting
DiscreteStructures = open("../tex/DiscreteStructures.tex","r") 

##chapter 1
##ChapterIntroduction = open("ChapterIntroduction.tex","r")

#Variables######################################################################
ChapterNames = [] #list that holds every chapter name

#Patterns#######################################################################

##DiscreteStructures file Patterns
ChapterNamePattern = re.compile(r'\\input{(.*?)}') #pulls <CHAPTERNAME>

#Chapter Patterns
IntroPattern = re.compile(r'\\chapter{(.*?)}(.*?)\\section', re.DOTALL) #pulls chapter title and intro blur
SectionTitlePattern = re.compile(r'\\section{(.*?)}') #pulls <SECTIONTITLE>

#Script#########################################################################

##DiscreteStructures scripts
ChapterNamePatternMatches = ChapterNamePattern.findall(DiscreteStructures.read())

for match in ChapterNamePatternMatches:
     ChapterNames.append(match)
     
##Chapter scripts

###Intro

shutil.rmtree("../docs")
os.mkdir("../docs")

PrefaceTexFile = open("../tex/Preface.tex")
PrefaceTex = PrefaceTexFile.read()

try:
    os.mkdir("../docs/Preface")
except FileExistsError:
    print("Directory already exists")

PrefaceMDFile = open("../docs/Preface/Preface.md", "w+")
PrefaceMDFile.write(PrefaceTex)

for i in range(1, len(ChapterNames)):
    ChapterTexFile = open("../tex/{}.tex".format(ChapterNames[i]))
    ChapterTex = ChapterTexFile.read()

    #TODO: remove unnecessary things here
    
    match = IntroPattern.findall(ChapterTex)[0]
    NewDirName = "Chapter-{}".format(i)
    
    try:
        os.mkdir("../docs/"+NewDirName)
    except FileExistsError:
        print("Directory already exists")
    
    ChapterMDFile = open("../docs/{}/{}.md".format(NewDirName, ChapterNames[i]), "w+")
    ChapterMDFile.write("#Chapter {}: {}\n\n{}".format(i, match[0], match[1]))

    #TODO: sections and subsections

    ChapterTexFile.close()
    ChapterMDFile.close()

DiscreteStructures.close()
