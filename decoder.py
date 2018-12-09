#! /usr/local/bin/python3.6
def getDictionary(fileLocation):
    reverseDict={}
    inputfile=open(fileLocation,'r+')
    for line in inputfile.read().split("\n"):
            separator=line.find('.-.') 
            reverseDict[line[:separator]]=line[(separator+3):]
            if(line=='```'): #end of dict
               return reverseDict
def intepretFile(fileLocation):
    inputfile=open(fileLocation,'r+')
    separator=0
    string=''
    iterator=0
    for line in inputfile.read().split("\n"):
        if '```' in line: #looking for special character symbolizing end of dict
            break
        else:
            separator+=1
    inputfile.close()

    inputfile=open(fileLocation,'r+')
    for line in inputfile.read().split("\n"):
        if iterator>separator:
            string+=line
        iterator+=1
    return string
def decode(string, reverseDict,outputFileLocation):
    index=0
    s=''
    file_output=open('outputFileLocation','w+')
    while(index<len(string)):
        indexrange=0
        while True:
            indexrange+=1
            try:
                file_output.write(reverseDict[string[index:index+indexrange]])
            except KeyError:
                continue
            else:
                if(reverseDict[string[index:index+indexrange]]=='\\n'):
                    s+='\n'
                else:
                    s+=reverseDict[string[index:index+indexrange]]
                    print('{} is mapped to {}'.format(string[index:index+indexrange],reverseDict[string[index:index+indexrange]]))
                index+=indexrange
                break
    print(s)
                
            
reverseDict=getDictionary('/Users/christao/downloads/testparagraph.txt')
print(reverseDict)
write=intepretFile('/Users/christao/downloads/testparagraph.txt')
decode(write,reverseDict,'Users/christao/downloads/finaloutput.txt')
