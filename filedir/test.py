from filehelper import filehelper
import os
if __name__ == "__main__":
    p = filehelper.currentFolder()
    
    #print (f'current folder : ==> {p}')

    # print(filehelper.files(p))
    # print(filehelper.tree(p))
    # print(filehelper.files(p, True))

    # print(filehelper.exist('C:\\Windows')) #True
    # print(filehelper.exist('D:\\Projects')) #True
    # print(filehelper.exist('D:\\Project')) # False
    # print(filehelper.exist(r'D:\RoboMongo\robo3t.exe')) #True
    # print(filehelper.exist(r'D:\RoboMongo\robo3t11.exe')) #False


    #filehelper.createFolder(os.path.join(p, "sub2"))

    #print (filehelper.sizeof(r'D:\RoboMongo\robo3t.exe'))

    #-- read/write plain text
    # abctxt = os.path.join(p,"sub","abc.txt")
    # filehelper.writeText(abctxt,"aaaaabb")
    # print(filehelper.readText(abctxt))
    # filehelper.writeText(abctxt,"aaaaabbbbccc")
    # print(filehelper.readText(abctxt))

    #-- read/write plain pickle
    # abcpkl = os.path.join(p,"sub","abcpkl")
    # tree = filehelper.tree(p)
    # filehelper.writePickle(abcpkl, tree)
    # print(filehelper.readPickle(abcpkl))

    #-- read/write plain shelve
    #abcshv = os.path.join(p,"sub","abcshv")
    #tree = filehelper.tree(p)
    #filehelper.writeShelve(abcshv,'dir_tree',tree)
    #print(filehelper.readShelve(abcshv,'dir_tree'))
    # shlvall = filehelper.readShelveAll(abcshv)
    # for k,v in shlvall.items():
    #     print(f'<shelve> key :{k} value :{v}')

    

    # --soft delete
    # abcpkl = os.path.join(p,"sub","abcpkl")
    # filehelper.deleteFile(abcpkl)
    # filehelper.deleteFolder(os.path.join(p,"sub3"))
    # filehelper.deleteFolder(os.path.join(p,"sub2"))

    # --hard delete very dangerous
    # filehelper.deleteFile(os.path.join(p,"sub2","test1.txt"), True)
    # filehelper.deleteFolder(os.path.join(p,"sub2"), True)
    #very dangerous

    #-- copy file
    # abcpkl = os.path.join(p,"sub","abcpkl")
    # filehelper.cpFile(abcpkl, os.path.join(p,"sub2"))

    #-- copy folder
    #filehelper.cpFolder(os.path.join(p,"sub"), os.path.join(p, "sub3"))

    #--mv
    # filehelper.mvFile(os.path.join(p,"sub2","sub.zip"), \
    #     os.path.join(p,"sub3")
    # )

    #-- rename
    # abcpkl2 = os.path.join(p,"sub2","abcpkl")
    # filehelper.renameFile(abcpkl2, "abcpkl2")


    #-- zip
    # filehelper.zipFolder(os.path.join(p,"sub"))

    #-- unzip
    #filehelper.unzip(os.path.join(p,"sub3","sub.zip"))