#The image modifier functions


from tkinter import filedialog
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import load_model_3 as mn


def rotate_180():
    from PIL import Image
    path=root.filename
    
    colorImage  = Image.open(path)
    rotated     = colorImage.rotate(180)
    rotated.save("roatated_180.png")
    
    from tkinter import messagebox
    messagebox.showinfo("Output", "image is saved as rotated_180.png\n try again by selcting that file")
    
    root.destroy()
    window()
    
def rotate_270():
    from PIL import Image
    path=root.filename
    print(path)
    colorImage  = Image.open(path)
    rotated     = colorImage.rotate(270)
    rotated.save("roatated_270.png")
    
    from tkinter import messagebox
    messagebox.showinfo("Output", "image is saved as rotated_270.png\n try again by selcting that file")
    
    root.destroy()
    window()
def rotate_90():
    from PIL import Image
    path=root.filename
    colorImage  = Image.open(path)
    transposed  = colorImage.transpose(Image.ROTATE_90)
    transposed.save("rotated_90.png")
    from tkinter import messagebox
    messagebox.showinfo("Output", "image is saved as rotated_90.png\n try again by selcting that file")
    
    root.destroy()
    window()


#from tkinter import messagebox
def detection_function():
    path=root.filename
    RES=mn.main_function(path)
    res="The image is of "+str(RES)
    from tkinter import messagebox
    messagebox.showinfo("Output", res)
    root.destroy()
    window()
def create_window():
    window = tk.Toplevel(root) 
def refresh():
    root.destroy()
    window()
def refresh1(event):
    root.destroy()
    window()    
def client_exit():
        root.destroy()
        
def importImages2(event):
        from tkinter import messagebox
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("JEPG files","*.jpg"),("png files","*.png")))
        #print(root.filename)
        #image=Image.open(root.filename)
        try:
            image=Image.open(root.filename)
            #image.verify()
            image = image.resize((250, 250), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(image)
            panel = tk.Label(root, image = img)
            panel.image = img
            #panel.pack(side = "bottom", fill = "both", expand = "yes")
            panel.place(x=550, y=200, anchor="center")
            button2 = tk.Button(root,text="Check",bg = 'DeepSkyBlue3',command=detection_function,height =2 , width = 10)
            button2.config(font=("Helvetica", 11))
            button2.place(x=550, y=380,anchor="center")
            #button3.config(font=("Helvetica", 11))
            #photo = PhotoImage(file = r"right.png") 

            #photoimage = photo.subsample(4,4) 

            #Button(frame1, text = 'Click Me !', image = photoimage, compound = Right).pack(side = TOP)
            button4 = tk.Button(root,text="Rotate Left\nClockwise",bg = 'DeepSkyBlue3',command=rotate_270,height =2 , width = 15)
            button4.config(font=("Helvetica", 11))
            button4.place(x=450, y=470,anchor="center")
            button5= tk.Button(root,text="Rotate Right \n Counter Clockwise",bg="DeepSkyBlue3",command=rotate_90,height =2 , width = 15)
            button5.config(font=("Helvetica", 11))
            button5.place(x=650, y=470,anchor="center") 
#            button6= tk.Button(root,text="Rotate Right",bg="DeepSkyBlue3",command=refresh,height =2 , width = 10)
#            button6.config(font=("Helvetica", 11))
#            button6.place(x=650, y=470,anchor="center") 
        except OSError:
		    
            messagebox.showinfo("Error", "Not an image")
            refresh1()
        
        
def importImages():
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("JEPG files","*.jpg"),("png files","*.png")))
        #print(root.filename)
        #image=Image.open(root.filename)
        try:
            image=Image.open(root.filename)
            #image.verify()
            image = image.resize((250, 250), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(image)
            panel = tk.Label(root, image = img)
            panel.image = img
            #panel.pack(side = "bottom", fill = "both", expand = "yes")
            panel.place(x=550, y=200, anchor="center")
            button2 = tk.Button(root,text="Check",bg = 'DeepSkyBlue3',command=detection_function,height =2 , width = 10)
            button2.config(font=("Helvetica", 11))
            button2.place(x=550, y=400,anchor="center")
            #button3.config(font=("Helvetica", 11))
            button4 = tk.Button(root,text="Rotate Left",bg = 'DeepSkyBlue3',command=rotate_270,height =2 , width = 10)
            button4.config(font=("Helvetica", 11))
            button4.place(x=100, y=150,anchor="center")
            button5= tk.Button(root,text="Rotate Right",bg="DeepSkyBlue3",command=rotate_90,height =2 , width = 10)
            button5.config(font=("", 11))
            button5.place(x=100, y=220,anchor="center")   
        except OSError:
            messagebox.showinfo("Error", "Not an image")
            refresh1()
         

def about_function():
    """
    msg = tk.Message(root, text = "This software is developed by Fahim Abdullah \nand Mitu Akter \n under the supervition of Kazi Mahmudul Hasan Munna.")
    msg.config(bg='lightgreen', font=('times', 24, 'italic'))
    msg.place(x=400,y=400)
    print("bla bla bla")
    """
    messagebox.showinfo ("About","This software is developed by \nFahim Abdullah and Mitu Akter \nunder the supervition of Kazi Mahmudul Hasan Munna.")
    refresh()
        
def window():       
    global root
    root = tk.Tk()
    root.title("Detection")
    root.geometry("800x550")
    root.configure(background='gray40')
    ########---------------------Manu bar-------------------######################
    
    menu = Menu(root)
    root.config(menu=menu)
    
    
    ######################################################
    subMenu=Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="New Seasion..",command=refresh)
    subMenu.add_command(label="Open",command=importImages)
    subMenu.add_command(label="Exit",command=client_exit) 
    ##########################################################
    editMenu=Menu(menu)
    menu.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Refresh",command=refresh)
    #editMenu.add_command(label="Paste",command=detection_function)
    #editMenu.add_command(label="Undo",command=detection_function)
    #editMenu.add_command(label="Redo",command=detection_function)
    ############################################
    helpMenu=Menu(menu)
    menu.add_cascade(label="Help", menu=helpMenu)
    helpMenu.add_command(label="About",command=about_function)
    
    ############################################################################################################
    global topframe
    topframe =tk.Frame(root, bg="gray40",highlightbackground="black", highlightcolor="black", highlightthickness=2, width=250, height=550, bd= 0)
    topframe.pack(side=LEFT)
    global bottomframe
    bottomframe = tk.Frame(root,bg="gray", highlightbackground="black", highlightcolor="black", highlightthickness=2, width=550, height=550, bd= 0)
    bottomframe.pack(side=RIGHT)
    
    label1 = tk.Label(root,text="Select an image(.jpg/.png)",bg='Pale Turquoise2')
    label1.config(font=("Helvetica", 13))
    #label1.grid(row=0,column=0,padx=20,pady=20)
    label1.place(x=120, y=30, anchor="center")
    #
    
    #button1 = tk.Button(topframe,text="Import")
    #button1.bind("<Button-1>",importImages)
    #button1.pack()
    
    button = Button(root, text="Upload image", height =2, width = 12,bg="DeepSkyBlue3")
    #img = PhotoImage(file="E:/ml/1-Project/import_test.png") # make sure to add "/" not "\"
    button.config(font=("Helvetica", 11))
    button.bind("<Button-1>",importImages2)
    #button.pack() # Displaying the button
    #button.grid(row=1 ,column=0)
    button.place(x=100, y=90, anchor="center")
    
    button6= tk.Button(root,text="Refresh",bg="DeepSkyBlue3",height =2 , width = 10)
    button6.bind("<Button-1>",refresh)
    button6.config(font=("Helvetica", 11))
    button6.place(x=100, y=160,anchor="center") 

    label2 = tk.Label(root,text="Preview",bg='Pale Turquoise3')
    label2.config(font=("Helvetica", 17))
    #label2.grid(row = 0,column=10,padx=210,pady=10)
    label2.place(x=550, y=30, anchor="center")
    
    root.mainloop()
window()