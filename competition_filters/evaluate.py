import filters as fil

import csv
id = []
problems = []
solutions = []

with open('AI_EarthHack_Dataset.csv', mode ='r', encoding="latin1")as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        id.append(lines[0])
        problems.append(lines[1])
        solutions.append(lines[2])
        #print(lines)

vals = []

for i in range (1,3):
    #print(problems[i], solutions[i])
    vals.append(fil.realTech(problems[i], solutions[i], 1))

print(vals)

#id = []
#problems = []
#solutions = []


#for i in range (1, 1302):
#    id.append(i)

#print(id)
#print(id)
#print(problems)
#print(solutions)

"""
row = []
for row in csvreader:
    rows.append(row)
print(rows)
""" #ideally it would be better if we access the id, problem and solution in the same list (this would output a 2-d list). 

#concept: we evalaute each data point of the list with the filter. Remove it if the filter returns not viable.

#Another Idea: Just identify the problem and solution based on what its index in the list is, e.g. item 1 has index 0, etc...  we can match up these things.