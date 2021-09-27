import tkinter as tk
from functools import partial
from winreg import *

key_val = r'SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\bc5038f7-23e0-4960-96da-33abaf5935ec'
key = OpenKey(HKEY_LOCAL_MACHINE, key_val, 0, KEY_ALL_ACCESS)

def tuple_to_string(tup):
    str = ''
    for item in tup:
        str = str + "{}".format(item)
    return str

def print_number(number):
    output_textbox.configure(state=tk.NORMAL)
    output_textbox.delete(0, tk.END)
    output_textbox.insert(0, str(number))
    output_textbox.configure(state=tk.DISABLED)

def read_reg():
    current = QueryValueEx(key, "ValueMax")
    (percent, type) = current
    text = str(percent) + "%"
    output_textbox.configure(state=tk.NORMAL)
    output_textbox.delete(0, tk.END)
    output_textbox.insert(0, text)
    output_textbox.configure(state=tk.DISABLED)

def write_reg(number):
    SetValueEx(key, "ValueMax", 0, REG_DWORD, number)
    read_reg()

okno = tk.Tk()
okno.title("Kalkulator")
okno.geometry("300x500")

okno.grid_rowconfigure(0, weight=1)
okno.grid_rowconfigure(1, weight=8) #dzielimy okno na wiersze, tyle wierszy ile zdefiniujemy i ich weight, na tyle jest dzielone okno
okno.grid_columnconfigure(0, weight=1)

output_frame = tk.Frame(okno, width=300, height=100, background='grey')
output_frame.grid(row=0, column=0, sticky=tk.NSEW) #ta czesc siatki znajduje sie w rzedzie 0, kolumnie 0 i "przykleja sie" do wszystkich naroznikow

button_frame = tk.Frame(okno, width=300, height=400, background='light blue')
button_frame.grid(row=1, column=0, sticky=tk.NSEW)

for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1) #tworzymy liste 4x1, gdzie kazdy przycisk zajmuje 1/4 miejsca, poniewaz zajmuje weight/liczbe wierszy
button_frame.grid_columnconfigure(0, weight=1)

output_textbox = tk.Entry(output_frame, font=("Arial", 25), state=tk.DISABLED, disabledbackground='white', background='white', fg='black') #tworzenie pola tekstowego, ktorego rodzicem jest output_frame
output_textbox.pack(fill=tk.BOTH, expand=True) #fill both wypelnia w osi X oraz Y, expand upewnia sie, ze bedzie sie skalowac ze skalowaniem okna

read_reg()

button_100 = tk.Button(button_frame, font=("Arial", 25), text="100%", bg='grey', fg='black')
button_100.configure(command=partial(write_reg, 100))
#button_100.configure(command=partial(read_reg))
button_100.grid(row=0, column=0, sticky=tk.NSEW)
button_70 = tk.Button(button_frame, font=("Arial", 25), text="70%", bg='grey', fg='black')
button_70.configure(command=partial(write_reg, 70))
#button_70.configure(command=partial(read_reg))
button_70.grid(row=1, column=0, sticky=tk.NSEW)
button_50 = tk.Button(button_frame, font=("Arial", 25), text="50%", bg='grey', fg='black')
button_50.configure(command=partial(write_reg, 50))
#button_50.configure(command=partial(read_reg))
button_50.grid(row=2, column=0, sticky=tk.NSEW)
button_30 = tk.Button(button_frame, font=("Arial", 25), text="30%", bg='grey', fg='black')
button_30.configure(command=partial(write_reg, 30))
#button_30.configure(command=partial(read_reg))
button_30.grid(row=3, column=0, sticky=tk.NSEW)

okno.mainloop()
#while True:
#    read_reg()
#    okno.update_idletasks()
#    okno.update()
