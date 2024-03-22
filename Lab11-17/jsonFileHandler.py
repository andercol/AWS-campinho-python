


# 126- [PF] -Lab - Manipuladores de arquivos e módulos para recuperar informações sobre insulina

import json

def readJsonFile(filename):
    data=""
    try:
        with open('files/insulin.json') as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data


