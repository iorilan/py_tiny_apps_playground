import csv_helper as ch
import os
import datetime

def sample_read(name):
    file = os.path.join("sample_data",name)
    res= ch.csv_lines(file)
    for line in res:
        if line:
            print(line)

def sample_write():
    data = [
        ["Name","Id","CreatedAt"]
    ]
    for i in range(0,20):
        data.append([f"Jeo{i}",f'S_{i+1}',datetime.datetime.now()])
    #print(data)
    file = os.path.join("sample_data","1.csv")
    ch.save(data, file)

def sample_write2():
    data = [
        ["Name","Id","CreatedAt"]
    ]
    for i in range(0,20):
        data.append({'Name':f"Jeo{i}",'Id':f'S_{i+1}','CreatedAt':datetime.datetime.now()})

    #print(data)
    file = os.path.join("sample_data","2.csv")
    ch.save2(data, file)

if __name__ == "__main__":
    # sample_write()
    # print(sample_read("1.csv"))

    sample_write2()
    print(sample_read("2.csv"))
    