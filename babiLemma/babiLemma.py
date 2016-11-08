import sys
import io
import os
import collections
import json
from pycorenlp import StanfordCoreNLP
from Globals import GlobalsClass

class babiLemma(object):
    def __init__(self, corenlp_url=GlobalsClass.CORENLP_SERVER):
        self.corenlp = StanfordCoreNLP(corenlp_url)
        self.writeString=""
        self.resJSON=dict()
        self.count=0;
        self.tempDict = dict()
        pass
    def readInput(self, trainFilePath):
        print("Files are beig read and tokenized ...")
        props = { 'annotators': 'tokenize,ssplit,pos,lemma', 'outputFormat': 'json'}
        for root, dirs, files in os.walk(trainFilePath):
            for presentFile in files:
                filePath = os.path.join(root, presentFile)
                with io.open(filePath, "r") as sFile:
                    for textLine in sFile: 
                        output = self.corenlp.annotate(textLine, properties=props)
                        self.parseOutput(textLine, output)
    def parseOutput(self, textLine, output):
        resString = ""
        originalText = ""
        lemma = ""
        resultDict = dict()
        resultDict['Sentence'] = textLine.strip("\n")
        for sentence in output['sentences']:
            for tok in sentence['tokens']:
                originalText = tok['originalText']
                if(tok['pos'] == 'VBD' or tok['pos'] == 'VB' or tok['pos'] == 'VBG' or tok['pos'] == 'VBN'or tok['pos'] == 'VBP'or tok['pos'] == 'VBZ'):
                    resString += "\"POS_Verb\": [" + originalText+"],"
                    lemma +=tok['lemma']
                    resultDict['POS_Verb'] = originalText
                    resultDict['Lemma_Verb'] = tok['lemma']
                elif(tok['pos'] == 'NNP'):
                    resString += "\"POS_NNP\": ["  + originalText +"],"
                    resultDict['POS_NNP'] = originalText
                elif(tok['pos'] == 'NN'):
                    resString += "\"POS_NN\": [" + originalText +"]"
                    resultDict['POS_NN'] = originalText
        self.writeString = self.writeString+"{\"sentence\": "+"\""+textLine.strip("\n") +"\""+ "," + resString + "," + "\"Verb Lemma\"" + ": [" + lemma + "]}"+"\n"
        string1 = json.dumps(resultDict, indent=4, sort_keys=True)
        self.tempDict[self.count] = resultDict
        self.count+=1
        
    def writeToFile(self, str, json):
        if(json == "TRUE"):
            with open(GlobalsClass.JSON_FILE, "a+") as textFile:
                textFile.write(str)
        elif(json == "FALSE"):   
             with open(GlobalsClass.NERTEXT_FILE, "a+") as textFile:
                textFile.write(self.writeString) 

if __name__ == "__main__":
    babiLemma = babiLemma()
    babiLemma.readInput(GlobalsClass.LEMMA_TEXT)
    babiLemma.writeToFile("","FALSE")
    jsonString = json.dumps(babiLemma.tempDict, indent=4, sort_keys=True)
    babiLemma.writeToFile(jsonString, "TRUE")
    #print(babiLemma.writeString)
