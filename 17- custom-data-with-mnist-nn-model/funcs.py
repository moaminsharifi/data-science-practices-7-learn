import pickle
import os
def put(filname , data, customPath = False):
    filePath = '{}.pickle'.format(filname)
    if customPath:
        filePath = filname
        
    with open(filePath, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
        print("""
        {} save in {}
        """.format(filname, filePath))
        
        
        
def get(filname, customPath = False):
    filePath = '{}.pickle'.format(filname)
    if customPath:
        filePath = filname
    with open(filePath, 'rb') as handle:
        data = pickle.load(handle)
        print("""
        read {} from {} ended.
        """.format(filname, filePath))
        return data  


    
def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result
 
def mkdirs(paths = []):
    for path in paths:
        if(os.path.exists(path)):
            pass
        else:
            os.makedirs(path)

def copys(srcs , tagets):
    import shutil
    assert len(srcs) == len(tagets)
    for idx in range(len(srcs)):
        shutil.copy2(srcs[idx], tagets[idx])

def files_exist(paths = []):
    for path in paths:
        if not os.path.exists(path):
            return False
    return True

def rename_all_file_by_number(paths  = [], ext= '.jpg'):
    for path in paths:
        path_files = os.listdir(path)
        i = 0
        for file in path_files:
            src = '{}/{}'.format(path,file)
            target = '{}/{}{}'.format(path,i , ext)
            os.rename(src, target)
            i = i + 1