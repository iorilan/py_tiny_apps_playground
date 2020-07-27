from PyPDF2 import PdfFileReader,PdfFileWriter
from fpdf import FPDF

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
    pdf_writer = PdfFileWriter()
    reader1 = PdfFileReader(pdf1)
    for p in range(reader1.getNumPages()):
        pdf_writer.addPage(reader1.getPage(p))
    reader2 = PdfFileReader(pdf2)
    for p in range(reader2.getNumPages()):
        pdf_writer.addPage(reader2.getPage(p))
    with open (output_pdf, 'wb') as output:
        pdf_writer.write(output)


def water_mark(pdf, watermark_pdf, output):
    watermark_obj = PdfFileReader(watermark_pdf)
    watermark_page = watermark_obj.getPage(0)

    reader = PdfFileReader(pdf)
    writer = PdfFileWriter()
    for p in range(reader.getNumPages()):
        page = reader.getPage(p)
        page.mergePage(watermark_page)
        writer.addPage(page)
    with open(output, 'wb') as output_file:
        writer.write(output_file)


def encrypt(pdf_input,pdf_output,pwd):
    writer = PdfFileWriter()
    reader = PdfFileReader(pdf_input)

    for p in range(reader.getNumPages()):
        writer.addPage(reader.getPage(p))
    writer.encrypt(user_pwd=pwd, owner_pwd=None, use_128bit=True)

    with open(pdf_output, 'wb') as file:
        writer.write(file)
    


"""
    more details :
    https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html
"""
class PDF(FPDF):
    def header(self):
        txt='Title'
        self.set_font("Arial","B",20)
        width = self.get_string_width(txt)+5
        self.set_x((210-width)/2)
        self.set_draw_color(0,50,50)
        self.set_text_color(120,50,100)
        self.set_fill_color(100,0,0)

        self.set_line_width(1)
        self.cell(width,9,txt, 1,1, 'C',1)
        self.ln(10)

    def new_page(self,title,body):
        self.add_page()

        self.set_font("Arial",'',15)
        self.set_fill_color(150,100,200)
        self.cell(0,6, title,0,1,'L',1)
        self.ln(4)

        self.set_font("Times",'',12)
        self.multi_cell(0, 5, body)
        self.ln()
        self.set_font('','I')
        self.cell(0, 5, '(end of text)')
        

    def footer(self):
        txt='footer'
        self.set_y(-15)
        self.set_font("Arial",'I',8)
        self.set_text_color(128)
        self.cell(0,10,txt,0,0,'C')

def create(pages, output):
    pdf = PDF()
    for p in pages:
        pdf.new_page(p['header'], p['body'])
    pdf.output(output,'F')
    
