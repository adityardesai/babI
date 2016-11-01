from babiNER import babiNER
from Globals import GlobalsClass

if __name__ == "__main__":
    babiTest = babiNER()
    babiTest.tokenizeInput(GlobalsClass.TEST)
    babiTest.removeNumbers()
    babiTest.getKeys()
    #babiTest.tagNER()