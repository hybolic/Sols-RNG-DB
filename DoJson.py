from PRELOADER import active_venv
from json      import dumps, loads
from os.path   import exists
from os        import remove
active_venv()


OUTPUT_DIR = "./database/Auras/"
INPUT_DIR  = "./pre_database/Auras/"
AuraList_FILE = "AllAuras"
ENCODER = "UTF-8"

        
def WriteDictToFile(FILE, OBJECT, INDENT="    ",SEPERATOR=(', ', ' : '), ENCODER=ENCODER):
    if exists(FILE):
        remove(FILE)
    with open(FILE,"w",encoding=ENCODER) as file:
        file.write(dumps(OBJECT, ensure_ascii=False, indent=INDENT,separators=SEPERATOR))
        
def QuickTransfer(OUTPUT_DIR, INPUT_DIR, AuraList_FILE):
    with open(INPUT_DIR + AuraList_FILE + ".json", "r", encoding="UTF-8") as file:
        AuraList:dict = loads(file.read())
        
        WriteDictToFile(OUTPUT_DIR + AuraList_FILE + ".json", AuraList)
        WriteDictToFile(OUTPUT_DIR + AuraList_FILE + ".mini.json", AuraList, INDENT=None,SEPERATOR=(",",":"))
        
#DO AURA STUFF
with open(INPUT_DIR + AuraList_FILE + ".json", "r", encoding="UTF-8") as file:
    AuraList:dict = loads(file.read())
    WriteDictToFile(OUTPUT_DIR + AuraList_FILE + ".json", AuraList)
    WriteDictToFile(OUTPUT_DIR + AuraList_FILE + ".mini.json", AuraList, INDENT=None,SEPERATOR=(",",":"))
    
    compacted = AuraList.copy()
    for key, value in compacted.items():
        value.pop("fandom_wiki")
        if "Title" in value.items():
            value.pop("Title")
            
    WriteDictToFile(OUTPUT_DIR + AuraList_FILE + ".compact.json", compacted)
    WriteDictToFile(OUTPUT_DIR + AuraList_FILE + ".compact.mini.json", compacted, INDENT=None,SEPERATOR=(",",":"))
    
    obtainable = AuraList.copy()
    for key, value in AuraList.items():
        if "Unobtainable" in value["rarity"] and not ("native" in value.keys()):
            obtainable.pop(key)
    WriteDictToFile(OUTPUT_DIR + AuraList_FILE + ".obtainable.json", obtainable)
    WriteDictToFile(OUTPUT_DIR + AuraList_FILE + ".obtainable.mini.json", obtainable, INDENT=None,SEPERATOR=(",",":"))

QuickTransfer("./database/Biome/", "./pre_database/Biome/", "Biome")
QuickTransfer("./database/Fish/",  "./pre_database/Fish/",  "Fish")
QuickTransfer("./database/Fish/",  "./pre_database/Fish/",  "Mutation")
QuickTransfer("./database/Fish/",  "./pre_database/Fish/",  "Rarity")