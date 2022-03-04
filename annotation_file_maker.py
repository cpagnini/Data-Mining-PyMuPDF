import json
from pages_tableCoordination_dictionary import final_dict

#######################################################################################################################
#Creazione nuovo file di annotazioni
#######################################################################################################################

result = json.dumps(final_dict)
with open('table_coord.json', 'w+') as file:
    file.write(str(result))
