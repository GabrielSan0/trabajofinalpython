import tkinter as tk
from PIL import ImageTk, Image #pip install Pillow
from logica import * 
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana Flotante")
ventana.geometry("1440x960")

# Establecer el color de fondo de la ventana
color_rgb = "#363435"  # Código de color RGB
ventana.configure(bg=color_rgb)

# Cargar la imagen
ruta_imagen = "ferreteria.png"
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((800, 262))  # Redimensionar la imagen a las dimensiones deseadas

imagen_tk = ImageTk.PhotoImage(imagen)

v = logica






# Mostrar la imagen en una etiqueta
etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
etiqueta_imagen.grid(row=0, column=0, padx=350, pady=10)








# Ejecutar la aplicación
ventana.mainloop()