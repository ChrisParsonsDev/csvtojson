#set up paths and vars
import sys

if len(sys.argv) == 3:
    csvfile = open(sys.argv[1],'r')
    jsonfile = open(sys.argv[2], 'w')
elif len(sys.argv) == 2:
    csvfile = open(sys.argv[1],'r')
    jsonfile = open('output.json', 'w')
else:
    print "Usage - csvtojson.py inputfile.csv output.json"
    sys.exit()


arr=[]
headers = []

# Read in the headers/first row
for header in csvfile.readline().split(','):
    headers.append(header)

# Extract the information into the "xx" : "yy" format.
for line in csvfile.readlines():
  lineStr = ''
  for i,item in enumerate(line.split(',')):
      lineStr+='"'+headers[i] +'" : "' + item + '",\n'
  arr.append(lineStr)

csvfile.close()

#convert the array into a JSON string:
jsn = '{\n "data":['
jsnEnd = ']\n}'
for i in range(len(arr)-1):
    if i == len(arr)-2:
        jsn+="{"+str(arr[i])[:-2]+"}\n"
    else:
        jsn+="{"+str(arr[i])[:-2]+"},\n"
jsn+=jsnEnd

#write to file
jsonfile.write(jsn)
jsonfile.close()
print "Done."
