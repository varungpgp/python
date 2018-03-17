##code is for python for everybody assignment 9.4
# Write a program to read through the mbox-short.txt and figure out who
#has the sent the greatest number of mail messages. The program looks for
#'From ' lines and takes the second word of those lines as the person who
#sent the mail. The program creates a Python dictionary that maps the
#sender's mail address to a count of the number of times they appear in the
#file. After the dictionary is produced, the program reads through the
#dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
handle = open(name)
dicti = dict()

for data in handle:
    if data.startswith('From:'):
        continue
    elif data.startswith('From'):
        splitting = data.split()
        val = splitting[1]
        #print(val)
        dicti[val] = dicti.get(val,0) + 1

findvalue = None
name = None
for email,value in dicti.items():
    if findvalue is None or value > findvalue:
       findvalue = value
       name = email
print(name, findvalue)
