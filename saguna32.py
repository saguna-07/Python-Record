import os.path
import sys
fname = input("Enter the filename : ")
if not os.path.isfile(fname):
 print("File", fname, "doesn't exists")
 sys.exit(0)
infile = open(fname, 'r')
lineList = infile.readlines()
lineCount = int(input("Enter the number of lines you want to display : "))
for i in range(lineCount):
 print(i+1, ":", lineList[i], end="")
word = input("Enter a word : ")
cnt = 0
for line in lineList:
 cnt += line.count(word)
print("The word", word, "appears", cnt, "times in the file")