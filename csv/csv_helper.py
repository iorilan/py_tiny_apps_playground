import csv
import os 
def csv_lines(file_name):
    f = open(file_name)
    reader = csv.reader(f)
    res = list(reader)
    f.close()
    return res

def save(grid, file_name):
    rows = len(grid)
    f = open(file_name,'w',newline='',encoding='utf8')
    writer = csv.writer(f)
    for r in grid:
        if r:
            writer.writerow(r)
    f.close()

def save2(grid, file_name):
    headers = grid[0]
    with open(file_name, 'w', newline='') as f:
        writer = csv.DictWriter(f,fieldnames=headers)
        writer.writeheader()

        for r in range(1,len(grid)):
            writer.writerow(grid[r])
        