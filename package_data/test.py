import os, shelve

def format_same_loc():
    loc_data = {}
    
    try:
        os.chdir('py_data')
    except (FileNotFoundError):
        os.chdir('..')
        os.mkdir('py_data')
        os.chdir('py_data')
##    file = open(py_filename, 'r')
##    t = file.read()
##    print(type(t))
##    file.close()

    shelfFile = shelve.open('test')
    type(shelfFile)
    for v in shelfFile['data']:
        print(v)
    shelfFile.close()

format_same_loc()
