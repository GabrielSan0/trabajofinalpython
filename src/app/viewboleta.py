import tkinter as tkk 
from src.app.controller import *
from entity import *
from tkinter import PhotoImage
from PIL import Image, ImageTk


c_fondo = '#363435'
c_verde = '#9AC6C5'
c_cuadro = '#3D4944'
c_botoningresar = '#099A97'
c_botonlimpiar = '#0E64EF'



#crear objeto de la clase tk
root =tkk.Tk()
root.title("FERETERIA SAC")
root.geometry("1440x960+180+20") #resolucion y posicion de la ventana 
root.minsize(1440 ,960)   #tamanio minimo en pantalla
root.config(bg=c_fondo)
r1 = None
#variables
trabajador=tkk.StringVar()
categoria=tkk.StringVar()
he=tkk.DoubleVar()
tardanzas=tkk.DoubleVar()

def limpiar():
    categoria.set("")
    trabajador.set("")
    he.set("")
    tardanzas.set("")
    txt3.delete("1.0",tkk.END)

def categorias():
    global r1  # Declarar r1 como global
    viewtrabajador=trabajador.get()
    viewcategoria=categoria.get()
    viewhe=he.get()
    viewtardanzas=tardanzas.get()
    txt3.delete("1.0",tkk.END)
    dat= Datos(viewtrabajador,viewcategoria,viewhe,viewtardanzas)
    pc= categoriacController()
    if viewcategoria == 'A':
        r1=pc.procesarA(dat)
    elif viewcategoria == 'B':
        r1=pc.procesarB(dat)
    elif viewcategoria == 'C':
        r1=pc.procesarC(dat)
    else:
        r1='la categoria ingresada no es un valor valido'
    
    txt3.insert("1.0",r1)
    

def abrir_viewboleta(r1):
    ventana_boleta = tkk.Toplevel(root)
    ventana_boleta.title("BOLETA")
    ventana_boleta.geometry("1440x960+180+20")
    ventana_boleta.minsize(860, 960)
    ventana_boleta.config(bg=c_fondo)

    lbl_r1 = tkk.Label(ventana_boleta, text=r1, font=("Consolas", 12))
    lbl_r1.pack()

    ventana_boleta.mainloop()



frameimage = tkk.Frame(root, width=1246, height=274, bg="red")
frameimage.pack()

img_original = Image.open('python/trabajofinal/images/imgferotek.jpg')
img_resized = img_original.resize((1246, 274), Image.ANTIALIAS)
img_titule = ImageTk.PhotoImage(img_resized)

label_image = tkk.Label(frameimage, image=img_titule)
label_image.pack(fill="both")








frametable = tkk.Frame(root, width=1246, height=274 )
frametable.config(bg=c_fondo)
frametable.pack()



frametitulos = tkk.Frame(root, width=1246, height=68)
frametitulos.config(bg=c_fondo)
frametitulos.pack()

frame = tkk.Frame(root, width=1246, height=174)
frame.config(bg=c_fondo)
frame.pack()

framebotones = tkk.Frame(root, width=1246, height=104, )
framebotones.config(bg=c_fondo)
framebotones.pack()



#cuadro titulos 
lbltrabajador=tkk.Label(frametable,text="N" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_verde, borderwidth=3  )
lbltrabajador.grid(row=0 ,column=0  , sticky="nsew" )

lbltrabajador=tkk.Label(frametable,text="CATEGORIA" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_verde, borderwidth=3  )
lbltrabajador.grid(row=0 ,column=1 , sticky="nsew")

lbltrabajador=tkk.Label(frametable,text="SUELDO" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_verde, borderwidth=3  )
lbltrabajador.grid(row=0 ,column=2 , sticky="nsew")

lbltrabajador=tkk.Label(frametable,text="SUELDO POR HORA" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_verde, borderwidth=3  )
lbltrabajador.grid(row=0 ,column=3 ,  sticky="nsew" )


#cuadro fila1
lbltrabajador=tkk.Label(frametable,text="1" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_cuadro, borderwidth=3  )
lbltrabajador.grid(row=1 ,column=0 )

lbltrabajador=tkk.Label(frametable,text="A" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_cuadro, borderwidth=3  )
lbltrabajador.grid(row=1 ,column=1  )

lbltrabajador=tkk.Label(frametable,text="S/.3000.00" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_cuadro, borderwidth=3  )
lbltrabajador.grid(row=1 ,column=2  )

lbltrabajador=tkk.Label(frametable,text="PH X4" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_cuadro, borderwidth=3  )
lbltrabajador.grid(row=1 ,column=3  )

#cuadro fila2
lbltrabajador=tkk.Label(frametable,text="2" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_cuadro, borderwidth=3  )
lbltrabajador.grid(row=2 ,column=0 )

lbltrabajador=tkk.Label(frametable,text="B" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_cuadro, borderwidth=3  )
lbltrabajador.grid(row=2 ,column=1  )

lbltrabajador=tkk.Label(frametable,text="S/.2500.00" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_cuadro, borderwidth=3  )
lbltrabajador.grid(row=2 ,column=2  )

lbltrabajador=tkk.Label(frametable,text="PH X3" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_cuadro, borderwidth=3  )
lbltrabajador.grid(row=2 ,column=3  )

#cuadro fila3
lbltrabajador=tkk.Label(frametable,text="3" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_cuadro, borderwidth=3  )
lbltrabajador.grid(row=3 ,column=0 )

lbltrabajador=tkk.Label(frametable,text="C" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_cuadro, borderwidth=3  )
lbltrabajador.grid(row=3 ,column=1  )

lbltrabajador=tkk.Label(frametable,text="S/.2000.00" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_cuadro, borderwidth=3  )
lbltrabajador.grid(row=3 ,column=2  )

lbltrabajador=tkk.Label(frametable,text="PH X2" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_cuadro, borderwidth=3  )
lbltrabajador.grid(row=3 ,column=3  )


#label de minititulo
lbltrabajador = tkk.Label(frametitulos, text="DATOS DE LA ENTRADA", width=76, fg="white", font=('Calibri', 24))
lbltrabajador.config(bg=c_verde, borderwidth=3)
lbltrabajador.grid( columnspan=2, padx=11 , pady=3)

#label de operaciones
lbltrabajador=tkk.Label(frame,text="Ingrese nombre del trabajo" ,width=23 ,  fg="white", font=('Calibri' , 12))
lbltrabajador.config(bg=c_fondo, borderwidth=3  )
lbltrabajador.grid(row=0 ,column=0 , padx=15, pady=15 )

txttrabajador=tkk.Entry(frame,textvariable=trabajador ,width=30 ,  fg="white" , font=('Calibri' , 12))
txttrabajador.config(bg=c_cuadro , highlightbackground=c_cuadro, highlightthickness=2, relief="groove")
txttrabajador.grid(row=0 ,column=1, padx=30 , pady=15)

lblcategoria=tkk.Label(frame,text="Ingrese categoria del trabajo" ,width=23 , fg="white" , font=('Calibri' , 12))
lblcategoria.config(bg=c_fondo , borderwidth=3)
lblcategoria.grid(row=0 ,column=3 , padx=30 , pady=15)

txtcategoria=tkk.Entry(frame,textvariable=categoria ,width=30 ,  fg="white" , font=('Calibri' , 12))
txtcategoria.config(bg=c_cuadro, highlightbackground=c_cuadro, highlightthickness=2, relief="groove" )
txtcategoria.grid(row=0 ,column=4 ,padx=15, pady=15)

lblhe=tkk.Label(frame,text="Ingrese horas extras del trabajo" ,  fg="white", font=('Calibri' , 12))
lblhe.config(bg=c_fondo, borderwidth=3)
lblhe.grid(row=1 ,column=0, padx=15)

txthe=tkk.Entry(frame,textvariable=he ,width=30 ,  fg="white" , font=('Calibri' , 12))
txthe.config(bg=c_cuadro , highlightbackground=c_cuadro, highlightthickness=2, relief="groove")
txthe.grid(row=1 ,column=1, padx=15)

lbltardanzas=tkk.Label(frame,text="Ingrese tardanzas del trabajo (EN MINUTOS)" ,  fg="white", font=('Calibri' , 12))
lbltardanzas.config(bg=c_fondo , borderwidth=3)
lbltardanzas.grid(row=1 ,column=3,padx=15)

txttardanzas=tkk.Entry(frame,textvariable=tardanzas ,width=30 ,  fg="white" , font=('Calibri' , 12))
txttardanzas.config(bg=c_cuadro, highlightbackground=c_cuadro, highlightthickness=2, relief="groove" )
txttardanzas.grid(row=1 ,column=4,padx=15)



btn1 = tkk.Button(framebotones, text="Ingresar", command=lambda: abrir_viewboleta(r1), width=30, fg="white", font=('Calibri', 12))
btn1.config(bg=c_botoningresar, highlightbackground=c_cuadro, highlightthickness=2, relief="groove")
btn1.grid(row=0, column=1, padx=100, pady=30)


btn2=tkk.Button(framebotones,text="Limpiar",command=limpiar, width=30 ,  fg="white" , font=('Calibri' , 12))
btn2.config(bg=c_botonlimpiar, highlightbackground=c_cuadro, highlightthickness=2, relief="groove" )
btn2.grid(row=0 ,column=2,padx=100, pady=30)
sp3=tkk.Label(root)

#imagen 

logo = PhotoImage(file='python/trabajofinal/images/logo.png')

txt3=tkk.Text(root)
txt3.pack()
txt3.config(width=50,height=10,font=("Consolas",12),
            padx=2,pady=12,selectbackground="red")
root.call('wm', 'iconphoto', root._w, logo)

#para de borrar 

#perderas el

root.mainloop()