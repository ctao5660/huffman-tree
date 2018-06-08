#!/usr/local/bin/python3.6
class Node:
    def __init__(self,frequency,char):
        self.left= None
        self.right=None
        self.frequency=frequency
        self.char=char
    def printTree(node):     #prints tree from leftmost node to rightmost node
        if(node.char!=None):
            print( self.char, end=" ")
        else:
             printTree(self.left)
             printTree(self.right)

class BinaryTree:
    def __init__(self,freqlist): #takes in dictionary with char:frequency that char appears in the text
        self.sortedList=sorted(freqlist, key=freqlist.get) #sorts dictionary from highest freq to lowest freq
        self.sortedList.reverse() #I want lowest to highest 
        self.listlength=len(self.sortedList)
        self.freqList=freqlist
        self.codeDict={} # {char:code that char equals} for encoding purposes
        self.reverseDict={} #{code that char equals:char} for decoding purposes
        self.nodeList=[] 
    def createTree(self): #creates tree by linking each node by .left or .right       returns root node of entire tree
        for char in self.sortedList:
            self.nodeList.append(Node(self.freqList[char],char)) #creates a list of leafnodes that have chars associated with them
        while(True):
            self.nodeList.sort(key=lambda node:node.frequency) #sorts list from lowest to highest frequencies
            node1=self.nodeList.pop(0)
            node2=self.nodeList.pop(0)
            newNode=Node(node1.frequency+node2.frequency,None) #combines two leaf nodes into root node with root freq=node1 frequency+ node2 frequency
            if(node1.frequency>=node2.frequency): #more frequent node goes on left
                newNode.left=node1
                newNode.right=node2
            else:
                newNode.left=node2
                newNode.right=node1
            self.nodeList.append(newNode) #puts new node back into nodeList
            self.nodeList.sort(key=lambda node:node.frequency)
            if(len(self.nodeList)==1): #stops loop if only root node is left
                break
        return self.nodeList.pop(0) #returns root node
    
        
    def SearchAndCode2(self, rNode, encoded): #traverses tree left to right and assigns code to each char, puts into codeDict
        if (rNode is None): #if reached past end node
            return
        if (rNode.char is not None): #found leaf node
            self.codeDict[rNode.char]=encoded
            self.reverseDict[encoded]=rNode.char
            print('Character is {} and Code is {}'.format(rNode.char,encoded))
            return
        lencoded = encoded + "1" 
        rencoded = encoded + "0"
        self.SearchAndCode2(rNode.left, lencoded)
        self.SearchAndCode2(rNode.right, rencoded)

       def isNode(self,stringlist, node): #boolean that takes in string code and returns true or false based on if that code gives char
        s=stringlist
        if (node.char is not  None):
            return True
        if not s:
            return False
        if(s[0]== '1'): #removes first item in list since program already iterated through it, recurses with new list
            s.pop(0) 
            return self.isNode(s,node.left)
        elif(s[0]== '0'):
            s.pop(0)
            return self.isNode(s,node.right)
        return False #if string runs out, return false
#hello

    def decodeMessage(self,filelocation,node): #takes .txt file  of 1's and 0's  and root node, decodes into chars 
        file_test=open(filelocation,'r+')
        encoded=list(file_test.read()) #takes entire string of 1's and 0's and assigns it to a string
        index=0
        string=''
        while index<len(encoded): #iterates through string by char, taking increasingly bigger substrings until the substring matches with the code in codeDict, then resets  
            indexrange=0 
            while(self.isNode(encoded[index:index+indexrange],node) is False): #while program has not found leaf node 
                indexrange+=1
                try: #tries to get substring from codeDict. If doesn't exist, throws KeyError 
                    file_test.write(self.reverseDict[''.join(encoded[index:index+indexrange])])
                    string+=(self.reverseDict[''.join(encoded[index:index+indexrange])])
                    print(self.reverseDict[''.join(encoded[index:index+indexrange])])
                except KeyError: #catches error means code substring doesnt exist, continues with next iteration with while loop, adding 1 to the range of the index
                    continue
            index+=indexrange
        print(string)







def countChars(filelocation): #takes in raw .txt file and counts the frequency of each characters appearance
    file_test=open(filelocation,'r')
    listofchar={}
    charCount=0
    while True:
        print('Hello')
        char=file_test.read(1) #reads 1 character at a time
        if not char: #if reached end of file
            break
        if char not in listofchar:
            listofchar[char]=1
        else:
            listofchar[char]+=1
        charCount+=1
    return listofchar
def encodeMessage(filelocation,newfilelocation, tree):
    file_test=open(filelocation,'r+')
    file_output=open(newfilelocation,'w+')
    numCount=0
    for k,v in tree.reverseDict.items():
        if(v=='\n'): #special case for new line(\n), gets lost when writing to test file
            file_output.write('{}.-.{}\n'.format(k,'\\n')) #escapes \
        else:
            file_output.write('{}.-.{}\n'.format(k,v))
    file_output.write('```\n') # ``` separates the code dictionary from the list of 1's and 0's. Decoder program utilizes this
    while True:
        char=file_test.read(1) #reads 1 char at a time
        if not char: #if EOF
            break
        numCount+=1
        file_output.write(tree.codeDict[char])
    print('Number of bits is {}'.format(numCount/8))


aList=countChars('/Users/christao/downloads/freshprince.txt')
tree=BinaryTree(aList)
aNode=tree.createTree()
tree.SearchAndCode2(aNode,'')
encodeMessage('/Users/christao/downloads/freshprince.txt','/Users/christao/downloads/testparagraph.txt',tree)
print(tree.reverseDict)
#tree.decodeMessage('/Users/christao/downloads/testparagraph.txt',aNode)






