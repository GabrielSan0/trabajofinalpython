import tkinter as tkk
from src.app.controller import CategoriacController
from src.app.entity import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox
import os


class ViewMain:

    CORE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    c_fondo = '#363435'
    c_verde = '#9AC6C5'
    c_cuadro = '#3D4944'
    c_botoningresar = '#099A97'
    c_botonlimpiar = '#0E64EF'
    r1 = None

    root = tkk.Tk()

    trabajador = tkk.StringVar()
    categoria = tkk.StringVar()
    he = tkk.DoubleVar()
    tardanzas = tkk.DoubleVar()

    txt3 = None

    def __int__(self):

        pass


    def home_view(self):

        self.root.title("FERETERIA SAC")
        self.root.geometry("1440x960+180+20")  # resolucion y posicion de la ventana
        self.root.minsize(1440, 960)  # tamanio minimo en pantalla
        self.root.config(bg=self.c_fondo)

        frameimage = tkk.Frame(self.root, width=1246, height=274, bg="red")
        frameimage.pack()

        mifile1 = os.path.join(self.CORE_DIR, "assets/images/imgferotek.jpg")
        img_original = Image.open(mifile1)
        img_resized = img_original.resize((1246, 274), Image.ANTIALIAS)
        img_titule = ImageTk.PhotoImage(img_resized)

        label_image = tkk.Label(frameimage, image=img_titule)
        label_image.pack(fill="both")

        frametable = tkk.Frame(self.root, width=1246, height=274)
        frametable.config(bg=self.c_fondo)
        frametable.pack()

        frametitulos = tkk.Frame(self.root, width=1246, height=68)
        frametitulos.config(bg=self.c_fondo)
        frametitulos.pack()

        frame = tkk.Frame(self.root, width=1246, height=174)
        frame.config(bg=self.c_fondo)
        frame.pack()

        framebotones = tkk.Frame(self.root, width=1246, height=104, )
        framebotones.config(bg=self.c_fondo)
        framebotones.pack()

        # cuadro titulos
        lbltrabajador = tkk.Label(frametable, text="N", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_verde, borderwidth=3)
        lbltrabajador.grid(row=0, column=0, sticky="nsew")

        lbltrabajador = tkk.Label(frametable, text="CATEGORIA", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_verde, borderwidth=3)
        lbltrabajador.grid(row=0, column=1, sticky="nsew")

        lbltrabajador = tkk.Label(frametable, text="SUELDO", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_verde, borderwidth=3)
        lbltrabajador.grid(row=0, column=2, sticky="nsew")

        lbltrabajador = tkk.Label(frametable, text="SUELDO POR HORA", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_verde, borderwidth=3)
        lbltrabajador.grid(row=0, column=3, sticky="nsew")

        # cuadro fila1
        lbltrabajador = tkk.Label(frametable, text="1", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_cuadro, borderwidth=3)
        lbltrabajador.grid(row=1, column=0)

        lbltrabajador = tkk.Label(frametable, text="A", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_cuadro, borderwidth=3)
        lbltrabajador.grid(row=1, column=1)

        lbltrabajador = tkk.Label(frametable, text="S/.3000.00", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_cuadro, borderwidth=3)
        lbltrabajador.grid(row=1, column=2)

        lbltrabajador = tkk.Label(frametable, text="PH X4", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_cuadro, borderwidth=3)
        lbltrabajador.grid(row=1, column=3)

        # cuadro fila2
        lbltrabajador = tkk.Label(frametable, text="2", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_cuadro, borderwidth=3)
        lbltrabajador.grid(row=2, column=0)

        lbltrabajador = tkk.Label(frametable, text="B", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_cuadro, borderwidth=3)
        lbltrabajador.grid(row=2, column=1)

        lbltrabajador = tkk.Label(frametable, text="S/.2500.00", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_cuadro, borderwidth=3)
        lbltrabajador.grid(row=2, column=2)

        lbltrabajador = tkk.Label(frametable, text="PH X3", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_cuadro, borderwidth=3)
        lbltrabajador.grid(row=2, column=3)

        # cuadro fila3
        lbltrabajador = tkk.Label(frametable, text="3", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_cuadro, borderwidth=3)
        lbltrabajador.grid(row=3, column=0)

        lbltrabajador = tkk.Label(frametable, text="C", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_cuadro, borderwidth=3)
        lbltrabajador.grid(row=3, column=1)

        lbltrabajador = tkk.Label(frametable, text="S/.2000.00", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_cuadro, borderwidth=3)
        lbltrabajador.grid(row=3, column=2)

        lbltrabajador = tkk.Label(frametable, text="PH X2", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_cuadro, borderwidth=3)
        lbltrabajador.grid(row=3, column=3)

        # label de minititulo
        lbltrabajador = tkk.Label(frametitulos, text="DATOS DE LA ENTRADA", width=76, fg="white", font=('Calibri', 24))
        lbltrabajador.config(bg=self.c_verde, borderwidth=3)
        lbltrabajador.grid(columnspan=2, padx=11, pady=3)

        # label de operaciones
        lbltrabajador = tkk.Label(frame, text="Ingrese nombre del trabajo", width=23, fg="white", font=('Calibri', 12))
        lbltrabajador.config(bg=self.c_fondo, borderwidth=3)
        lbltrabajador.grid(row=0, column=0, padx=15, pady=15)

        txttrabajador = tkk.Entry(frame, textvariable=self.trabajador, width=30, fg="white", font=('Calibri', 12))
        txttrabajador.config(bg=self.c_cuadro, highlightbackground=self.c_cuadro, highlightthickness=2, relief="groove")
        txttrabajador.grid(row=0, column=1, padx=30, pady=15)

        # input categoria
        lblcategoria = tkk.Label(frame, text="Ingrese categoria del trabajo", width=23, fg="white",
                                 font=('Calibri', 12))
        lblcategoria.config(bg=self.c_fondo, borderwidth=3)
        lblcategoria.grid(row=0, column=3, padx=30, pady=15)

        txtcategoria = tkk.Entry(frame, textvariable=self.categoria, width=30, fg="white", font=('Calibri', 12))
        txtcategoria.config(bg=self.c_cuadro, highlightbackground=self.c_cuadro, highlightthickness=2, relief="groove")
        txtcategoria.grid(row=0, column=4, padx=15, pady=15)

        lblhe = tkk.Label(frame, text="Ingrese horas extras del trabajo", fg="white", font=('Calibri', 12))
        lblhe.config(bg=self.c_fondo, borderwidth=3)
        lblhe.grid(row=1, column=0, padx=15)

        txthe = tkk.Entry(frame, textvariable=self.he, width=30, fg="white", font=('Calibri', 12))
        txthe.config(bg=self.c_cuadro, highlightbackground=self.c_cuadro, highlightthickness=2, relief="groove")
        txthe.grid(row=1, column=1, padx=15)

        lbltardanzas = tkk.Label(frame, text="Ingrese tardanzas del trabajo (EN MINUTOS)", fg="white",
                                 font=('Calibri', 12))
        lbltardanzas.config(bg=self.c_fondo, borderwidth=3)
        lbltardanzas.grid(row=1, column=3, padx=15)

        txttardanzas = tkk.Entry(frame, textvariable=self.tardanzas, width=30, fg="white", font=('Calibri', 12))
        txttardanzas.config(bg=self.c_cuadro, highlightbackground=self.c_cuadro, highlightthickness=2, relief="groove")
        txttardanzas.grid(row=1, column=4, padx=15)

        btn1 = tkk.Button(framebotones, text="Ingresar", command=self.categorias, width=30, fg="white", font=('Calibri', 12))
        btn1.config(bg=self.c_botoningresar, highlightbackground=self.c_cuadro, highlightthickness=2, relief="groove")
        btn1.grid(row=0, column=1, padx=100, pady=30)

        btn2 = tkk.Button(framebotones, text="Limpiar", command=self.limpiar, width=30, fg="white", font=('Calibri', 12))
        btn2.config(bg=self.c_botonlimpiar, highlightbackground=self.c_cuadro, highlightthickness=2, relief="groove")
        btn2.grid(row=0, column=2, padx=100, pady=30)
        sp3 = tkk.Label(self.root)

        # imagen

        mifile2 = os.path.join(self.CORE_DIR, "assets/images/logo.png")

        logo = PhotoImage(file=mifile2)

        self.txt3 = tkk.Text(self.root)
        self.txt3.pack()
        self.txt3.config(width=50, height=10, font=("Consolas", 12),
                    padx=2, pady=12, selectbackground="red")
        self.root.call('wm', 'iconphoto', self.root._w, logo)

        # para de borrar
        # perderas el

        self.root.mainloop()

    def limpiar(self, ):
        self.categoria.set("")
        self.trabajador.set("")
        self.he.set("")
        self.tardanzas.set("")
        self.txt3.delete("1.0", tkk.END)

    def categorias(self):
        global r1  # Declarar r1 como global
        # se obtiene los valroes

        try:
            viewtrabajador = self.trabajador.get()
            viewcategoria = self.categoria.get()
            viewhe = self.he.get()
            viewtardanzas = self.tardanzas.get()
        except:
            self.limpiar()
            messagebox.showinfo(message='Los datos no han sido ingresados correctamente', title="Error de validacion")


        try:
            self.txt3.delete("1.0", tkk.END)
            dat = Datos(viewtrabajador, viewcategoria, viewhe, viewtardanzas)
            pc = CategoriacController()
            if viewcategoria == 'A':
                r1 = pc.procesarA(dat)
            elif viewcategoria == 'B':
                r1 = pc.procesarB(dat)
            elif viewcategoria == 'C':
                r1 = pc.procesarC(dat)
            else:
                r1 = 'la categoria ingresada no es un valor valido'

            messagebox.showinfo(message=r1, title="Resultado")
        except:
            # self.limpiar()
            messagebox.showinfo(message='Los datos no han sido ingresados correctamente', title="Error en el sistema")


        # self.txt3.insert("1.0", r1)


if __name__ == '__main__':
    view = ViewMain()
    view.home_view()