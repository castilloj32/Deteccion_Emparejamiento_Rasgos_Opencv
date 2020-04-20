import tkinter as tk

def input_box(x):

    root= tk.Tk()
    
    canvas1 = tk.Canvas(root, width = 400, height = 150)
    canvas1.pack()
    
    label2 = tk.Label(root, text= "Elige una norma para medir la distancia:")
    canvas1.create_window(200, 30, window=label2)
    
    
    def norma_l1 ():  
        
        label1 = tk.Label(root,text="Eligio Norma 1")
        canvas1.create_window(200, 70, window=label1)
        x=1
        return x
    def norma_l2 ():  
        label1 = tk.Label(root,text="Eligio Norma 2")
        canvas1.create_window(200, 70, window=label1)
        x=2
        return x
    button1 = tk.Button(text='Norm_L1', command=norma_l1)
    canvas1.create_window(100, 120, window=button1)
    
    button2 = tk.Button(text='Norm_L2', command=norma_l2)
    canvas1.create_window(300, 120, window=button2)
    
    root.mainloop()
    