#def movesLeftMargin(startNum):
    #starts cursor at "" inch(es) on left Margin
    #formatter.push_margin(startNum)

#def moveLeftMarginBack():
    #formatter.pop_margin()
    
import random

def moveLeftMargin(num):
  index = 0
  while index is not num:
    print(" ")
    index = index + 1
  return

x = random.randint(50, 80)
fr = open('DAT1.txt','r')
fw = open('textFile.txt','a')
text = fr.read()
numCharInLine = 80
leftMargin = int(input("Enter left margin number: "))
rightMargin = leftMargin + numCharInLine
print(rightMargin)
#i = 0
#while i < (len(text)):
  #index = 0
  #moveLeftMargin(leftMargin)
  #while index < rightMargin:
    #fw.write(text[i])
    #index = index + 1
    #i = i + 1
  #for j in range(0, leftMargin):
    #print(" ")
  #print(text[i])
  #fw.write(text[i])
  #i = i + 1
  #fw.write('/n')
index = 0
for h in range(0, leftMargin):
  fw.write(" ")
for i in range(0, len(text)):
  if index < numCharInLine:
    print(text[i])
    fw.write(text[i])
    index = index + 1
  else:
    index = 0
    fw.write('\n')
    for j in range(0, (leftMargin + 1)):
      fw.write(" ")
    print(text[i])
    fw.write(text[i])
  
fr.close()
fw.close()
