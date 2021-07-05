import pickle
from xdg import xdg_cache_home
import os
class FileOperations:
    def __init__(self, name=None):
        self.number = 0
        self.name = name
        if name == None:
            self.name = 'save_file'
        #self.file = open(os.path.join(xdg_cache_home(), 'planer', self.name), 'wb')

    def save(self, obj):
        tmp_name =  f'{self.name}_{self.number}'
        pickle.dump(obj, open(tmp_name, 'wb'))
        self.number += 1
        return tmp_name
    
    def delete(self, name):
        if os.path.exists(name):
            os.remove(name)
