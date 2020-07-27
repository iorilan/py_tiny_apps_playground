from excel_helper import excel_helper

def read_sheet1():
    helper = excel_helper()    
    data = helper.readSheet("sample.xlsx", "Sheet1")
    for row in data:
        print(row)

def read_all():
    helper = excel_helper()    
    data = helper.readAll("sample.xlsx")
    for k,v in data.items():
        print(f'============sheet:{k}===============')
        for row in v:
            print(row)
def create_new():
    helper = excel_helper()
    data = {
        'sheet1':[
                    ['name','age','id'],
                    ['aaaa',22,'S01'],
                    ['bbb',33,'S02']
                ],
        'sheet2':[
                    ['company','address','join_date'],
                    ['google','address1 993033','2020-01-01'],
                    ['facebook','address 229222','2020-09-02']
                ],
    }
    helper.write_excel_doc(data, 'write_sample.xlsx')

def create_new2():
    helper = excel_helper()
    helper.merge_with_sum_sample()

def create_chart():
    helper = excel_helper()
    helper.sample_bar_chart('Sample',
        [
            ['X','Y1','Y2'],
            [1,20,49],
            [2,25,29],
            [3,10,91],
            [4,80,23],
            [5,60,49],
            [8,40,19],
            [7,21,8],
        ]
    )

if __name__ == "__main__":
    #read_all()
    #create_new()
    # create_new2()
    create_chart()