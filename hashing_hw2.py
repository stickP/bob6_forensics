import sys
import os
import hashlib
import csv

dirname = sys.argv[1]
hashtype = sys.argv[2].lower()
dirpath = './' + dirname

dict_hash = {}

try:
    file_list= os.listdir(dirpath)

except FileNotFoundError:
    print("There not exists directory " + dirname)

else:
    fpath = []
    for fname in file_list:
        fpath.append(os.path.join(dirpath, fname))

    if hashtype == 'sha256':
        hfunc = hashlib.sha256()
    elif hashtype == 'sha1':
        hfunc = hashlib.sha1()
    elif hashtype == 'md5':
        hfunc = hashlib.md5()
    else:
        print (hashtype + "is not a hash function.")
        sys.exit()
    
    for f in fpath:
        hfunc.update(f.encode('utf8'))
        hashvalue = hfunc.hexdigest()
        dict_hash[os.path.basename(f)] = hashvalue

    print (dict_hash)

    with open('hash.csv', 'w', encoding='utf8') as cfile:
        writer = csv.writer(cfile)
        for key, value in dict_hash.items():
            writer.writerow([key, value])