import commands
import sys
import os 
import shutil

print "Oldest 10 files in the current directory(Access Time):"
print ""

a = commands.getoutput('ls -ltu | sort | tail -n 10 > output.txt') 
file1 = open("output.txt","r")
k = 1
line2 = []
lines = file1.readlines()
lines = lines[:-1]
for line in lines:
	line = str(k) + " ) " + line
	#print line
#	k+=1
	line1 = line.split()
	line1 = line1[10:]
	sr = str(line1)
#	print sr
	line3 =' '.join(line1)
#	print line3

#	line3 = sr.join(sr)
	line2.append(line3)

print line2

for i in line2:
	kalu = str(k) + " ) " + i
	k+=1
	print kalu


#ignore last line which has totals

str1 = ""

print "Enter Number to remove file "

while 1:
	str1 = raw_input("Press to EXIT to exit :")
	if str1.upper() == "EXIT":
		sys.exit(-1)
	#dire = 'rm -f ' + line2[int(str1) - 1]
	x = "Press Y to confirm delete this file and N to not: " + line2[int(str1) - 1] + "\n"
	temp = raw_input(x)

	if temp.upper() == "Y":
		if os.path.isdir(line2[int(str1) - 1]):
			shutil.rmtree(line2[int(str1) - 1])
		else:
			os.remove(line2[int(str1) - 1])
		del line2[int(str1) - 1]
	else:
		continue
		

print line2	




