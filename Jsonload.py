import json

file = open('helpdb.txt', mode='r')
data = json.load(file)

command = 'CD'
for line in data[command]:
    print(line)

file.close()
