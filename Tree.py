class TrieNode:
    isEnd = None
    child = None
    count = 0
    def __init__(self):
        self.isEnd = False
        self.child = [None for i in range(27)]       
class TrieTree:
    root = None
    def __init__(self):
        self.root = TrieNode()
    def InsertSequence(self , string):
        Tmproot = self.root
        for i in range(0 , len(string)):
            index = ord(string[i])-ord('A')
            if Tmproot.child[index] == None:
                Tmproot.child[index] = TrieNode()
            if Tmproot.child[index] != None:
                Tmproot.child[index].count+=1
            Tmproot = Tmproot.child[index]
        Tmproot.isEnd= True
    def isSequence(self , string):
        Tmproot = self.root
        for i in range(0 , len(string)):
            index = ord(string[i])-ord('A')
            if Tmproot.child[index] == None:
                return False
            Tmproot = Tmproot.child[index]
        if Tmproot.isEnd == False:
            return False
        return True
    def isPrefixSequence(self , string):
        Tmproot = self.root 
        for i in range(0 , len(string)):
            index = ord(string[i])-ord('A')
            if Tmproot.child[index] == None:
                return False
            Tmproot = Tmproot.child[index]
        return True
    def isempty(self , ROOT):
        for i in range(27):
            if ROOT.child[i] != None:
                return False
        return True
    def DeleteSequence(self , ROOT , string , depth=0):
        if not ROOT:
            return None
        if depth == len(string):
            ROOT.isEnd = False
            if self.isempty(ROOT):
                del(ROOT)
                ROOT = None
            return ROOT
        index = ord(string[depth]) - ord('A')
        ROOT.child[index].count -= 1
        ROOT.child[index] = self.DeleteSequence(ROOT.child[index] ,string ,depth+1)
        if(self.isempty(ROOT) and ROOT.isEnd == False):
            del(ROOT)
            ROOT = None;    
        return ROOT;
    def CountPrefixSequence(self , string ):
        Tmproot = self.root 
        for i in range(0 , len(string)):
            index = ord(string[i])-ord('A')
            if Tmproot.child[index] == None:
                return 0
            Tmproot = Tmproot.child[index]
        return Tmproot.count

x = TrieTree()

               
            
        
    
    