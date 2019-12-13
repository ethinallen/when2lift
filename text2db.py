rawData = open('needToMakeDynamoDB.txt', 'r').readlines()

print("THIS IS MY LEN:\t{}".format(len(rawData)))

formattedData = {}

key = ''

for line in rawData:
    if len(line) < 20 and len(line) > 5:
        key = line
        formattedData[key] = []
    else:
        formattedData[key].append(line)

for key in formattedData:
    print("Recorded at time:\t{}".format(key))
