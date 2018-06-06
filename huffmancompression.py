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
        self.nodeList=[]
    def createTree(self):
        for char in self.sortedList:
            self.nodeList.append(Node(self.freqList[char],char))
        while(True):
            self.nodeList.sort(key=lambda node:node.frequency)
            node1=self.nodeList.pop(0)

            node2=self.nodeList.pop(0)
            newNode=Node(node1.frequency+node2.frequency,None)
            if(node1.frequency>=node2.frequency):
                newNode.left=node1
                newNode.right=node2
            else:
                newNode.left=node2
                newNode.right=node1
            self.nodeList.append(newNode)
            self.nodeList.sort(key=lambda node:node.frequency)
            if(len(self.nodeList)==1):
                break
        return self.nodeList.pop(0)
    
    


    
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
            self.codeDict[rNode.char]=encoded
            print('Character is {} and Code is {}'.format(rNode.char,encoded))
            return
        lencoded = encoded + "1"
        rencoded = encoded + "0"
        self.SearchAndCode2(rNode.left, lencoded)
        self.SearchAndCode2(rNode.right, rencoded)

    def SearchAndCode(self, rNode, targetChar,encoded):
        print('{} is compared to {}'.format(rNode.char,targetChar))
        if(rNode.char!=None and rNode.char==targetChar):
            self.codeDict[targetChar]=encoded
            return
        if(rNode.left!=None):
            self.SearchAndCode(rNode.left,targetChar,encoded+'1')
        if(rNode.right!=None):
            self.SearchAndCode(rNode.left,targetChar,encoded+'0')

    def isNode(self,stringlist, node):
        s=stringlist
        if (node.char is not  None):
            return True
        if(s[0]== '1'):
            s.pop(0)
            return self.isNode(s,node.left)
        elif(s[0]== '0'):
            s.pop(0)
            return self.isNode(s,node.right)
        return False
#hello

    def decodeMessage(self,filelocation):
        file_test=open(filelocation,'r+')
        with file_test as f:
            while True:
                return None







def countChars(filelocation):
    file_test=open(filelocation,'r')
    listofchar={}
    charCount=0
    for word in file_test.read().split():
        for char in list(word):
            if char not in listofchar:
                listofchar[char]=1
            else:
                listofchar[char]+=1
            charCount+=1
    print('Character count is {}'.format(charCount))
    return listofchar
def encodeMessage(filelocation, tree):
    file_test=open(filelocation,'r+')
    numCount=0
    for word in file_test.read().split():
        for char in list(word):
            numCount+=1
            file_test.write(tree.codeDict[char])
    print('Number of bits is {}'.format(numCount/8))
def decodeMessage(filelocation,tree):
    file_test=open(filelocation,'r+')
    for digit in file_test,read().split():
        return None

#aList={'a':54, 'b':26,'c':43, 'd':24}
aList=countChars('/Users/christao/downloads/freshprince.txt')
tree=BinaryTree(aList)
aNode=tree.createTree()
tree.SearchAndCode2(aNode,'')
print(tree.isNode(list('1010'),aNode))

#encodeMessage('/Users/christao/downloads/freshprince.txt',tree)
#for char in aList:
 #   print (char)
  #  encodedString=''
   # tree.SearchAndCode(aNode,char, encodedString)
    #print('--------------------------------------------------')

