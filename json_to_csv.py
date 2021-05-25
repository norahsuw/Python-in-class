import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

def getJSON ():
    global read_file
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_json (import_file_path)

def convertToCSV ():
    global read_file
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    read_file.to_csv (export_file_path, index = None, header=True)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()

read_file=pd.DataFrame()
root= tk.Tk()
canvasl = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief ='raised')
canvasl.pack()

labell =tk.Label(root, text='File Conversion Tool', bg = 'lightsteelblue2')
labell.config(font=('helvetica', 20))
canvasl.create_window(150, 60, window=labell)

browseButton_JSON = tk.Button(text="        Import JSON File ", command=getJSON, bg='green', fg='white', font=('helvetica',12,'bold'))
canvasl.create_window(150, 130, window=browseButton_JSON)

saveAsButton_CSV = tk.Button(text='Convert JSON to CSV', command=convertToCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvasl.create_window(150, 180, window=saveAsButton_CSV)

exitButton = tk.Button (root, text='    Exit Application     ',command=exitApplication, bg='brown', fg='white',font=('helvetica',12, 'bold'))
canvasl.create_window(150, 230, window=exitButton)

root.mainloop()