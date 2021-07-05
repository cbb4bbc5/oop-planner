import pickle
from xdg import xdg_cache_home
from os import path
class FileOperations:
    def __init__(self, file=None):
        self.number = 0
        self.__reserved__ = f'save_file_{self.number}'
        if file != None:
            self.file = file
        else:
            self.file = open(path.join(xdg_cache_home(), 'planer', self.__reserved__), 'wb')
            self.number += 1
    
    def save(self, obj):
        if self.__reserved__ in self.file.name:
            self.number += 1
        pickle.dump(obj, self.file)
    
    def delete(self):
        pass
