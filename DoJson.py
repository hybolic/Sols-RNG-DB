from PRELOADER import active_venv
active_venv()
import os, json


OUTPUT_DIR = "./database/Auras/"
INPUT_DIR  = "./pre_database/"
AuraList_FILE = "Auras"
ENCODER = "UTF-8"

        
def WriteDictToFile(FILE, OBJECT, INDENT="    ",SEPERATOR=(', ', ' : '), ENCODER=ENCODER):
    if os.path.exists(FILE):
        os.remove(FILE)
    with open(FILE,"w",encoding=ENCODER) as file:
        file.write(json.dumps(OBJECT, ensure_ascii=False, indent=INDENT,separators=SEPERATOR))

#TODO: Crawl Pre_database folder and append to correct database folder

file = AuraList_FILE
OUTPUT_FILE = file
with open(INPUT_DIR + file + ".json", "r", encoding="UTF-8") as file:
    AuraList:dict = json.loads(file.read())
    
    WriteDictToFile(OUTPUT_DIR + OUTPUT_FILE + ".json", AuraList)
    WriteDictToFile(OUTPUT_DIR + OUTPUT_FILE + ".mini.json", AuraList, INDENT=None,SEPERATOR=(",",":"))
    
    compacted = AuraList.copy()
    for key, value in compacted.items():
        value.pop("fandom_wiki")
        if "Title" in value.items():
            value.pop("Title")
            
    WriteDictToFile(OUTPUT_DIR + OUTPUT_FILE + ".compact.json", compacted)
    WriteDictToFile(OUTPUT_DIR + OUTPUT_FILE + ".compact.mini.json", compacted, INDENT=None,SEPERATOR=(",",":"))
    
    obtainable = AuraList.copy()
    for key, value in AuraList.items():
        if "Unobtainable" in value["rarity"] and not ("native" in value.keys()):
            obtainable.pop(key)
    WriteDictToFile(OUTPUT_DIR + OUTPUT_FILE + ".obtainable.json", obtainable)
    WriteDictToFile(OUTPUT_DIR + OUTPUT_FILE + ".obtainable.mini.json", obtainable, INDENT=None,SEPERATOR=(",",":"))