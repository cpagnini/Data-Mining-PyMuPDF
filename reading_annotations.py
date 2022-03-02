import json

path = "annotations.json"

#######################################################################################################################
#Dictionary's structure (annotation.js)- It is a nested dictionary where every file has a general name: for every general name you have one to many pages and the corrisponding
#pixel coordinates. As an example the geneneral file name PMC3357951 has the following pages: PMC3357951_00001.pdf, PMC3357951_00004.pdf, PMC3357951_00000.pdf
#######################################################################################################################


#Reading annotations.js
d={}
with open(path) as f:
  data = json.load(f)
  for keys, values in data.items():
    if isinstance(values, list):
      continue
    for k,v in values.items():
      d[k] = v
print('Keys\n')
print(d['PMC3357951'].keys())
print('\nValues\n')
print(d['PMC3357951'].values())