#8.4 Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the split() method.
#The program should build a list of words.
#For each word on each line check to see if the word is already in the list and if not append it to the list.
#When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.split()
    for x in line:
        if x in lst: continue
        lst.append(x)
        lst.sort()
print(lst)





#sorts the new list in A B C order


#print("line.rstrip()", line.rstrip())
#print("lst", lst)
#print("lst[1:]", lst[1:])
    #splitlst = lst.split()
#print("splitlst", splitlst)


#print(lst.rstrip(lst))
#print(line)
#print(line.rstrip())
