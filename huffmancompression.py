#!/usr/local/bin/python3.6
class Node:
    def __init__(self,frequency,char):
        self.left= None
        self.right=None
        self.frequency=frequency
        self.char=char
    def printTree(node):
        if(node.char!=None):
            print( self.char, end=" ")
        else:
             printTree(self.left)
             printTree(self.right)

class BinaryTree:
    def __init__(self,freqlist):
        self.sortedList=sorted(freqlist, key=freqlist.get)
        self.sortedList.reverse()
        self.listlength=len(self.sortedList)
        self.freqList=freqlist
        self.codeDict={}
    def createTree(self):
        while len(self.sortedList)!=1:
            if(len(self.sortedList)==self.listlength):
                character=self.sortedList.pop(0)
                freq=self.freqList[character]
                node1=Node(freq,character)
                character=self.sortedList.pop(0)
                freq=self.freqList[character]
                node2=Node(freq,character)
            else:
                node1=self.sortedList.pop(0)
                character=self.sortedList.pop(0)
                freq=self.freqList[character]
                node2=Node(freq,character)
            rootNode=Node(node1.frequency+node2.frequency,None)
            if(node1.frequency>node2.frequency):
                rootNode.left=node1
                rootNode.right=node2
            else:
                rootNode.left=node2
                rootNode.right=node1
            self.sortedList=[rootNode]+self.sortedList
        root=self.sortedList.pop(0)
        return root
    def printTree(self,node):
        if(node.char!=None):
            print( node.char, end=" ")
        else:
            self. printTree(node.left)
            self.printTree(node.right)
    def SearchAndCode2(self, rNode, encoded):
        if (rNode is None):
            return
        if (rNode.char is not None):
            print( "%s %s" % (rNode.char, encoded))
            return
        lencoded = encoded + "0"
        rencoded = encoded + "1"
        
        self.SearchAndCode2(rNode.left, lencoded)
        self.SearchAndCode2(rNode.right, rencoded)

    def SearchAndCode(self, rNode, targetChar,encoded):
        print('{} is compared to {}'.format(rNode.char,targetChar))
        if(rNode.char!=None and rNode.char==targetChar):
            self.codeDict[targetChar]=encoded
            print(encoded)
            return 
        if(rNode.left!=None):
            self.SearchAndCode(rNode.left,targetChar,encoded+'1')
        if(rNode.right!=None):    
            self.SearchAndCode(rNode.left,targetChar,encoded+'0')
        





def countChars(filelocation):
    file_test=open(filelocation,'r')
    listofchar={}
    for word in file_test.read().split():
        for char in list(word):
            if char not in listofchar:
                listofchar[char]=1
            else:
                listofchar[char]+=1
    return listofchar

aList={'a':3, 'b':12, 'c':2}
#aList=countChars('Downloads/freshprince.txt')
tree=BinaryTree(aList)
aNode=tree.createTree()
tree.SearchAndCode2(aNode,'')
print(aNode.frequency)

for char in aList:
    print (char)
    encodedString=''
    tree.SearchAndCode(aNode,char, encodedString)
    print('--------------------------------------------------')


