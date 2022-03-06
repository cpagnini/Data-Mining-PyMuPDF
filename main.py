import os
from data_extraction import pdfProcessing
from annotation_file_maker import annotationMaker

filePath = 'table_coord.json'
if os.path.exists(filePath):
    os.remove(filePath)
annotationMaker()
pdfProcessing()