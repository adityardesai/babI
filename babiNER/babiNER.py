import sys
import io
import os
import nltk
import collections
from Globals import GlobalsClass
from nltk.tokenize import RegexpTokenizer

class babiNER:
    def __init__(self):
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.text = []
        self.vocabDict = collections.defaultdict(int)
        self.vocabList = []
        self.wordsWithNumbers = []
        self.namedEntitiesList=[]
        wordsWithNumbers = []
    
    def tokenizeInput(self, trainFilePath):
        print("Files are beig read and tokenized ...")
        for root, dirs, files in os.walk(trainFilePath):
            for presentFile in files:
                filePath = os.path.join(root, presentFile)
                with io.open(filePath, "r") as sFile:
                    for textLine in sFile: 
                        self.text += self.tokenizer.tokenize(textLine)
        # print(self.text)
    def removeNumbers(self):
        self.wordsWithNumbers = self.text
        for word in self.wordsWithNumbers:
            if(word.isnumeric() is False):
                self.vocabDict[word] += 1
        #print(len(self.vocabDict))
    def printDetails(vocabDict, vocabList):
        for key, value in vocabDict.items():
            print(key + " : " + str(value))
        print("Dictionary Length " + str(len(vocabDict)))
        for key in vocabList:
            print(key)
    
    def getKeys(self):
        for key in sorted(self.vocabDict.keys()):
            self.vocabList.append(key)
        #print(len(self.vocabList))
    
    def writeVocabToFile(self):
        print("Writing the Vocabluary to file...")
        with io.open(GlobalsClass.VOCAB_FILE, "w") as sFile:
            for word in self.vocabList:
                sFile.write(word)
                sFile.write("\n")
        print("Vocab list written to a file at " + GlobalsClass.VOCAB_FILE)
    
    def writeNERResults(self):
        with io.open(GlobalsClass.VOCAB_NER_FILE, "w") as sFile:
            for word, tag in self.namedEntitiesList:
                sFile.write(word)
                sFile.write(" ")
                sFile.write(tag)
                sFile.write("\n")
        print("VOCAB_NER_FILE file ready at " + GlobalsClass.VOCAB_NER_FILE)
    def tagNER(self):
        print("Named Entities are being identified...")
        from nltk.tag import StanfordNERTagger
        from nltk.tokenize import word_tokenize
        os.environ['JAVAHOME']="/usr/bin/"
        classpath = "/home/aditya/src/stanfordNER/stanford-ner-2015-12-09"
        myText = ""
        st = StanfordNERTagger(GlobalsClass.STANFORD_BABI_NER_CLASSIFIER,
                           GlobalsClass.STANFORD_NER_PATH,
                           encoding=GlobalsClass.ENCODING)
        st._stanford_jar = classpath
        for eachWord in self.vocabList:
            myText += eachWord + " "
        tokenized_text = word_tokenize(myText)
        self.namedEntitiesList = st.tag(tokenized_text)
        #print(self.namedEntitiesList)
        self.writeNERResults()
    def newTokens(self):
        import csv
        with io.open("/home/aditya/newJavaSpace/babI/babiNER/Vocab.tsv", "r") as tsvin:
            tsvin =csv.reader(tsvin, delimiter='\t')
            for row in tsvin:
                print(row)