import os
from datetime import datetime



def getTextExtension():
    extension_list = []
    folder_path = 'C:\\python_task\\'
    file_list = os.listdir(folder_path)
    print(folder_path)
    extension_dict = {}
    for i in file_list:
        if '.txt' in i:
            extension_list.append(i)
    
    for i in extension_list:
        mod_time = os.path.getmtime(folder_path + i)
        extension_dict[i] =  datetime.fromtimestamp(mod_time)
    return extension_dict
        
print(getTextExtension())












