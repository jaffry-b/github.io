import os
import datetime
import sys
import shutil
import random 

root_directory= os.getcwd()

directory = './assets/images/Japan'

weight= 0
####

def createToFile(w,fpath,title):
    file_obj = open("truework" + "-" + w + ".md","w")
    file_obj.write("---\n")
    file_obj.write("weight: " + w + "\n" + "images: \n- " + fpath + "\n" + "title: " + title + " " + w + "\n")
    file_obj.write("date: " + str(datetime.date.today())+"\n")
    file_obj.write("tags:\n" + "- " + title + "\n" + "---")
    file_obj.close()

def importImagePath(w,file,title):
        if file.is_file():
            createToFile(str(w),file.path[8:],title)
        

def beginOperation(w,title):
    target_dir = sorted(os.scandir(directory), key=lambda e: e.name)
    for file in target_dir:
            if file.is_file():
                w += 1
                importImagePath(w,file,title)
            else:
                print("exiting!")
                exit

def main():
    title="Default"
    pr=False
    if len( sys.argv ) > 1:
        if sys.argv[1] == "-d":
            for item in os.listdir("."):
                if item.endswith(".md"):
                    [print("deleting... " + item)]
                    os.remove(os.path.join(".", item))
        elif sys.argv[1] == "-r":
            if sys.argv[2] :
                title = str(sys.argv[2])
            beginOperation(weight,title)
        else:
            print("Improper command entered!")
        


if __name__ == "__main__":
    main()



    
#tags:
#- archive # all posts
#- nature
#---







