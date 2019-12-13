import re
import seaborn as sns
import time as t


rawData = open('needToMakeDynamoDB.txt', 'r').readlines()

print("THIS IS MY LEN:\t{}".format(len(rawData)))

formattedData = {}

key = ''

for line in rawData:
    if len(line) < 20 and len(line) > 5:
        key = line
        formattedData[key] = []
    elif line != '\n':
        formattedData[key].append(line)

for key in formattedData:
    for entry in formattedData[key]:
        print("ENTRY:\t{}".format(entry))
        count = re.findall("Last Count: \d+Updated", entry)
        count = int(count[0][11:-7])
        print("Count:\t{}".format(count))
        # print("Recorded at time:\t{}".format(key))
