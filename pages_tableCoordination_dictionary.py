from reading_annotations import d

#######################################################################################################################
#Creating a new dictionary having as keys the 'pages' and as values the table's coordinates only
#######################################################################################################################

#This method allow to find the beginning of coordinates required
def findBackString(string, index):
  if string[index]=='[':
    return index
  return findBackString(string, index-1)


mydict={}

#A new dictionary is created with 'pages' and every annotations related to it.
for key in d.keys(): 
  lst=[] 
  count = 0 
  for values in d[key].values(): #Values can be either 'pages' - .pdf - and coordinates.
    for v in values:
      if  '.pdf' in v:
        lst.append(v) 
      else:
        mydict[lst[count]]=v 
        count+=1


#Creating the final dictionary with 'pages' and their table's coordinates.
final_dict = {}
for key in mydict.keys():
  value = mydict[key]
  listToStr = ' '.join(map(str, value))
  endTableCoord = listToStr.find(', 4]') #4 is the Category corrisponding to the table's coordinates
  
  if endTableCoord!=-1:
    startTableCoord = findBackString(listToStr, endTableCoord)
    final_dict[key] =listToStr[startTableCoord:endTableCoord]
   

