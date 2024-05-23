from tkinter import *	 
import tkinter.messagebox as messagebox
from tkinter import ttk 

class TopUpStore:
    def __init__(self, window):
        self.window = window
        self.strnama = StringVar() 
        self.radio = IntVar() 
        self.strhobby = StringVar(value='Pilih di sini')  
        self.strmetode = StringVar(value='Pilih di sini')  

    def on_click(self): 
        pilihan = self.radio.get()
        nominal = self.strhobby.get()
        metode_bayar = self.strmetode.get()
        uid = self.strnama.get()
        if pilihan == 1:
            pilihan = "Genesis Cristal"
        elif pilihan == 2:
            pilihan = "Primogem"
        pesan = f"UID: {uid}\nPilihan: {pilihan}\nNominal: {nominal}\nMetode Bayar: {metode_bayar}"
        print(messagebox.askquestion("Top UP Store", pesan)) 

    def run(self):
        self.window.geometry("320x220") 
        self.window.title("TOP UP STORE") 
        self.window.resizable(width = 0, height = 0) 

        menu = Menu(self.window) 
        itemfile = Menu(menu, tearoff=0) 
        itemhelp = Menu(menu, tearoff=0) 
        itemfile.add_command(label='New') 
        itemfile.add_command(label='Save') 
        itemfile.add_command(label='Open') 
        itemhelp.add_command(label = 'About') 
        menu.add_cascade(label='File', menu=itemfile) 
        menu.add_cascade(label='Edit') 
        menu.add_cascade(label='View') 
        menu.add_cascade(label='Help', menu=itemhelp) 
        self.window.config(menu=menu) 

        buttonsubmit = Button(self.window,  
                    text = "Submit",  
                    command = self.on_click, 
                    font = ("Times New Roman", 13), 
                    fg = "black", 
                    state = ACTIVE  
                    ).place(x = 125, y = 170) 

        labelnama = Label(self.window, 
                      text = "UID\t:", 
                      font = ("times new roman", 10)).place(x=30, y=20) 
        labeljk = Label(self.window, 
                    text = "Pilihan\t:", 
                    font = ("times new roman", 10)).place(x=30, y=50) 
        labelhobby = Label(self.window, 
                       text = "Nominal\t:", 
                       font = ("times new roman", 10)).place(x=30, y=120) 
        labelmetode = Label(self.window, 
                       text = "Metode Bayar\t:", 
                       font = ("times new roman", 10)).place(x=30, y=150) 

        entrynama = Entry(self.window, 
                      textvariable = self.strnama, 
                      font = ("times new roman", 10)).place(x=100, y=20) 

        R1 = Radiobutton(self.window, 
                     text = "Genesis Cristal", 
                     font = ("times new roman", 10), 
                     variable = self.radio, 
                     value = 1).place(x = 100, y = 50) 
        R2 = Radiobutton(self.window, 
                     text = "Primogem", 
                     font = ("times new roman", 10), 
                     variable = self.radio, 
                     value = 2).place(x = 100, y = 70) 

        combobox1 = ttk.Combobox(self.window,  
                       width = 17, 
                       font = ("times new roman", 10),  
                       textvariable = self.strhobby,  
                       state ="readonly") 
        combobox1.place(x=100, y=117) 
        combobox1['values'] = ('60 = Rp. 11.773','1090 = Rp. 180,942','2240 = Rp. 392.402') 

        combobox2 = ttk.Combobox(self.window,  
                       width = 17, 
                       font = ("times new roman", 10),  
                       textvariable = self.strmetode,  
                       state ="readonly") 
        combobox2.place(x=100, y=147) 
        combobox2['values'] = ('Transfer Bank', 'OVO', 'DANA', 'GoPay') 

        self.window.mainloop() 

window = Tk() 
app = TopUpStore(window)
app.run()
