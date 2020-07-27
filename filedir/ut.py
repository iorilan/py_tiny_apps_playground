import unittest
from filehelper import filehelper 
import os
class UT(unittest.TestCase):
    def test1(self):
        self.reset()

        p = filehelper.currentFolder()
        self.assertTrue(len(p) > 0)
        self.assertTrue(len(filehelper.files(p)) == 3)
        self.assertTrue(len(filehelper.files(p, True)) ==10)

    def test2(self):
        self.reset()

        p = filehelper.currentFolder()
        curDir = filehelper.tree(p)
        #print(curDir)
        self.assertTrue(len(curDir[0]['files']) ==3)
        self.assertTrue(len(curDir[1]['files']) ==6)
        self.assertTrue(len(curDir[2]['files']) ==1)

    def test3(self):
        self.reset()

        self.assertTrue(filehelper.exist('C:\\Windows') and \
                        filehelper.folderExist('C:\\Windows')) 
        self.assertFalse(filehelper.exist('D:\\Project'))
        self.assertFalse(filehelper.folderExist('D:\\Project'))

        self.assertTrue(filehelper.exist(r'D:\RoboMongo\robo3t.exe') and \
                        filehelper.fileExist(r'D:\RoboMongo\robo3t.exe')) 
        self.assertFalse(filehelper.exist(r'D:\RoboMongo\robo3t11.exe'))
        self.assertFalse(filehelper.fileExist(r'D:\RoboMongo\robo3t11.exe'))
    
    def testDel(self):
        self.reset()

        d = os.path.join(filehelper.currentFolder(),"sub2")
        filehelper.createFolder(d)
        self.assertTrue(filehelper.folderExist(d))

        filehelper.deleteFolder(d,True) #hard
        self.assertFalse(filehelper.folderExist(d))

        filehelper.createFolder(d)
        self.assertTrue(filehelper.folderExist(d))
        filehelper.deleteFolder(d) #soft
        self.assertFalse(filehelper.folderExist(d))

    def testRw1(self):
        self.reset()

        d = os.path.join(filehelper.currentFolder(),"sub2")
        filehelper.createFolder(d)
        self.assertTrue(filehelper.folderExist(d))

        abctxt = os.path.join(d,"abc.txt")
        s="aaaaabb"
        filehelper.writeText(abctxt,s)
        self.assertTrue(filehelper.fileExist(abctxt))
        self.assertTrue(filehelper.readText(abctxt) == s)

        abcpkl = os.path.join(d,"abcpkl")
        tree = filehelper.tree(d)
        filehelper.writePickle(abcpkl, tree)
        self.assertTrue(filehelper.fileExist(abcpkl))
        self.assertTrue(filehelper.readPickle(abcpkl) == tree)

        abcshv = os.path.join(d, "abcshv")
        filehelper.writeShelve(abcshv,'dir_tree',tree)
        self.assertTrue(filehelper.fileExist(os.path.join(d, "abcshv.dat")))
        self.assertTrue(filehelper.fileExist(os.path.join(d, "abcshv.dir")))
        self.assertTrue(filehelper.fileExist(os.path.join(d, "abcshv.bak")))

        self.assertTrue(filehelper.readShelve(abcshv,'dir_tree') == tree)
        shlvall = filehelper.readShelveAll(abcshv)
        self.assertTrue(shlvall['dir_tree'] == tree)
        # for k,v in shlvall.items():
        #     print(f'<shelve> key :{k} value :{v}')

        filehelper.deleteFolder(d)
        self.assertFalse(filehelper.folderExist(d))
    
    def reset(self):
        d = os.path.join(filehelper.currentFolder(),"sub2")
        filehelper.deleteFolder(d)
        self.assertFalse(filehelper.folderExist(d))

if __name__ == "__main__":
    unittest.main()
        