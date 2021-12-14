'''
author : Thura Aung
Tokenization
Stop words remove 
Cleanning - remove punctuations, english numbers and letters
Ready to use for text pre-processing 
'''
import argparse
import re
import pyidaungsu as pds

parser = argparse.ArgumentParser(description='Pre-processing for Myanmar language')
parser.add_argument('-i', '--input', type=str, help='input file', required=True)
parser.add_argument('-o', '--output', type=str, default='sylbreak_out.txt', help='output file', required=True)
parser.add_argument('-s', '--separator', type=str, default=r'|', help='the separator option for syllable (e.g. -s "/"), default is "|"', required=True)
args = parser.parse_args()

inputFile = getattr(args, 'input')
outFile = getattr(args, 'output')
sOption = getattr(args, 'separator')
data = "" 

CleanPattern = re.compile(r'\d+|[၊။!-/:-@[-`{-~\t ]|[A-za-z0-9]')

stopwordslist = []
slist = []
with open("../data/stop_words.txt", encoding = 'utf8') as stopwordsfile:
    stopwords = stopwordsfile.readlines()
    slist.extend(stopwords)

    for w in range(len(slist)):
        temp = slist[w]
        stopwordslist.append(temp.rstrip())
        

def clean_sentence(sentence):
    sent = CleanPattern.sub(" ",sentence)
    return sent

def removeStopWord(text,stopwordslist):
    vWord = text
    returnList = []       
    
    for v in vWord:
        if v in stopwordslist:
            continue
        else:
            returnList.append(v)

    tempp = ""
    for ff in returnList:
        if (len(returnList)>0):
            if ff == returnList[-1]:
                tempp += ff
            else:
                tempp += ff+" "
            
    return tempp

def tokenize(line):
    sentence = pds.tokenize(line,form="word")
    sentence = removeStopWord(sentence,stopwordslist)
    cleaned = clean_sentence(sentence)
    return cleaned

with open(file_path) as fp:
    line = fp.readline()
    while line:
        data += "\n" + tokenize(line)
        line = fp.readline()

# Writing Data to Output File
if outFile:
    with open(outFile, 'w',  encoding='utf-8') as file:
        file.write(data)
        print(f"Word Tokenization succcessfully done. Write data to {outFile}")