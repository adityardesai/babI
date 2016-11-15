from babiNER import babiNER
from Globals import GlobalsClass

if __name__ == "__main__":
    babiTrain = babiNER()
    babiTrain.newTokens()
    #babiTrain.tokenizeInput(GlobalsClass.TRAINING)
    #babiTrain.removeNumbers()
    #babiTrain.getKeys()
    #babiTrain.writeVocabToFile()
    