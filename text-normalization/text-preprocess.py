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
parser.add_argument('-o', '--output', type=str, default='preprocessing.txt', help='output file', required=True)
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

def stop_word(sentence):
  new_sentence = []
  for word in sentence.split():
    if word not in stopwordslist:
      new_sentence.append(word)
  return(' '.join(new_sentence))

def tokenize(line):
    sentence = pds.tokenize(line,form="word")
    sentence = stop_word(sentence)
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
