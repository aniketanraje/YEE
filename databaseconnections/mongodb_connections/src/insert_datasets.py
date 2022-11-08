import glob
 
path = "./../../../data_extractor/data/*.txt"
for fname in glob.glob(path):
    print(fname)