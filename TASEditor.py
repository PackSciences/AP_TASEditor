from tkinter import *
import csv
import numpy as np

CheminVersDataDefault = 'C:\\Users\\Alexandre\\AppData\\Local\\AnotherPerspective_YoYo\\'

class ExcelFr(csv.excel):
    
    delimiter = ";"
 
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
    
def FromTASToExcel(rank = 100000):
    l = readTAS(rank)
    writeToCSV(l)
    print('Now exporting from TAS to Excel until frame number ' + str(rank))

def FromTTE():
    global ranking
    FromTASToExcel(ranking)
    
def FromExceltoTAS():
    l = readCSV()
    writeToTASFiles(l)
    print("Now exporting from Excel to TAS")

def SetPath():
    if Chemin_Tk.get() != '':
        CheminVersData = Chemin_Tk.get()
        print(CheminVersData + ' has been set as path')
    else:
        CheminVersData = CheminVersDataDefault
        print(CheminVersData + ' has been set as path')

def SetLimit():
    global ranking
    if Limite_TK.get() != '':
        ranking = int(float(Limite_TK.get()))
        print(str(ranking) + ' has been set as limit')
    else:
        print(str(ranking) + ' has been set as limit')
    
Wn = Tk()
ranking = 100000

CheminVersData = CheminVersDataDefault
csv.register_dialect('excel-fr', ExcelFr())

cadre_title = Frame(Wn, width = 768, height = 576, borderwidth = 3)
cadre_title.pack(fill = BOTH)
cadre_path = Frame(Wn, width = 768, height = 576, borderwidth = 3)
cadre_path.pack(fill = BOTH)
cadre_buttons = Frame(Wn, width = 768, height = 576, borderwidth = 3)
cadre_buttons.pack(fill = BOTH)

champ_label = Label(cadre_title, text= 'Another Perspective TAS Editor by PackSciences')
champ_label.pack(fill = BOTH)
Chemin_Tk = StringVar()
champ_path = Label(cadre_path, text= 'Choose your path to Another Perspective AppData folder')
champ_path.pack(fill = BOTH)
champ_info = Label(cadre_path, text= 'If none specified, it will be the default one')
champ_info.pack(fill = BOTH)
chaine_path = Entry(cadre_path, textvariable = Chemin_Tk, width = 150)
chaine_path.pack()
button_path = Button(cadre_path, command = SetPath, text = 'Set path')
button_path.pack()
#
Limite_TK = StringVar()
champ_lim = Label(cadre_path, text= 'Choose your range')
champ_lim.pack(fill = BOTH)
chaine_lim = Entry(cadre_path, textvariable = Limite_TK, width = 7)
chaine_lim.pack()
button_lim = Button(cadre_path, command = SetLimit, text = 'Set limit')
button_lim.pack()

#
button_expexcl = Button(cadre_buttons, command = FromExceltoTAS, text = 'Export from Excel to TAS files')
button_expexcl.pack()
button_exptas = Button(cadre_buttons, command = FromTASToExcel, text = 'Export from TAS to Excel files')
button_exptas.pack()

button_exit = Button(cadre_buttons, command = Wn.quit, text = 'Exit')
button_exit.pack()
Wn.mainloop()
Wn.destroy()
