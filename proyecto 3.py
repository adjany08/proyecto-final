from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import ttk
import os
import random
from random import choice
import datetime
import sys


    
class Interfaz:

    

    """
    E:N/A
    S:Creacion del constructor de la clase interfaz
    R:N/A
    """

    def __init__(self):
        self.rutaPersonajes = "personajes.txt"
        self.rutaUsaurios = "usuarios.txt"
        
    """
    E:N/A
    S:Creacion de la ventana principal
    R:N/A 
    """        


    def main(self):
        self.root = tk.Tk()
        self.root.title("Menú principal")
        self.root.geometry("700x500")
        self.root.config(bg="DodgerBlue4")
        self.root.resizable(False,False)
        imagen=PhotoImage(file="logo2.png")
        fondo=Label(self.root,image=imagen).place(x=250,y=50)

        tk.Label(self.root, text="         El GRAN TORNEO      ", font=("Rockwell Extra Bold", 15),bg="white" , fg="DodgerBlue4").pack(fill=tk.X)
        
        labelUsuario=tk.Label(self.root, text="Usuario " , font=("arial",15),bg="DodgerBlue4",fg="white").place(x=315,y=270)
        usuario = tk.StringVar()
        self.usuarioEntry=tk.Entry(self.root,textvariable=usuario,width=40).place(x=230, y=300)

        

        labelContra=tk.Label(self.root, text="Contraseña " , font=("arial",15),bg="DodgerBlue4",fg="white").place(x=300,y=323)
        contrasenna = tk.StringVar()
        self.contrasennaEntry=tk.Entry(self.root,show="*",textvariable=contrasenna,width=40).place(x=230, y=360)
    
        botonIngreso= tk.Button(self.root, text="Ingresar", width=10, font=("Aharoni",12), bg="white",fg="green", command=lambda:self.verificarClave(usuario.get(),contrasenna.get())).place(x=230,y=400)
        botonSalir= tk.Button(self.root, text="Salir", width=10,font=("Aharoni",12), bg="white",fg="red", command=lambda:self.Salir()).place(x=380,y=400)

        self.root.mainloop()





    """
    E:un usuario y contrasenna
    S:Funcion para volver al menu principal
    R:N/A
    """




    def verificarClave(self,usuario,contrasenna):
        contenido = self.retornaContenidoArchivo("usuarios.txt")
        lista = contenido[0]
        while contenido != []:
            if contenido[0][1] == usuario and contenido[0][2] == contrasenna:
                return self.opcionesJuego()

            else:
                contenido = contenido[1:]
        return tk.messagebox.showerror("Contraseña incorrecta ", "El usuario o la contraseña son incorrectos ")        
                
             
        
    """
    E:N/A
    S:Creacion de la ventana para guiar al usuario a las opcines de juego
    R:N/A
    """        
        
    def opcionesJuego(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Opciones de juego")
        self.root.config(bg=("DodgerBlue4"))
        self.root.resizable(False,False)
        
       

        tk.Label(self.root, text="         OPCIONES      ", font=("Rockwell Extra Bold", 15),bg="white" , fg="DodgerBlue4").pack(fill=tk.X)

        botonOJ1= tk.Button(self.root, text="Crear o borrar personajes", width=34, font=("Aharoni",12), bg="white",fg="DodgerBlue4", command=lambda:self.ventanaPersonaje()).place(x=60,y=110)
        botonOJ2= tk.Button(self.root, text="Crear o borrar torneo", width=34,font=("Aharoni",12), bg="white",fg="DodgerBlue4", command=lambda:self.ventanaTorneo()).place(x=60,y=170)
        botonOJ3= tk.Button(self.root, text="Jugar torneo",width=34, font=("Aharoni",12), bg="white",fg="DodgerBlue4", command=lambda:self.ventanaJugar()).place(x=350,y=260)
        botonOJ5= tk.Button(self.root, text="Estadisticas", width=34, font=("Aharoni",12), bg="white",fg="DodgerBlue4", command=lambda:self.noDisponible()).place(x=350,y=320)
        botonOJ6= tk.Button(self.root, text="Volver", width=34, font=("Aharoni",12), bg="white",fg="DodgerBlue4", command=lambda:self.volverMain()).place(x=60,y=410)

        
    """
    E:N/A
    S:Creacion de la ventana para la gestion de personajes
    R:N/A
    """
    
    def ventanaPersonaje(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Gestion de personajes")
        self.root.config(bg=("DodgerBlue4"))
        self.root.resizable(False,False)
        imagen=PhotoImage(file="tenor.gif")
        fondo=Label(self.root,bg="DodgerBlue4",image=imagen).place(x=351,y=180)
        
       

        tk.Label(self.root, text="         Gestión de personajes      ", font=("Rockwell Extra Bold", 15),bg="white" , fg="DodgerBlue4").pack(fill=tk.X)

        botonVP1= tk.Button(self.root, text="Crear  personaje", width=40, font=("Aharoni",12), bg="white",fg="DodgerBlue4", command=lambda:self.ventanaCrearPersonaje()).place(x=40,y=70)
        botonVP2= tk.Button(self.root, text="Borrar personaje", width=40,font=("Aharoni",12), bg="white",fg="red", command=lambda:self.ventanaBorrarPersonaje()).place(x=40,y=130)
        botonVP2= tk.Button(self.root, text="Volver", width=40,font=("Aharoni",12), bg="white",fg="black", command=lambda:self.opcionesJuego()).place(x=40,y=190)
        

        self.root.mainloop()

    """
    E:N/A
    S:Creacion de la ventana para crear personajes
    R:N/A
    """

        
        
    def ventanaCrearPersonaje(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Crear personaje")
        self.root.config(bg=("DodgerBlue4"))
        self.root.resizable(False,False)
        imagen=PhotoImage(file="superheroe2.png")
        fondo=Label(self.root,bg="DodgerBlue4",image=imagen).place(x=150,y=200)
        

        tk.Label(self.root, text="         Creando personaje      ", font=("Rockwell Extra Bold", 15),bg="white" , fg="DodgerBlue4").pack(fill=tk.X)

        labelTipo = tk.Label(self.root,fg="White", bg="DodgerBlue4",text="Seleccione el tipo de su personaje:",font=("Comic Sans MS",10)).place(x=20, y=70)
        tipo = tk.StringVar()
        self.comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = tipo, values=("Héroe","Villano")).place(x=250,y=70)

        labelSexo = tk.Label(self.root,fg="White", bg="DodgerBlue4",text="Seleccione el sexo de su personaje:",font=("Comic Sans MS",10)).place(x=20, y=100)
        sexo = tk.StringVar()
        self.comboSexo = ttk.Combobox(self.root,state="readonly", textvariable = sexo, width=20, values=("Mujer","Hombre","No determinado")).place(x=250,y=100)


        labelNombre = tk.Label(self.root,fg="White",bg="DodgerBlue4",text="Ingrese el nombre de su personaje:",font=("Comic Sans MS",10)).place(x=20, y=130)
        nombre = tk.StringVar()
        self.nombreEntry=tk.Entry(self.root,textvariable=nombre,width=30).place(x=250, y=130)


        labelAlter = tk.Label(self.root,fg="White", bg="DodgerBlue4",text="Ingrese el nombre de heroe/villano de su personaje:",font=("Comic Sans MS",10)).place(x=20, y=160)
        alter = tk.StringVar()
        self.nombreEntry=tk.Entry(self.root,textvariable=alter,width=20).place(x=350, y=160)


        labelVelocidad = tk.Label(self.root,fg="White", bg="DodgerBlue4",text="Velocidad:",font=("Comic Sans MS",10)).place(x=20, y=190)
        velocidad=IntVar()
        spinVel = Spinbox(self.root,width=5,state="readonly",textvariable=velocidad,from_=0,to=100).place(x=105,y=190)
       
        
        labelFuerza = tk.Label(self.root,fg="White", bg="DodgerBlue4",text="Fuerza:",font=("Comic Sans MS",10)).place(x=20, y=220)
        fuerza=IntVar()
        spinF = Spinbox(self.root,width=5,state="readonly",textvariable=fuerza,from_=0,to=100).place(x=105,y=220)
        

        labelInteligencia = tk.Label(self.root,fg="White", bg="DodgerBlue4",text="Inteligencia:",font=("Comic Sans MS",10)).place(x=20, y=250)
        inteligencia=IntVar()
        spinI = Spinbox(self.root,width=5,state="readonly",textvariable=inteligencia,from_=0,to=100).place(x=105,y=250)
        

        labelDefensaPersonal =tk.Label(self.root,fg="White", bg="DodgerBlue4",text="Defensa:",font=("Comic Sans MS",10)).place(x=20, y=280)
        defensa=IntVar()
        spinD = Spinbox(self.root,width=5,state="readonly",textvariable=defensa,from_=0,to=100).place(x=105,y=280)
        

        labelMagia = tk.Label(self.root,fg="White", bg="DodgerBlue4",text="Magia:",font=("Comic Sans MS",10)).place(x=20, y=310)
        magia=IntVar()
        spinM = Spinbox(self.root,width=5,state="readonly",textvariable=magia,from_=0,to=100).place(x=105,y=310)

        

        labelTelepatia = tk.Label(self.root,fg="White", bg="DodgerBlue4",text="Telepatia:",font=("Comic Sans MS",10)).place(x=20, y=340)
        telepatia=IntVar()
        spinT = Spinbox(self.root,width=5,state="readonly",textvariable=telepatia,from_=0,to=100).place(x=105,y=340)
        

        labelEstratega = tk.Label(self.root,fg="White", bg="DodgerBlue4",text="Estratega:",font=("Comic Sans MS",10)).place(x=20, y=370)
        estrategia=IntVar()
        spinE = Spinbox(self.root,width=5,state="readonly",textvariable=estrategia,from_=0,to=100).place(x=105,y=370)
        

        labelVolar = tk.Label(self.root,fg="White", bg="DodgerBlue4",text="Vuelo:",font=("Comic Sans MS",10)).place(x=20, y=400)
        vuelo=IntVar()
        spinV = Spinbox(self.root,width=5,state="readonly",textvariable=vuelo,from_=0,to=100).place(x=105,y=400)
        

        labelElasticidad = tk.Label(self.root,fg="White", bg="DodgerBlue4",text="Elasticidad:",font=("Comic Sans MS",10)).place(x=20, y=430)
        elasticidad=IntVar()
        spinElas = Spinbox(self.root,width=5,state="readonly",textvariable=elasticidad,from_=0,to=100).place(x=105,y=430)
        

        labelRegeneracion = tk.Label(self.root,fg="White", bg="DodgerBlue4",text="Regeneracion:",font=("Comic Sans MS",10)).place(x=20, y=460)
        regeneracion=IntVar()
        spinR = Spinbox(self.root,width=5,state="readonly",textvariable=regeneracion,from_=0,to=100).place(x=105,y=460)

        botonCP= (tk.Button(self.root, text="Guardar", width=10,
                            font=("Aharoni",12), bg="white",fg="green", command=lambda:self.guardarPersonaje(tipo.get(),sexo.get(),nombre.get(),alter.get(),velocidad.get(),
                            fuerza.get(),inteligencia.get(),defensa.get(),magia.get(),telepatia.get(),estrategia.get(),
                            vuelo.get(),elasticidad.get(),regeneracion.get())).place(x=400,y=420))         
                  
        botonSalir= tk.Button(self.root, text="Volver", width=10,font=("Aharoni",12), bg="white",fg="red", command=lambda:self.ventanaPersonaje()).place(x=520,y=420)
        

        self.root.mainloop()

    """

        Verificar archivos
    E: Una ruta
    S:1 o 0 dependiendo de si la ruta existe o no
    R: n/a
    O: verificar si existe un archivo con la ruta ingresada
    """



    def verificarArchivos(self,ruta): #Función que verifica si el archivo existe
        if not (os.path.isfile(ruta)):
            open (ruta,"w")
            1
        else:
            return 0
       


            

    """
    E:una lista y un nombre
    S:True si existe el personaje
    R:N/A
    """



    def existePersonaje(self, lista, alter):
        if lista != []:
            personaje = lista[0]
            if personaje[3].lower() == alter.lower():
                return True
            else:
                return self.existePersonaje(lista[1:], alter)
        else:
            return False

    """
    E:N/A
    S:Retornar el contenido de un archivo
    R:N/A
    """

    def retornaContenidoArchivo(self,ruta): 
        with open(ruta, "r") as archivo:
            todoTexto=archivo.read()
        convertirTextoALista = todoTexto.split("\n")
        return self.convierteALista(convertirTextoALista)

    """
    E:N/A
    S:Convertir a lista contenido de archivo
    R:N/A
    """

    def convierteALista(self,lista):
        if lista == []:
            return []
        elif lista[0] != "":
            return [lista[0].split(",")] + self.convierteALista(lista[1:])
        else:
            return self.convierteALista(lista[1:])

    """
    E:Un tipo y los atributos que posee el personaje
    S:Guardar un personaje en un archivo txt
    R:Las habilidades deben ser tipo int y no se permiten personajes repetidos
    """        


    def guardarPersonaje(self,tipo,sexo,nombre,alter,velocidad,fuerza,inteligencia,defensa,magia,telepatia,estrategia,vuelo,elasticidad,regeneracion):
        try:
            if (isinstance(tipo,str) and isinstance(sexo,str) and isinstance(nombre,str) and isinstance(alter,str) and isinstance(velocidad,int)
                and isinstance(fuerza,int) and isinstance(inteligencia,int) and isinstance(defensa,int) and isinstance(magia,int)
                and isinstance(telepatia,int) and isinstance(estrategia,int) and isinstance(vuelo,int) and isinstance(elasticidad,int)
                and (regeneracion,int)):
                    retorno = self.verificarArchivos(self.rutaPersonajes)
                    if retorno == 1 or retorno == 0:
                        contenido = self.retornaContenidoArchivo(self.rutaPersonajes)
                        if self.existePersonaje(contenido,alter):
                            tk.messagebox.showerror("Error ", "Ya existe un personaje guardado con este nombre ")
                        elif velocidad+fuerza+inteligencia+defensa+magia+telepatia+estrategia+vuelo+elasticidad+regeneracion!=100:
                            tk.messagebox.showerror("Error ", "La suma de las habilidades debe ser menor o igual a 100 ")
                        else:
                            if tipo !="" and sexo != "" and nombre != "" and alter != "" :
                                archivo = open(self.rutaPersonajes,"a")
                                archivo.write(tipo)
                                archivo.write(",")
                                archivo.write(sexo)
                                archivo.write(",")
                                archivo.write(nombre)
                                archivo.write(",")
                                archivo.write(alter)
                                archivo.write(",")
                                archivo.write(str(velocidad))
                                archivo.write(",")
                                archivo.write(str(fuerza))
                                archivo.write(",")
                                archivo.write(str(inteligencia))
                                archivo.write(",")
                                archivo.write(str(defensa))
                                archivo.write(",")
                                archivo.write(str(magia))
                                archivo.write(",")
                                archivo.write(str(telepatia))
                                archivo.write(",")
                                archivo.write(str(estrategia))
                                archivo.write(",")
                                archivo.write(str(vuelo))
                                archivo.write(",")
                                archivo.write(str(elasticidad))
                                archivo.write(",")
                                archivo.write(str(regeneracion))
                                archivo.write("\n")
                                archivo.close
                                tk.messagebox.showinfo("Personaje agregado", ("El  "+tipo+" "+alter+" ha sido agregado con exito"))
                            else:
                                tk.messagebox.showerror("Error en los datos", "No deben de haber espacios vacios")
                                
                        
        except ValueError:
            tk.messagebox.showerror("Error en los datos", "Ha ocurrido un error en los datos ingresados")
            
            
            
    """
    E:N/A
    S:Creacion de la ventana para borrar personaje
    R:N/A
    """            
        
     

    def ventanaBorrarPersonaje(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Borrar personaje")
        self.root.config(bg=("DodgerBlue4"))
        self.root.resizable(False,False)

        tk.Label(self.root, text="         Borrando personaje     ", font=("Rockwell Extra Bold", 15),bg="white" , fg="DodgerBlue4").pack(fill=tk.X)
        
        labelNombre = tk.Label(self.root, bg="DodgerBlue4",fg="white",text="Ingrese el nombre del personaje a borrar",font=("Comic Sans MS",20)).place(x=65, y=100)
        nombreB = tk.StringVar()
        nombreBEntry=tk.Entry(self.root,textvariable=nombreB,width=28).place(x=258, y=150)

                         
        botonEliminar = tk.Button(self.root, text="Borrar personaje", width=40,font=("Aharoni",12), bg="white",fg="red",command=lambda:self.eliminarPersonaje(nombreB.get())).place(x=180,y=290)                             

        botonVolver = tk.Button(self.root, text="      Volver     ", width=40,font=("Aharoni",12), bg="white",fg="DodgerBlue4", command=lambda:self.ventanaPersonaje()).place(x=180,y=350)


        self.root.mainloop

        """
    E:Una lista
    S:guardar items
    R:No aplica
    O:Guardar el contenido previo de un archivo
    """
    def guardarItems(self,lista):
        with open (self.rutaPersonajes, "w") as archivo:
            while lista !=[]:
                linea = ",".join(lista[0])+"\n"
                archivo.write(linea)
                lista = lista[1:]


 
        

    def eliminarPersonaje(self,nombre):
        contenido = self.retornaContenidoArchivo(self.rutaPersonajes)
        if self.existePersonaje(contenido,nombre):
            personajes = self.retornaContenidoArchivo(self.rutaPersonajes)
            nuevaL = []
            elimina = False
            for perso in personajes:
                if nombre != perso[2]:
                    nuevaL += [perso]
                else:
                    elimina = True
            if(elimina):
                self.guardarItems(nuevaL)
                tk.messagebox.showinfo("Personaje eliminado", ("La personaje " +nombre+ " ha sido elminada con exito"))
                
        else:
            tk.messagebox.showerror("Error en el nombre", "El personaje "+nombre+" no existe")


    




    """
    E:N/A
    S:Creacion de la ventana torneo
    R:N/A
    """        

    
    def ventanaTorneo(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Gestion de torneos")
        self.root.config(bg="DodgerBlue4")
        self.root.resizable(False, False)
        imagen=PhotoImage(file="torneo21.png")
        fondo=Label(self.root,bg="DodgerBlue4",image=imagen).place(x=351,y=180)
        

        tk.Label(self.root, text="         Gestion de torneos     ", font=("Rockwell Extra Bold", 15),bg="white" , fg="DodgerBlue4").pack(fill=tk.X)

        botonGT1= tk.Button(self.root, text="Crear  torneo", width=40, font=("Aharoni",12), bg="white",fg="DodgerBlue4", command=lambda:self.ventanaCrearTorneo()).place(x=40,y=70)
        botonGT2= tk.Button(self.root, text="Borrar torneo", width=40,font=("Aharoni",12), bg="white",fg="red", command=lambda:self.noDisponible()).place(x=40,y=130)
        botonGT3= tk.Button(self.root, text="Volver", width=40,font=("Aharoni",12), bg="white",fg="Black", command=lambda:self.opcionesJuego()).place(x=40,y=190)


        self.root.mainloop()

    """
    E:N/A
    S:Creacion de la ventana crear torneo
    R:N/A
    """

    def noDisponible(self):
        tk.messagebox.showinfo("Error ", "Esta funcion no esta disponible")
        


    def ventanaCrearTorneo(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Gestion de torneos")
        self.root.config(bg="DodgerBlue4")
        self.root.resizable(False, False)
        imagen=PhotoImage(file="torneo22.png")
        fondo=Label(self.root,bg="DodgerBlue4",image=imagen).place(x=351,y=190)

        tk.Label(self.root, text="         Creando torneo      ", font=("Rockwell Extra Bold", 13),bg="white" , fg="DodgerBlue4").pack(fill=tk.X)

        labelNombreT = tk.Label(self.root,fg="White",bg="DodgerBlue4",text="Ingrese el nombre del torneo:",font=("Comic Sans MS",13)).place(x=20, y=40)
        nombreTorneo = tk.StringVar()
        nombreEntry=tk.Entry(self.root,textvariable=nombreTorneo,width=30).place(x=300, y=43)

        labelFecha = tk.Label(self.root,fg="White",bg="DodgerBlue4",text="Ingrese la fecha del torneo:",font=("Comic Sans MS",13)).place(x=20, y=70)
        fecha = tk.StringVar()
        fechaEntry=tk.Entry(self.root,textvariable=fecha,width=30).place(x=300, y=73)


        labelLugar= tk.Label(self.root,fg="White",bg="DodgerBlue4",text="Ingrese el lugar del torneo:",font=("Comic Sans MS",13)).place(x=20, y=100)
        lugar = tk.StringVar()
        nombreEntry=tk.Entry(self.root,textvariable=lugar,width=30).place(x=300, y=103)

        
        labelLuchas= tk.Label(self.root,fg="White",bg="DodgerBlue4",text="Ingrese el número de luchas:",font=("Comic Sans MS",13)).place(x=20, y=130)
        luchas= IntVar()
        spinLuchas= Spinbox(self.root,width=5,state="readonly",textvariable=luchas,from_=1,to=5).place(x=300,y=133)


        labelModo = tk.Label(self.root,fg="White", bg="DodgerBlue4",text="Seleccione el modo de juego",font=("Comic Sans MS",13)).place(x=20, y=160)
        
        boton1 = (tk.Button(self.root, text="Manual", width=18, font=("Aharoni",12), bg="white",fg="black",
                            command=lambda:self.manual(luchas.get(),nombreTorneo.get(),fecha.get(),lugar.get())).place(x=80,y=200))
        boton2 = (tk.Button(self.root, text="Personaje vs Programa", width=18, font=("Aharoni",12), bg="white",fg="black",
                            command=lambda:self.perVSprograma(luchas.get(),nombreTorneo.get(),fecha.get(),lugar.get())).place(x=80,y=240))
        boton3 = (tk.Button(self.root, text="Programa vs Programa", width=18, font=("Aharoni",12), bg="white",fg="black",
                            command=lambda:self.programaVSprograma(luchas.get(),nombreTorneo.get(),fecha.get(),lugar.get())).place(x=80,y=280))

        botonSalir= tk.Button(self.root, text="Volver", width=10,font=("Aharoni",12), bg="white",fg="red", command=lambda:self.ventanaTorneo()).place(x=130,y=420)
        
        

        self.root.mainloop()


    """
    E:las luchas,nombreTorneo,fecha y lugar
    S:Funcion que valida las entradas de crear torneo
    R:N/A
    """
        
    def validaFecha(fecha):
        try:
            if fecha != datetime.strptime(fecha, "%Y-%m-%d").strftime('%Y-%m-%d'):
                raise ValueError
            return True
        except ValueError:
            return False
        
       
            
            

    def programaVSprograma(self,luchas,nombreTorneo,fecha,lugar):
        if luchas != "" and nombreTorneo != "" and fecha != "" and lugar !="":
            return self.ventanaluchaProgramaVSprograma(luchas,nombreTorneo,fecha,lugar)
        else:
            tk.messagebox.showerror("Error ", "No deben de existir espacios vacios")
        
        
                
            
    def ventanaluchaProgramaVSprograma(self,luchas,nombreTorneo,fecha,lugar):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Gestion de torneos")
        self.root.config(bg="DodgerBlue4")
        self.root.resizable(False, False)
        imagen=PhotoImage(file="tenor21.gif")
        fondo=Label(self.root,bg="DodgerBlue4",image=imagen).place(x=120,y=100)
        

        tk.Label(self.root, text="         Seleccion Automatica      ", font=("Rockwell Extra Bold", 13),bg="white" , fg="DodgerBlue4").pack(fill=tk.X)

        labelT=tk.Label(self.root, text=(" Seleccione Guardar para guardar el torneo "+nombreTorneo) , font=("Comic Sans MS",20),bg="DodgerBlue4",fg="white").place(x=60,y=50)


        botonSalir= tk.Button(self.root, text="Volver", width=34,font=("Aharoni"), bg="white",fg="red", command=lambda:self.ventanaCrearTorneo()).place(x=200,y=400)
        
        villanos = self.buscarVillanos()

        heroes = self.buscarHeroes()

        
        bandoH = []
        bandoV = []




        if luchas == 1:

            
            
            
            bandoV = [choice(villanos)]
            bandoH = [choice(heroes)]
            
        
            
            

        elif luchas == 2:

            

         
            bandoV = [choice(villanos)] +[choice(villanos)]  
            bandoH = bandoH = [choice(heroes)] +[choice(heroes)]
            



            
        elif luchas == 3:
            

  
            bandoV = [choice(villanos)] +[choice(villanos)]+[choice(villanos)]
            bandoH = [choice(heroes)] +[choice(heroes)]+[choice(heroes)]
             

            

        elif luchas == 4:

            
            bandoV = [choice(villanos)] +[choice(villanos)]+[choice(villanos)]+[choice(villanos)]
            bandoH = [choice(heroes)] +[choice(heroes)]+[choice(heroes)]+[choice(heroes)]
             

        
        elif luchas == 5:
            

         
            bandoV = [choice(villanos)] +[choice(villanos)]+[choice(villanos)]+[choice(villanos)]+[choice(villanos)]
            bandoH = [choice(heroes)] +[choice(heroes)]+[choice(heroes)]+[choice(heroes)]+[choice(heroes)]
             


            

        botonGuardar= (tk.Button(self.root,width=34, text="Guardar Torneo", font=("Aharoni"), bg="white",fg="green",
                                 command=lambda:self.crearTorneo(nombreTorneo,fecha,lugar,luchas,bandoH,bandoV)).place(x=200,y=350))

        self.root.mainloop()

        
            
#######################################################################################

    """
    E:las luchas,nombreTorneo,fecha y lugar
    S:Funcion que valida las entradas de crear torneo
    R:N/A
    """
        
        

    def perVSprograma(self,luchas,nombreTorneo,fecha,lugar):
        if luchas != "" and nombreTorneo != "" and fecha != "" and lugar !="":
            return self.ventanaluchaProgramaVSprograma(luchas,nombreTorneo,fecha,lugar)
        else:
            tk.messagebox.showerror("Error ", "No deben de existir espacios vacios")
             

    def ventanaluchaPersonaVSprograma(self, luchas,nombreTorneo,fecha,lugar):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Seleccion de bandos")
        self.root.config(bg="DodgerBlue4")
        self.root.resizable(False, False)
        imagen=PhotoImage(file="levantamiento.png")
        fondo=Label(self.root,image=imagen,bg="DodgerBlue4").place(x=120,y=200)
        
        tk.Label(self.root, text="         seleccione un  bando      ", font=("Rockwell Extra Bold", 13),bg="white" , fg="DodgerBlue4").pack(fill=tk.X)

        

        botonH = (tk.Button(self.root, text="Héroes", width=34,font=("Aharoni",12), bg="white",fg="DodgerBlue4",
                            command=lambda:self.ventanaSeleccionHeroes(luchas,nombreTorneo,fecha,lugar)).place(x=100,y=90))
        botonV = (tk.Button(self.root, text="Villanos", width=34,font=("Aharoni",12), bg="white",fg="DodgerBlue4",
                            command=lambda:self.ventanaSeleccionVillanos(luchas,nombreTorneo,fecha,lugar)).place(x=100,y=140))
        botonVolver = (tk.Button(self.root, text="Volver", width=34,font=("Aharoni",12), bg="white",fg="red",
                                 command=lambda:self.ventanaCrearTorneo()).place(x=100,y=190))



        self.root.mainloop()
        
        
    def ventanaSeleccionVillanos(self,luchas,nombreTorneo,fecha,lugar):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Gestion de torneos")
        self.root.config(bg="DodgerBlue4")
        self.root.resizable(False, False)

        tk.Label(self.root, text="         Seleccion de  personajes      ", font=("Rockwell Extra Bold", 13),bg="white" , fg="DodgerBlue4").pack(fill=tk.X)

        labelT=tk.Label(self.root, text=(" Seleccione los villanos para el torneo "+nombreTorneo) , font=("Comic Sans MS",20),bg="DodgerBlue4",fg="white").place(x=60,y=50)

        

        botonSalir= tk.Button(self.root, text="Volver", width=34,font=("Aharoni"), bg="white",fg="red", command=lambda:self.ventanaCrearTorneo()).place(x=200,y=400)
        
        villanos = self.buscarVillanos()

        heroes = self.buscarHeroes()

        
        bandoH = []
        bandoV = []




        if luchas == 1:

                        

            
            villano1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano1, values=villanos).place(x=220,y=120)
            
            
            bandoH = [choice(heroes)]
            bandoV =[villano1.get()]
        
            
            

        elif luchas == 2:

            
            villano1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano1, values=villanos).place(x=250,y=120)
            villano2 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano2, values=villanos).place(x=250,y=150)

            bandoH = [choice(heroes)] +[choice(heroes)]
            bandoV = [[villano1.get()] + [villano2.get()]]



            
        elif luchas == 3:
            


            villano1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano1, values=villanos).place(x=250,y=120)
            villano2 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano2, values=villanos).place(x=250,y=150)
            villano3 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano3, values=villanos).place(x=250,y=180)

            bandoH = [choice(heroes)] +[choice(heroes)]+[choice(heroes)]
            bandoV = [[villano1.get()] + [villano2.get()] + [villano3.get()]]

            

        elif luchas == 4:
            
          

                        
            villano1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano1, values=villanos).place(x=257,y=120)
            villano2 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano2, values=villanos).place(x=257,y=150)
            villano3 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano3, values=villanos).place(x=257,y=180)
            villano4 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano4, values=villanos).place(x=257,y=210)

            bandoH = [choice(heroes)] +[choice(heroes)]+[choice(heroes)]+[choice(heroes)]
            bandoV = [[villano1.get()] + [villano2.get()] + [villano3.get()] + [villano4.get()]]

        
        elif luchas == 5:
            
            villano1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano1, values=(villanos)).place(x=257,y=120)
            villano2 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano2, values=(villanos)).place(x=257,y=150)
            villano3 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano3, values=(villanos)).place(x=257,y=180)
            villano4 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano4, values=(villanos)).place(x=257,y=210)
            villano5 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano5, values=(villanos)).place(x=257,y=240)
            
            bandoH = [choice(heroes)] +[choice(heroes)]+[choice(heroes)]+[choice(heroes)]+[choice(heroes)]
            bandoV = [[villano1.get()] + [villano2.get()] + [villano3.get()] + [villano4.get()] + [villano5.get()]]


            

        botonGuardar= (tk.Button(self.root,width=34, text="Guardar Torneo", font=("Aharoni"), bg="white",fg="green",
                                 command=lambda:self.crearTorneo(nombreTorneo,fecha,lugar,luchas,bandoH,bandoV)).place(x=200,y=350))
        
        self.root.mainloop()
        
    def ventanaSeleccionHeroes(self,luchas,nombreTorneo,fecha,lugar):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Gestion de torneos")
        self.root.config(bg="DodgerBlue4")
        self.root.resizable(False, False)

        tk.Label(self.root, text="         Seleccion de  personajes      ", font=("Rockwell Extra Bold", 13),bg="white" , fg="DodgerBlue4").pack(fill=tk.X)

        labelT=tk.Label(self.root, text=(" Seleccione los héroes para el torneo "+nombreTorneo) , font=("Comic Sans MS",20),bg="DodgerBlue4",fg="white").place(x=60,y=50)


        botonSalir= tk.Button(self.root, text="Volver", width=34,font=("Aharoni"), bg="white",fg="red", command=lambda:self.ventanaCrearTorneo()).place(x=200,y=400)
        
        villanos = self.buscarVillanos()

        heroes = self.buscarHeroes()

        
        bandoH = []
        bandoV = []




        if luchas == 1:

            

            
            heroe1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe1, values=heroes).place(x=257,y=120)
            
            
            bandoV = [choice(villanos)]
            bandoH =[heroe1.get()]
            
        
            
            

        elif luchas == 2:

            
            heroe1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe1,values=heroes).place(x=257,y=120)
            heroe2= tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe2,values=heroes).place(x=257,y=150)

         
            bandoV = [choice(villanos)] +[choice(villanos)]  
            bandoH = [[heroe1.get()] + [heroe2.get()]]
            



            
        elif luchas == 3:
            
            heroe1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe1,values=heroes).place(x=257,y=120)
            heroe2 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe2,values=heroes).place(x=257,y=150)
            heroe3 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe3,values=heroes).place(x=257,y=180)

  
            bandoV = [choice(villanos)] +[choice(villanos)]+[choice(villanos)]
            bandoH = [[heroe1.get()] + [heroe2.get()] + [heroe3.get()]]
             

            

        elif luchas == 4:
            
            heroe1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe1, values=heroes).place(x=257,y=120)
            heroe2 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe2, values=heroes).place(x=257,y=150)
            heroe3 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe3, values=heroes).place(x=257,y=180)
            heroe4 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe4, values=heroes).place(x=257,y=210)


            
            bandoV = [choice(villanos)] +[choice(villanos)]+[choice(villanos)]+[choice(villanos)]
            bandoH = [[heroe1.get()] + [heroe2.get()] + [heroe3.get()] + [heroe4.get()]]
             

        
        elif luchas == 5:
            heroe1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe1, values=(heroes)).place(x=257,y=120)
            heroe2 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe2, values=(heroes)).place(x=257,y=150)
            heroe3 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe3, values=(heroes)).place(x=257,y=180)
            heroe4 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe4, values=(heroes)).place(x=257,y=210)
            heroe5 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe5, values=(heroes)).place(x=257,y=240)

         
            bandoV = [choice(villanos)] +[choice(villanos)]+[choice(villanos)]+[choice(villanos)]+[choice(villanos)]
            bandoH = [[heroe1.get()] + [heroe2.get()] + [heroe3.get()] + [heroe4.get()] + [heroe5.get()]]
             


            

        botonGuardar= (tk.Button(self.root,width=34, text="Guardar Torneo", font=("Aharoni"), bg="white",fg="green",
                                 command=lambda:self.crearTorneo(nombreTorneo,fecha,lugar,luchas,bandoH,bandoV)).place(x=200,y=350))

        self.root.mainloop()
#############################################################################################    
    """
    E:las luchas,nombreTorneo,fecha y lugar
    S:Funcion que valida las entradas de crear torneo
    R:N/A
    """




    def manual(self,luchas,nombreTorneo,fecha,lugar):
        if luchas != "" and nombreTorneo != "" and fecha != "" and lugar !="":
            return self.ventanaluchaProgramaVSprograma(luchas,nombreTorneo,fecha,lugar)
        else:
            tk.messagebox.showerror("Error ", "No deben de existir espacios vacios")
            
            

    
    """
    E:N/A
    S:Funcion que crea una lista de villanos
    R:N/A
    """

    def buscarVillanos(self):
        contenido = self.retornaContenidoArchivo(self.rutaPersonajes)
        lista = contenido[0]
        listaVillanos = []
        while contenido != []:
            if contenido[0][0] == "Villano":
                listaVillanos += [contenido[0][3]]
                contenido = contenido[1:]
            else:
                contenido = contenido[1:]
        return listaVillanos


    """
    E:N/A
    S:Funcion que crea una lista de heroes
    R:N/A
    """


    def buscarHeroes(self):
        contenido = self.retornaContenidoArchivo(self.rutaPersonajes)
        listaHeroes = []
        while contenido != []:
            if contenido[0][0] == "Héroe":
                listaHeroes += [contenido[0][3]]
                contenido = contenido[1:]
            else:
                contenido = contenido[1:]
        return listaHeroes
        
                
    """
    E:N/A
    S:Creacion de la ventana para escoger a los personajes
    R:N/A
    """         
        

            
    def luchaManual(self,luchas,nombreTorneo,fecha,lugar):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Gestion de torneos")
        self.root.config(bg="DodgerBlue4")
        self.root.resizable(False, False)

        tk.Label(self.root, text="         Seleccion de  personajes      ", font=("Rockwell Extra Bold", 13),bg="white" , fg="DodgerBlue4").pack(fill=tk.X)

        labelT=tk.Label(self.root, text=(" Seleccione los personajes para el torneo "+nombreTorneo) , font=("arial",15),bg="DodgerBlue4",fg="white").place(x=150,y=50)

        labelT=tk.Label(self.root, text=" Seleccione los Heroes " , font=("arial",15),bg="DodgerBlue4",fg="white").place(x=90,y=150)
        labelT=tk.Label(self.root, text=" Seleccione los Villanos ", font=("arial",15),bg="DodgerBlue4",fg="white").place(x=390,y=150)

        botonSalir= tk.Button(self.root, text="Volver", width=10,font=("Aharoni",12), bg="white",fg="red", command=lambda:self.ventanaCrearTorneo()).place(x=130,y=420)
        
        villanos = self.buscarVillanos()

        heroes = self.buscarHeroes()

        
        bandoH = []
        bandoV = []




        if luchas == 1:

            

            
            heroe1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe1, values=heroes).place(x=100,y=190)
            
            

            
            villano1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano1, values=villanos).place(x=400,y=190)
            

            bandoH =[heroe1.get()]
            bandoV =[villano1.get()]
        
            
            

        elif luchas == 2:

            
            heroe1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe1,values=heroes).place(x=100,y=190)
            heroe2= tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe2,values=heroes).place(x=100,y=220)

            villano1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano1, values=villanos).place(x=400,y=190)
            villano2 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano2, values=villanos).place(x=400,y=220)

            bandoH = [[heroe1.get()] + [heroe2.get()]]
            bandoV = [[villano1.get()] + [villano2.get()]]



            
        elif luchas == 3:
            
            heroe1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe1,values=heroes).place(x=100,y=190)
            heroe2 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe2,values=heroes).place(x=100,y=220)
            heroe3 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe3,values=heroes).place(x=100,y=250)

            villano1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano1, values=villanos).place(x=400,y=190)
            villano2 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano2, values=villanos).place(x=400,y=220)
            villano3 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano3, values=villanos).place(x=400,y=250)

            bandoH = [[heroe1.get()] + [heroe2.get()] + [heroe3.get()]]
            bandoV = [[villano1.get()] + [villano2.get()] + [villano3.get()]]

            

        elif luchas == 4:
            
            heroe1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe1, values=heroes).place(x=100,y=190)
            heroe2 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe2, values=heroes).place(x=100,y=220)
            heroe3 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe3, values=heroes).place(x=100,y=250)
            heroe4 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe4, values=heroes).place(x=100,y=280)


            


                        
            villano1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano1, values=villanos).place(x=400,y=190)
            villano2 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano2, values=villanos).place(x=400,y=220)
            villano3 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano3, values=villanos).place(x=400,y=250)
            villano4 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano4, values=villanos).place(x=400,y=280)

            bandoH = [[heroe1.get()] + [heroe2.get()] + [heroe3.get()] + [heroe4.get()]]
            bandoV = [[villano1.get()] + [villano2.get()] + [villano3.get()] + [villano4.get()]]

        
        elif luchas == 5:
            heroe1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe1, values=(heroes)).place(x=100,y=190)
            heroe2 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe2, values=(heroes)).place(x=100,y=220)
            heroe3 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe3, values=(heroes)).place(x=100,y=250)
            heroe4 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe4, values=(heroes)).place(x=100,y=280)
            heroe5 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = heroe5, values=(heroes)).place(x=100,y=310)

            villano1 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano1, values=(villanos)).place(x=400,y=190)
            villano2 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano2, values=(villanos)).place(x=400,y=220)
            villano3 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano3, values=(villanos)).place(x=400,y=250)
            villano4 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano4, values=(villanos)).place(x=400,y=280)
            villano5 = tk.StringVar()
            comboTipo = ttk.Combobox(self.root,width=20,state="readonly",textvariable = villano5, values=(villanos)).place(x=400,y=310)

            bandoH = [[heroe1.get()] + [heroe2.get()] + [heroe3.get()] + [heroe4.get()] + [heroe5.get()]]
            bandoV = [[villano1.get()] + [villano2.get()] + [villano3.get()] + [villano4.get()] + [villano5.get()]]


            

        botonGuardar= (tk.Button(self.root, text="Guardar Torneo", font=("Aharoni",12), bg="white",fg="green",
                                 command=lambda:self.crearTorneo(nombreTorneo,fecha,lugar,luchas,bandoH,bandoV)).place(x=400,y=420))

        self.root.mainloop()

###################################################################################################################################################

    """
    E:N/A
    S:Funcion para volver al menu principal
    R:N/A
    """

    def crearTorneo(self, nombreTorneo,fecha,lugar,luchas,bandoH,bandoV):
        bandoGanador = bandoH + bandoV
        torneoNuevo = Definicion_Torneo(nombreTorneo,fecha,lugar,luchas,bandoGanador)
        tk.messagebox.showinfo("Creado ", "El torneo ha sido creado con éxito")
        return self.ventanaCrearTorneo()
        
         
        
        
        
        
            
            

    """
    E:N/A
    S:Funcion para volver al menu principal
    R:N/A
    """

    def volverMain(self):
        self.root.destroy()
        self.main()
        
    """
    E:N/A
    S:Creacion del constructor de la clase interfaz
    R:N/A
    """        

    def ventanaJugar(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Jugar torneo")
        self.root.config(bg="DodgerBlue4")
        self.root.resizable(False, False)
        imagen=PhotoImage(file="swords.png")
        fondo=Label(self.root,bg="DodgerBlue4",image=imagen).place(x=240,y=70)

        tk.Label(self.root, text="         Jugar torneo      ", font=("Rockwell Extra Bold", 13),bg="white" , fg="DodgerBlue4").pack(fill=tk.X)

        torneos=[]
        comboTorneo = ttk.Combobox(self.root,width=20,state="readonly",values=(torneos)).place(x=265,y=320)
        
        botonJugar = tk.Button(self.root, text="Jugar Torneo",width=20, font=("Aharoni",12), bg="white",fg="green",command=lambda:self.noDisponible()).place(x=255,y=350)
        botonVolver = tk.Button(self.root, text="Volver",width=20, font=("Aharoni",12), bg="white",fg="red",command=lambda:self.opcionesJuego()).place(x=255,y=390)



        self.root.mainloop()



    """
    E:No aplica
    S:salida del sistema
    R:No aplica
    O:uso de la libreria sys para salir del programa creado
    """
    def Salir(self):
        
        self.root.destroy()
        sys.exit()
   

        


class Definicion_Torneo():

    
    """
    E:nombreTorneo,fecha,lugar,luchas,bandoGanador
    S:constructor de la definicion de torneo
    R:N/A
    """


    def __init__(self,nombreTorneo,fecha,lugar,luchas,bandoGanador):

        self.nombreTorneo = nombreTorneo
        self.fecha = fecha
        self.lugar = lugar
        self.luchas = luchas
        self.bandoGanador = []

class Definicion_Luchas():
    
    """
    E:nombreTorneo,fecha,lugar,luchas,bandoGanador
    S:constructor de la definicion de luchas
    R:N/A
    """


    def __init__(nombreTorneo,fecha,lugar,luchas,):

        self.nombreTorneo = nombreTorneo
        self.fecha = fecha
        self.lugar = lugar
        self.luchas = luchas
        self.bandoGanador = []

        




 
        
###############################################
a=Interfaz()
a.main()




        


