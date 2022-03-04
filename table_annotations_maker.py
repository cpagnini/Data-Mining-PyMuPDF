from reading_annotations import d
import json


def findBackString(string, index):
  if string[index]=='[':
    return index
  return findBackString(string, index-1)


#Creo un secondo dizionario che avrà come keys i nomi delle pagine (estensione .pdf) e come value le coordinate relative

mydict={}

for key in d.keys(): #Per ogni chiave del dizionario
  lst=[] #lista di appoggio per contenere le sole chiavi
  count = 0 #contatore per iterare lungo la  lista
  for values in d[key].values(): #Per ogni valore associato alla chiave del dizionario - Si tratta della combinazione file con estensione .pdf +  coordinate
    for v in values:
      if  '.pdf' in v:
        lst.append(v) #Se sono in presenza del file con estensione .pdf (la mia nuova chiave), la aggiungo alla lista
      else:
        mydict[lst[count]]=v #Altrimenti alimento il mio dizionario con la chiave trovata in precedenza ed il valore delle coordinate
        count+=1

final_dict = {}
# using list comprehension
key1 = ''
for key in mydict.keys():
  value = mydict[key]
  listToStr = ' '.join(map(str, value))
  endTableCoord = listToStr.find(', 4]') 
  
  if endTableCoord!=-1:
    startTableCoord = findBackString(listToStr, endTableCoord)
    final_dict[key] =listToStr[startTableCoord:endTableCoord]
   
print(final_dict)



result = json.dumps(final_dict)
with open('table_coord.json', 'w+') as file:
    file.write(str(result))