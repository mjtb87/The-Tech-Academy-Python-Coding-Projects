

import os
from datetime import datetime



def getTextExtension():
    folder_path = 'python_extensions_search'
    file_list = os.listdir(folder_path)
    extension_dict = {}
    for i in file_list:
        if '.txt' in i:
            mod_time = os.stat(os.path.join(folder_path, i)).st_mtime
            extension_dict[i] =  datetime.fromtimestamp(mod_time)  
    
    return extension_dict
        
        
    
print(getTextExtension())














