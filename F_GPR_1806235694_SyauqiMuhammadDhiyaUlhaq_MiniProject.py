#===Modul yang perlu diimport===#
from tkinter import *
import matplotlib.pyplot as plt
from tkinter import filedialog


x, y = [], []

class Plot:

    def __init__(self,master):
        self.master=master
        self.master.title("File-to-Graph Converter")
        self.master.minsize(200,100)

        self.judul = Label(self.master, text = "File-to-Graph Converter")
        self.judul.grid(row=0,column=1)
        self.label1 = Label(self.master, text = "Pilih File: ",anchor=E, justify=RIGHT)
        self.chooseFile = Button(self.master, text="Browse",command=self.choose_file)
        self.label1.grid(row=1,column=0,ipadx=25)
        self.chooseFile.grid(row=1,column=1,ipadx=20)
        self.txt=Label(self.master, text="*.txt",anchor=W, justify=LEFT)
        self.txt.grid(row=1,column=2,ipadx=25)

        self.keterangan = Label(self.master, text = "Ubah ke:")
        self.keterangan.grid(row=2, column=1)

        self.lineGraph = Button(self.master, text = "Line Graph",command=self.line_Graph)
        self.lineGraph.grid(row=3,column=0,ipadx=15)
        self.barGraph = Button(self.master, text = "Bar Graph",command=self.bar_Graph)
        self.barGraph.grid(row=3,column=1,ipadx=15)

        self.adaFile = Label(self.master, text="File belum ada")
        self.adaFile.grid(row=4,column=1)
        
    def choose_file(self):
        file_name = filedialog.askopenfilename()
        if not file_name:
            return
        for line in open(file_name, 'r'):
            values = [float(s) for s in line.split()]
            x.append(values[0])
            y.append(values[1])
            self.adaFile["text"]="File sudah tersedia!"

    def line_Graph(self):
        plt.figure(num='Line Graph | File-to-Graph Converter')
        plt.plot(x,y, marker="o")
        plt.xlabel("Tahun")
        plt.ylabel("Jumlah")
        plt.show()

    def bar_Graph(self):
        plt.figure(num='Bar Graph | File-to-Graph Converter')
        plt.bar(x,y)
        plt.xlabel("Tahun")
        plt.ylabel("Jumlah")
        plt.show()

        
def main():
    root_window = Tk()
    program = Plot(root_window)
    root_window.mainloop()
    

if __name__ == '__main__':
    main()
