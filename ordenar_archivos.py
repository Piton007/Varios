import os, time, shutil


def get_files_actual_directory(path):
    actual_my_directory=[]
    actual_my_directory.extend([ (file,None) for root,dirs,files in os.walk(path) if len(files)>0 for file in files ])
    return dict(actual_my_directory)
def moveFilesToDirectory(watchedDirectory):
    for file in watchedDirectory:
        extension=file.split(".").pop(-1)
        old_path="{path}\{file}".format(**(dict(path=path_to_watch,file=file)))
        new_directory = "{path}\{newDirectory}".format(**(dict(path=path_to_destination,newDirectory=extension.upper())))
        new_path=new_directory+"\{}".format(file)
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)
        shutil.move(old_path,new_path)
path_to_watch=input("Ingrese el path del directorio a observar: ")
path_to_destination=input("Ingrese el path del  directorio destino: ")
my_directory_dic=get_files_actual_directory(path_to_destination)
while 1:
  time.sleep (10)
  download_directory = dict ([(f, None) for f in os.listdir (path_to_watch)])
  moveFilesToDirectory(download_directory)
 
  
  



    




