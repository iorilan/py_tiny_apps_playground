import pdf_helper as helper
import os

if __name__ == "__main__":
    path1,path2 = os.path.join("sample_data","pdf1.pdf"),os.path.join("sample_data","pdf2.pdf")
    data=helper.read_all_text(path1)
    for d in data:
        print(d,end='\r\n=======page======\r\n')

    