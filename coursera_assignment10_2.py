#this code is for python for everybody assignment 10.2
# Write a program to read through the mbox-short.txt and figure out
#the distribution by hour of the day for each of the messages. You can
#pull the hour out from the 'From ' line by finding the time and then
#splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.

name = input("Enter file:")
fh = open(name)
lst = list()
di = dict()

for data in fh:
    if data.startswith('From:'):
       continue
    elif data.startswith('From'):
        data =  data.rstrip()
        strin = data.split()
        new = strin[5]
        hour = new[0:2]
        #print(hour)
        di[hour] = di.get(hour,0) + 1


for date,value in di.items():
    data = (date, value)
    lst.append(data)
    lst.sort()

for date,value in lst:
    print(date, value)
