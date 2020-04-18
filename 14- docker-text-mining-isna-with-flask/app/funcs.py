import pickle

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


    
