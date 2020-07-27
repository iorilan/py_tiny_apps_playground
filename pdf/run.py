import pdf_helper as helper
import os


def sample_read_all():
    path1,path2 = os.path.join("sample_data","pdf1.pdf"),os.path.join("sample_data","pdf2.pdf")
    data=helper.read_all_text(path1)
    for d in data:
        print(d,end='\r\n=======page======\r\n')

def sample_combine():
    pdf1,pdf2 = os.path.join("sample_data","pdf1.pdf"),os.path.join("sample_data","pdf2.pdf")
    pdf3 = os.path.join("sample_data","pdf3.pdf")
    helper.combine(pdf1,pdf2,pdf3)

def sample_watermark():
    pdf1,watermark = os.path.join("sample_data","pdf1.pdf"), \
                        os.path.join("sample_data","water_mark_sample.pdf")
    output = os.path.join("sample_data","watermark_merged.pdf")
    helper.water_mark(pdf1,watermark, output)

def sample_encrypt():
    pdf1,pdf_encrypt=os.path.join("sample_data","pdf1.pdf"), \
                        os.path.join("sample_data","encrypt.pdf")
    helper.encrypt(pdf1, pdf_encrypt,"1234")

def create_sample():
    pages = []
    pages.append({'header':'Header1','body':'sample body 11111'})
    pages.append({'header':'Header2','body':'sample body 22222'})
    helper.create(pages, "Create_Sample.pdf")

if __name__ == "__main__":
    #sample_read_all()
    # sample_combine()
    #sample_watermark()
    #sample_encrypt()
    create_sample()
