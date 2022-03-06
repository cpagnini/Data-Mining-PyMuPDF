import json
import fitz
import os
import glob
from operator import itemgetter
from itertools import groupby

def annotationsExtract():
    with open('table_coord.json') as json_file:
        d = json.load(json_file)
    return d

"""
-------------------------------------------------------------------------------
Manage PDF
-------------------------------------------------------------------------------
"""
def renderingText(text, rect):
    
  """Text will be orderdered from left to right and from top to bottom
  """
  eeprofile = [w for w in text if fitz.Rect(w[:4]).intersects(rect)]
  eeprofile.sort(key=itemgetter(3, 0))
  stats = groupby(eeprofile, key = itemgetter(3))
  for y1, gwords in stats:
        print(" ".join(w[4]for w in gwords))

def extractFromPDF(path, rect):
  #Open pdf file passed via path variabile.
  #Select a rectangle thanks to the rect variable.
  print('\nExtracting ', os.path.basename(path) + '\n')
  print('----------------------------------------------')
  try:
    doc =fitz.open(path)
    pdfbytes = doc.convert_to_pdf()  
    pdf = fitz.open("pdf", pdfbytes)
    page = pdf[0]
    words = page.get_text("words")  #Listing of words
    renderingText(words, rect)
  except:
    print('Error occurred')
 

"""
-------------------------------------------------------------------------------
Converting to BBOX coordinates 
-------------------------------------------------------------------------------
"""

def bboxCoords(coordinates):
  bbox=[]
  conversion = 0.36
  for c in coordinates:
    bbox.append(float(c)*conversion)
  return bbox

"""
-------------------------------------------------------------------------------
Processing PDF
-------------------------------------------------------------------------------
"""

def pdfProcessing():
    path = "PDFile/"
    pdfFiles = glob.glob(path +"/*.pdf")
    pdfFilesNoPath =[]
    for file in pdfFiles:
        pdfFilesNoPath.append(os.path.basename(file))
    d = annotationsExtract()
    i=0
    for file in pdfFilesNoPath:
        if file in d.keys():
            i+=1
            filePath = path+file
            coordinates =d.get(file).replace('[','').replace(']','').replace(' ','').split(',') 
            x0, y0, x1, y1 = bboxCoords(coordinates)
            rect = fitz.Rect(x0, y0, x1, y1)
            print('----------------------------------------------')
            print('\nProcessing doc number : '+str(i))
            extractFromPDF(filePath, rect)