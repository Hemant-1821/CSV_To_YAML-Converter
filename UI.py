import tkinter 
from tkinter import messagebox
from tkinter import filedialog
import yaml
import os
import csv
import codecs
import sys

root = os.getcwd()

def csvToYaml(csvFile, output):
    stream = open(output, 'w',encoding="utf-8")
    csvOpen = csv.reader(codecs.iterdecode(csvFile, 'utf-8'))
    keys = next(csvOpen)
    for row in csvOpen:
        yaml.dump([dict(zip(keys, row))], stream, default_flow_style=False)

def singleCSV(csvFile, output=None):
    output = output if output else root+'/'+(csvFile.split('/')[-1].replace('.csv','.yml'))
    with open(csvFile, 'rb') as csvFile:
        csvToYaml(csvFile, output)


main_win = tkinter.Tk()
main_win.geometry("1000x500")
main_win.sourceFileInput = ''
main_win.sourceFolder = ''


tkinter.Label(main_win, text="Enter output file(with extension .yml)").grid(row=0)
e1 = tkinter.Entry(main_win)
e1.grid(row=0, column=1)


def chooseFileInput():
    main_win.sourceFileInput = filedialog.askopenfilename(parent=main_win, initialdir= "/", title='Please select a directory')
    csvFile = main_win.sourceFileInput
    output1 = main_win.sourceFolder
    output = output1+ "/" + e1.get()
    print(output)
    print(csvFile)
    convert(csvFile,output)
    print("file converted")

b_chooseFile = tkinter.Button(main_win, text = "Choose Input File", width = 20, height = 3, command = chooseFileInput)
b_chooseFile.place(x = 250,y = 50)
b_chooseFile.width = 100

#output = " "

def chooseDir():
    main_win.sourceFolder =  filedialog.askdirectory(parent=main_win, initialdir= "/", title='Please select a directory')
    
    

b_chooseDir = tkinter.Button(main_win, text = "Choose output Folder", width = 20, height = 3, command = chooseDir)
b_chooseDir.place(x = 50,y = 50)
b_chooseDir.width = 100


def convert(csvFile,output):
    singleCSV(csvFile,output)

#button = tkinter.Button(main_win, text='convert', width=20,height = 3, command=convert)
#button.place(x = 500,y = 50)
#button.width = 100

main_win.mainloop()



