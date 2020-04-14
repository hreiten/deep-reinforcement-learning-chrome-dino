import pickle
def save_pkl(fpath, obj):
    with open(fpath, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        
def load_pkl(fpath):
    with open(fpath, 'rb') as f:
        return pickle.load(f)
