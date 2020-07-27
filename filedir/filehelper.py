import os
import pickle
import shelve
import copy
import shutil
import send2trash
import zipfile
class filehelper:
    
    @staticmethod
    def files(path, tree=False, limit=500):
        count = 0
        if tree is True:
            res = []
            for folder,subFolderArr,fileArr in os.walk(path):
                #print(f'{folder},{fileArr}')
                for file in fileArr:
                    res.append(file)
                    count+=1

                if count == limit:
                    break
        else:
            res = []
            arr = os.listdir(path)
            for f in arr:
                if os.path.isfile(f):
                    res.append(f)
                    count += 1
                    if count == limit:
                        break
        return res

    @staticmethod
    def tree(path):
        res = []
        for folder ,subArr, fileArr in os.walk(path):
            obj = {"dir":folder, "files":[]}
            #print(f'<folder>{folder}')
            for f in fileArr:
                obj['files'].append(f)
                #print(f'<file>{f}')
            # for sub in subArr:
            #     print(f'<sub folder>{sub}')
            res.append(obj)
        return res

    @staticmethod
    def exist(path):
        return os.path.exists(path)

    @staticmethod
    def fileExist(path):
        return os.path.isfile(path)

    @staticmethod
    def folderExist(path):
        return os.path.isdir(path)

    @staticmethod
    def createFolder(path):
        os.makedirs(path)

    @staticmethod
    def getFolderFile(path):
        return os.path.split(path)

    @staticmethod
    def currentFolder():
        return os.getcwd()

    @staticmethod
    def sizeof(path):
        return os.path.getsize(path)

    @staticmethod
    def readText(path):
        f=open(path)
        txt=f.read()
        f.close()
        return txt
    
    @staticmethod
    def writeText(path,content):
        f=open(path,'w')
        f.write(content)
        f.close()

    @staticmethod
    def readPickle(path):
        f=open(path, 'rb')
        obj = pickle.load(f)
        f.close()
        return obj

    @staticmethod
    def writePickle(path, obj):
        f=open(path, 'wb')
        pickle.dump(obj, f)
        f.close()

    @staticmethod
    def readShelve(path,k):
        f = shelve.open(path)
        res = copy.deepcopy(f[k])
        f.close()
        return res

    @staticmethod
    def readShelveAll(path):
        f = shelve.open(path)
        return copy.deepcopy(f)

    @staticmethod
    def writeShelve(path, k,v):
        f = shelve.open(path)
        f[k]=v
        f.close()
    
    @staticmethod
    def deleteFile(path, hard=False):
        if hard == True:
            os.unlink(path)
        else:
            send2trash.send2trash(path)

    @staticmethod
    def deleteFolder(path, hard=False):
        if hard == True:
            os.rmdir(path)
        else:
            send2trash.send2trash(path)

    @staticmethod
    def cpFile(path1,path2):
        shutil.copy(path1,path2)

    def cpFolder(path1, path2):
        shutil.copytree(path1, path2)

    @staticmethod
    def mvFile(path1, path2):
        shutil.move(path1, path2)
    
    @staticmethod
    def renameFile(path1, newname):
        folder,file=os.path.split(path1)
        shutil.move(path1, os.path.join(folder, newname))



    @staticmethod
    def zipFolder(folder):
        zipname= folder.split(os.path.sep)[-1]+'.zip'
        zippath = os.path.join(folder,zipname)
        z = zipfile.ZipFile(zippath,'w')
        dirfiles = os.listdir(folder)
        os.chdir(folder)
        for f in dirfiles:
            if os.path.isfile(f) and f != zipname:
                print(f)
                filename = f
                z.write(filename,compress_type=zipfile.ZIP_DEFLATED)
        z.close()

    @staticmethod
    def unzip(path):
        file = zipfile.ZipFile(path)
        folder,f = os.path.split(path)
        #print(file)
        os.chdir(folder)
        file.extractall()
        file.close()

