import xlwt
import xlrd
from xlutils.copy import copy
from tkinter import *
root = Tk()
root.title("Marks Uploader")
root.geometry("500x500")
            
def OnReturn(*args):
    rn = int(entry_1.get())
    mar = int(entry_2.get())
    aas = int(entry_3.get())
    rnn = rn
    maar = mar
    workbook = xlrd.open_workbook("Marks.xls")
    sheet = workbook.sheet_by_index(0) 
    rb = xlrd.open_workbook("Marks.xls")
    
    wb = copy(rb)
    
    w_sheet = wb.get_sheet(0)
    
    for row in range(sheet.nrows): 
        row_value = sheet.row_values(row)
        if row_value[0] == rn:
            w_sheet.write(row,1,mar)
            w_sheet.write(row,2,aas)
            print (row_value)
            entry_2.delete(0,'end')
            entry_3.delete(0,'end')
            wb.save("Marks.xls")
      
label_1 = Label(root, text = "Enter Reg No here").place(relx = 0.3,rely = 0.05,anchor = E)
entry_1 = Entry(root)
entry_1.place(relx = 0.6,rely = 0.05,anchor = E)
entry_1.insert(1,2016)
entry_1.bind("<Return>", OnReturn)

label_2 = Label(root, text = "Quiz Marks").place(relx = 0.3,rely = 0.1,anchor = E)

entry_2 = Entry(root)
entry_2.bind("<Return>", OnReturn)
entry_2.place(relx = 0.6,rely = 0.1,anchor = E)

entry_3 = Entry(root)
entry_3.place(relx = 0.6, rely = 0.15, anchor = E)
entry_3.bind("<Return>", OnReturn)

label_2 = Label(root, text = "Assignment Marks").place(relx = 0.3,rely = 0.15,anchor = E)


root.mainloop()
