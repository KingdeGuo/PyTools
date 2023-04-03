import re

with open('领域词典test.txt', 'r') as f:
    contents = f.read()

groups = re.findall(r'(\d+)(\D+)', contents)
grouped_contents = [groups[i:i+10] for i in range(0, len(groups), 10)]

datafile = open("data.txt", 'w')
mat = "{:2} {:20}"
for group in grouped_contents:
    for item in group:
        print(mat.format(item[0], item[1].strip()), end='\t')
        datafile.write(mat.format(item[0], item[1].strip()) + "\t")
    print('\n')
    datafile.write("\n")
# add a blank line