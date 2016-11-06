import sys
import io
import os
import collections
import json
from pycorenlp import StanfordCoreNLP

class babiLemma(object):
    def __init__(self, corenlp_url='http://localhost:9000'):
        self.corenlp = StanfordCoreNLP(corenlp_url)
        pass
    def tokenizeInput(self, trainFilePath):
        print("Files are beig read and tokenized ...")
        props = { 'annotators': 'tokenize,ssplit,pos,lemma', 'outputFormat': 'json'}
        for root, dirs, files in os.walk(trainFilePath):
            for presentFile in files:
                filePath = os.path.join(root, presentFile)
                with io.open(filePath, "r") as sFile:
                    for textLine in sFile: 
                        #textLine=textLine.split(" ")
                        output = self.corenlp.annotate(textLine, properties=props)
                        #print(output)
                        self.parseOutput(textLine,output)
    def parseOutput(self,textLine,output):
        resLabel=""
        originalText=""
        lemma=""
        result=dict()
        result['Sentence']=textLine
        for sentence in output['sentences']:
            for tok in sentence['tokens']:
                originalText=tok['originalText']
                if(tok['pos']=='VBD'):
                    resLabel+="VBD"+"\t"+originalText+"\t"
                    lemma+="\t"+tok['lemma']+"\t"
                    result['VBD']=originalText
                    result['Lemma']=tok['lemma']
                elif(tok['pos']=='NNP'):
                    resLabel+="NNP"+"\t"+originalText+"\t"
                    result['NNP']=originalText
                elif(tok['pos']=='NN'):
                    resLabel+="NN"+"\t"+originalText+"\t"
                    result['NN']=originalText
        #print(textLine.strip("\n")+"\t"+"{"+resLabel+"}"+"\t"+"VBD Lemma"+"["+lemma+"]")
        s3 = json.dumps(result, indent=4, sort_keys=True)
        print(s3)
if __name__ == "__main__":
    babiLemma = babiLemma()
    babiLemma.tokenizeInput("/home/aditya/newJavaSpace/babI/Tests/Test_single/lemmaTest")