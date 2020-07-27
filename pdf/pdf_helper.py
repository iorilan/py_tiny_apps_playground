from PyPDF2 import PdfFileReader

def read_all_text(file_name):
    res= []
    with open(file_name, 'rb') as pdf:
        reader = PdfFileReader(pdf)
        pages = reader.numPages
        for p in range(0, pages):
            pageObj = reader.getPage(p)
            res.append(pageObj.extractText())
    return res

def combine(pdf1, pdf2, output_pdf):
    pass

def water_mark(pdf, text):
    pass

def create(data):
    pass

def encrypt(pdf):
    pass

