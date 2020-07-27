import word_helper as wh
import os
def sample_read():
    file1,file2 = os.path.join("sample_data","1.docx"),\
        os.path.join("sample_data","2.docx")
    #wh.read_all(file1)
    wh.read_all(file2)

def sample_write():
    pages = [
        {
            'headings':[('Header 0',0),('Header 1',1),('Header3',2)], 'paragraph':
            [
                {
                    'txt':'Paragraph1 scentence some description here ',
                    'runs':['Run1','this is a 2nd test run']
                }
            ]
        },
        {
            'headings':[('Header 3',3),('Header 4',4),('Header5',5)], 'paragraph':
            [
                {
                    'txt':'Paragraph1 scentence some description here ',
                    'runs':['Run1','this is a 2nd test run','some more runs']
                },
                {
                    'txt':'Paragraph2 scentence some description here ',
                    'runs':['Run2','this is a 2nd test run','some more runs']
                },
            ]
        },
    ]
    wh.create_new(pages, os.path.join('sample_data',"new_created.docx"))
if __name__ == "__main__":
    #sample_read()
    sample_write()

    