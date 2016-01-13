import csv
import numpy as np

class ExcelFr(csv.excel):
    
    delimiter = ";"
 
csv.register_dialect('excel-fr', ExcelFr())
CheminVersData = 'C:\\Users\\Alexandre\\AppData\\Local\\AnotherPerspective_YoYo_Version4\\'
def writeToCSV(list):
    fic = open(CheminVersData + 'TASEditor.csv','w')
    with fic as f:
        writer = csv.writer(f, delimiter = ';')
        for i in range(len(list)):
            writer.writerow((str(i), list[i]))
    fic.close()
    return True

def writeToTASFiles(list):
    for i in range(len(list)):
        fic = open(CheminVersData + 'TAS_'+str(i)+'.tas','w')
        fic.write(list[i])
        fic.close()
    return True
    
    
def readCSV():
    listInputs = []
    list = []
    fic = open(CheminVersData + 'TASEditor.csv','r', newline='')
    reader = csv.reader(fic, 'excel-fr')
    for row in reader:
        if row != []:
            list.append(row)
    fic.close()
    dataN = np.array(list, dtype = str)
    for i in dataN[:,1]:
        if i != '':
            listInputs.append(i)
    return listInputs

def readTAS(rank):
    listInputs = []
    for i in range(rank+1):
        fic = open(CheminVersData + 'TAS_'+str(i)+'.tas','r')
        listInputs.append(fic.read())
        fic.close()
    return listInputs
    
def FromTASToExcel(rank):
    l = readTAS(rank)
    writeToCSV(l)

def FromExceltoTAS():
    l = readCSV()
    writeToTASFiles(l)
    
    