#################################################################
####              Calculadora de Hipotenusa                 ####
#################################################################
from tkinter import *
import math

def show_answer():
    a = num1.get()
    b= num2.get()
    x = math.pow(int(a), 2) + math.pow(int(b), 2)
    y = math.sqrt(x)
    label_result.config(text=" %.0f" % y)
    return

root = Tk()  
root.title("Calculate Hypotenuse")
root.geometry('400x300')
root.configure(bg='White')
Label( text="Length of side A").grid(row=0,pady=(25,25), padx=(45, 0))
Label( text="Length of side B").grid(row=1, pady=(25,25), padx=(45, 0))
Label( text="Length of Hypotenusa").grid(row=4, pady=(25,25), padx=(45, 0))



num1= Entry(root) 
num2= Entry(root)

label_result = Label(root)
label_result.grid(row=4, column=1, pady=(25, 25), padx=(45, 0))
 
num1.grid(row=0, column=1, pady=(25, 25), padx=(45, 0))
num2.grid(row=1, column=1, pady=(25, 25), padx=(45, 0))
Button(root,text="Calculate Hypotenusa", command=show_answer).grid(row=3,column=1)

mainloop()






#################################################################
####                Calculadora de Areas                     ####
#################################################################
from tkinter import *
import math

def Area_Rectangle():
    var1 = num1.get()
    var2= num2.get()
    x1 =  float(var1) * float(var2)
    label_Rectangule.config(text=" %.0f" % x1)
    return

def Area_Parallelogram():
    var3=num1.get()
    var4=num2.get()
    x2 =  float(var3) * float(var4)
    label_Parallelogram.config(text=" %.0f" % x2)
    return

def Area_Triangle():
    var5=num1.get()
    var6=num2.get()
    x3 = float (var5) * float (var6) / 2
    label_Triangle.config(text=" %.0f" % x3)
    return

def Area_Cube():
    var7=num1.get()
    var8=num2.get()
    x4 = float (var7) * float (var8) * 6
    label_Cube.config(text=" %.0f" % x4)
    return

def Area_Pyramid():
    var9 = num1.get()
    var10 = num2.get()
    x5 = ((2 * float(var9) * float(var10)) + math.pow(float(var9), 2))
    label_Pyramid.config(text=" %2d" % x5)
    return



root = Tk()  
root.title("Calculate Hypotenuse")
root.geometry('500x400')
root.configure(bg='White')
Label( text="Base").grid(row=0,column=1,pady=(25,25), padx=(45, 0))
Label( text="Altura").grid(row=1,column=1, pady=(25,25), padx=(45, 0))
Label( text="Enter the base and heigth").grid(row=0,column=0, pady=(25,25), padx=(45, 0))


num1= Entry(root) 
num2= Entry(root)
num1.grid(row=0, column=3, pady=(25, 25), padx=(45, 0))
num2.grid(row=1, column=3, pady=(25, 25), padx=(45, 0))

label_Rectangule = Label(root)
label_Parallelogram=Label(root)
label_Triangle=Label(root)
label_Cube=Label(root)
label_Pyramid=Label(root)

label_Rectangule.grid(row=3,column=3,pady=(20,10), padx=(45, 0))
label_Parallelogram.grid(row=4,column=3,pady=(20,10), padx=(45, 0))
label_Triangle.grid(row=5,column=3,pady=(20,10), padx=(45, 0))
label_Cube.grid(row=6,column=3,pady=(20,10), padx=(45, 0))
label_Pyramid.grid(row=7,column=3,pady=(20,10), padx=(45, 0))

Button(root,text="  Rectangulo ",command= Area_Rectangle).grid(row=3,column=0,pady=(20,10), padx=(45, 0))
Button(root,text="Parallelogram",command= Area_Parallelogram).grid(row=4,column=0,pady=(0,0), padx=(45, 0))
Button(root,text="  Triangle   ",command=Area_Triangle).grid(row=5,column=0,pady=(10,10), padx=(45, 0))
Button(root,text="    Cube     ",command= Area_Cube).grid(row=6,column=0,pady=(10,10), padx=(45, 0))
Button(root,text="   Pyramid   ",command= Area_Pyramid).grid(row=7,column=0,pady=(10,10), padx=(45, 0))
root.mainloop()


#################################################################
####                  Addition Program                      ####
#################################################################

from tkinter import *
import math

def Area_Suma():
    var1 = num1.get()
    var2= num2.get()
    x1 =  float(var1) + float(var2)
    label_Suma.config(text=" %.1f" % x1)
    return


root = Tk()  
root.title("Addition Program")
root.geometry('320x400')
root.configure(bg='#D2F5E4')
Label( text="Enter first number").grid(row=0,column=1,pady=(25,25), padx=(45, 0))
Label( text="Enter second number").grid(row=2,column=1,pady=(25,25), padx=(45, 0))
Label( text="Sum").grid(row=5,column=0,pady=(25,25), padx=(45, 0))


num1= Entry(root) 
num2= Entry(root)
num1.grid(row=1, column=1, pady=(25, 25), padx=(45, 0))
num2.grid(row=3, column=1, pady=(25, 25), padx=(45, 0))

label_Suma = Label(root)

label_Suma.grid(row=5,column=1,pady=(20,10), padx=(45, 0))


Button(root,text="  Add ",command= Area_Suma).grid(row=4,column=1,pady=(20,10), padx=(45, 0))

root.mainloop()


#################################################################
####                Button Color Options                     ####
#################################################################


from tkinter import *



def verde():
    root.config(bg='#22FC00')
    Label(root, text="Hello World ", bg="light green", font=("Helvetica", 16, "bold")).grid(row=0, pady=(15, 15), padx=(35, 0))
    return

def Amarillo():
    root.config(bg='yellow')
    Label(root, text="Hello World ", bg="light yellow", font=("Helvetica", 16, "bold")).grid(row=0, pady=(15, 15), padx=(35, 0))
    return

def Rojo():
    root.config(bg='#B81010')
    Label(root, text="Hello World ", bg="#F05D68", font=("italik", 16, "bold")).grid(row=0, pady=(15, 15), padx=(35, 0))
    return

def Azul():
    root.config(bg='blue')
    Label(root, text="Hello World ", bg="#35CAE5", font=("", 16, "bold")).grid(row=0, pady=(15, 15), padx=(35, 0))
    return
    
root = Tk()
root.geometry('225x250')
root.config(bg="white")
root.title('Button Color Options')
    
Label(root, text="Hello World ", bg="white", font=("italik", 16)).grid(row=0, pady=(15, 15), padx=(35, 0))
Button(root, text=' Click for message in Green' , command=verde, borderwidth=5).grid(row=1, column=0, pady=(5, 5), padx=(35, 0))
Button(root, text=' Click for message in Yellow', command=Amarillo, borderwidth=5).grid(row=2, column=0, pady=(5, 5), padx=(35, 0))
Button(root, text='  Click for message in Red'  , command=Rojo, borderwidth=5).grid(row=3, column=0, pady=(5, 5), padx=(35, 0))
Button(root, text='  Click for message in Blue' , command=Azul, borderwidth=5).grid(row=4, column=0, pady=(5, 5), padx=(35, 0))

root.mainloop()


############################################################
####             Runners Calculator                    ####
###########################################################

from tkinter import *
import math


def Hola():
    var1 = num1.get()
    var2= num2.get()
    x1 = float(var2) / float(var1)
    label_Rectangule.config(text=" %.3f" % x1)
    return

    
    
root = Tk()  
root.title("Runner Calculator")
root.geometry('400x400')
root.configure(bg='#F1AB0A')
Label( text="Millas corridas",bg="#F9D175").grid(row=0,column=1,pady=(25,25), padx=(45, 0))
Label( text="Tiempo utilizado",bg="#F9D175").grid(row=2,column=1,pady=(25,25), padx=(45, 0))
Label( text="Velocidad",bg="#F9D175").grid(row=5,column=0,pady=(25,25), padx=(45, 0))


num1= Entry(root,bg="#F9D175") 
num2= Entry(root,bg="#F9D175")
num1.grid(row=1, column=1, pady=(25, 25), padx=(45, 0))
num2.grid(row=3, column=1, pady=(25, 25), padx=(45, 0))

label_Rectangule = Label(root,bg="#F9D175")
label_Rectangule.grid(row=5,column=1,pady=(20,10), padx=(45, 0))


Button(root,text="Calcular",command= Hola,bg="#F9D175").grid(row=4,column=1,pady=(20,10), padx=(45, 0))

root.mainloop()


####################################################
######           Grade Percentages             ####
####################################################

from tkinter import *
import math


def show_answer():
    var1 = num1.get()
    var2 = num2.get()
    var3 = num3.get()
    var4 = num4.get()
    grade = float(var1) + float(var2) + float(var3)
    per = float(grade) + float(var4)
    ans1 = float(per/550) * 100
    label_result.config(bg="#AF12F9",text="Total Percentage: %.2f" % ans1)
    return


root = Tk()
root.geometry('350x225')
root.resizable(False, False)
root.config(bg="#AF12F9")
root.title('Grade Percentages')
Label(root, text="Primer examen: ", bg="#AF12F9").grid(row=0, column=0, pady=(25, 0), padx=(25, 25))
Label(root, text="Segundo examen: ", bg="#AF12F9").grid(row=0, column=1, pady=(25, 0), sticky=W)
Label(root, text="Tercer examen: ", bg="#AF12F9").grid(row=1, column=0, pady=(30, 0), padx=(25, 25))
Label(root, text="Puntos: ", bg="#AF12F9").grid(row=1, column=1, pady=(30, 0), padx=(0, 0), sticky=W)

num1 = Entry(root)
num2 = Entry(root)
num3 = Entry(root)
num4 = Entry(root)

label_result = Label(root, bg="#AF12F9")

num1.grid(row=1, column=0, pady=(5, 25), padx=(30, 30))
num2.grid(row=1, column=1, pady=(5, 25), padx=(0, 10))
num3.grid(row=2, column=1, pady=(5, 25), padx=(0, 10))
num4.grid(row=2, column=0, pady=(5, 25), padx=(30, 30))

label_result.grid(row=3, column=1, pady=(0, 25), padx=(0, 75))

Button(root, text='porcentaje', command=show_answer).grid(row=3, column=0, pady=(5, 25), padx=(0, 25))

mainloop()
