import networkx as nx
import collections
import matplotlib.pyplot as plt

# myDict = dict()
# myDict[1]='move'
# 
# G=nx.Graph()
# G.add_node("Mary")
# G.add_node("Bedroom")
# G.add_edge("Mary","Bedroom",attr_dict=myDict)
# nx.draw(G)
# 
# 
# 
# print(G.nodes())
# print(G.edges())
# print(G.get_edge_data('Mary','Bedroom'))
# plt.show()

#   General Rep 
#   babiGraphObj.addNode('Actor')
#   babiGraphObj.addNode('Location/Object')
#   babiGraphObj.addToTSLemmaDict(TimeStamp(feature number),'lemma')
#   babiGraphObj.addEdge('Actor', 'Location/Object')

class babiGraph():
    def __init__(self):
        self.edgeList=[]
        self.nodeList=[]
        self.timeStampLemmaDict = dict()
        self.G=nx.Graph()
    def addToTSLemmaDict(self,TS,lemma):
        self.timeStampLemmaDict[TS]=lemma
    def addEdge(self,u,v):
        self.edgeList.append((u,v))#add it as tuple
    def addNode(self,node):
        self.nodeList.append(node)
    def createGraph(self):
        self.G.add_edges_from(self.edgeList,self.timeStampLemmaDict)
        self.G.add_nodes_from(self.nodeList)
    def getNodeList(self):
        print("NodeList")
        print(self.nodeList)
        print(len(self.nodeList))
    def getEdgeList(self):
        print("EdgeList")
        print(self.edgeList)
        print(len(self.edgeList))
    def getTimeStampLemmaDict(self):
        for timeStamp,Lemma in self.timeStampLemmaDict.items():
            print("For TimeStamp " + str(timeStamp)+ " associated Lemma is "+" : " + Lemma)
    def displayGraph(self):
        nx.draw(self.G,with_labels=True)
        plt.show()
if __name__ == "__main__":
    babiGraphObj = babiGraph()
    
    babiGraphObj.addNode('Mary')
    babiGraphObj.addNode('bathroom')
    babiGraphObj.addToTSLemmaDict(1,'move')
    babiGraphObj.addEdge('Mary', 'bathroom')
    
    babiGraphObj.addNode('Sandra')
    babiGraphObj.addNode('bedroom')
    babiGraphObj.addToTSLemmaDict(2,'journey')
    babiGraphObj.addEdge('Sandra', 'bedroom')
    
    babiGraphObj.addNode('Mary')
    babiGraphObj.addNode('football')
    babiGraphObj.addToTSLemmaDict(3,'get')
    babiGraphObj.addEdge('Mary', 'football')
    
    babiGraphObj.addNode('John')
    babiGraphObj.addNode('kitchen')
    babiGraphObj.addToTSLemmaDict(4,'go')
    babiGraphObj.addEdge('John', 'kitchen')
    
    babiGraphObj.addNode('Mary')
    babiGraphObj.addNode('kitchen')
    babiGraphObj.addToTSLemmaDict(5,'go')
    babiGraphObj.addEdge('Mary', 'kitchen')
    
    babiGraphObj.addNode('Mary')
    babiGraphObj.addNode('garden')
    babiGraphObj.addToTSLemmaDict(6,'go')
    babiGraphObj.addEdge('Mary', 'garden')
    
    babiGraphObj.createGraph()
    
    babiGraphObj.getEdgeList()
    babiGraphObj.getNodeList()
    babiGraphObj.getTimeStampLemmaDict()
    babiGraphObj.displayGraph()