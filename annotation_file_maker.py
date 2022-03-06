import json
from pages_tableCoordination_dictionary import dictionaryMaker

#######################################################################################################################
#Creazione nuovo file di annotazioni
#######################################################################################################################

def annotationMaker():
    final_dict = dictionaryMaker
    result = json.dumps(final_dict)
    with open('table_coord.json', 'w+') as file:
        file.write(str(result))
