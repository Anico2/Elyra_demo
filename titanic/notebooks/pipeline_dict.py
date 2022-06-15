import os
import pickle

#to do: input checks

dict_with_pickles = {}
def import_pickled_dict(diz, current_path):
    parent_parent = os.listdir(os.path.dirname(os.getcwd()))
    parent_parent[parent_parent.index("dati")]
    parent_dir = os.path.dirname(os.getcwd())+"\\"+parent_parent[0]
    for f in os.listdir(parent_dir):
        if os.path.isfile(os.path.join(current_path, f)):
            names = f.split("_")
            if "dict" in names:
                key = names[0]+names[1]
                with open(f, 'rb') as pick:
                    diz[key] = pickle.load(file=pick)
                    
import_pickled_dict(dict_with_pickles, os.getcwd())


#to do: check sort of the dict

##.. other operations

write_path = os.getenv("PATH_NAME", None)

if write_path:
    with open(write_path+"pipeline_dict.pickle", 'wb') as handle:
        pickle.dump(import_pickled_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
else:
    raise ValueError("wrong path")