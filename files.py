import os
import shutil

def check_dir(directory):
    try: 
        # creating a folder named data 
        if not os.path.exists(directory): 
            os.makedirs(directory) 
    # if not created then raise error 
    except OSError: 
        print ('Error: Creating directory of data') 

def check_file(file_name):
    if not os.path.exists(file_name):
        print("ERROR: The file {} doesn't exist".format(file_name))
        return False
    return True

def check_extention(file_name, extention):
    return file_name if file_name[:-4] == extention else file_name + extention

def delete_folder(path):
    print('Delete {}'.format(path))
    shutil.rmtree(path)
