from tkinter import *
from tkinter import messagebox
import sqlite3

root= Tk()
root.geometry("300x450")

#===Funciones===#
def conexionBase():
	conexion= sqlite3.connect("BaseDatos")
	cursor= conexion.cursor()

	try:
		cursor.execute('''
			CREATE TABLE USUARIO(
			ID INTEGER PRIMARY KEY, 
			NOMBRE VARCHAR(10), 
			APELLIDO VARCHAR(20), 
			CIAL INTEGER(10), 
			CLASE VARCHAR(10), 
			DOMICILIO VARCHAR(20), 
			CORREO VARCHAR(30), 
			COMENTARIO VARCHAR(200))
			''')

		messagebox.showinfo("Base de Datos", "La base de datos se ha creado correctamente")

	except:
		messagebox.showwarning("Warning", "La base de datos ya esta creada")

def salirAplicacion():
	valor= messagebox.askquestion("Salir", "Seguro que deseas salir de la aplicacion?")

	if valor=="yes":
		root.destroy()

def limpiarCampos():
	id.set("")
	nombre.set("")
	apellido.set("")
	cial.set("")
	clase.set("")
	domicilio.set("")
	correo.set("")
	cuadroComentario.delete(1.0, END) #1.0-> Punto de partida para empezar a borrar. END-> Punto en el que acabar de borrar

def create():
	conexion= sqlite3.connect("BaseDatos")
	cursor= conexion.cursor()

	"""cursor.execute("INSERT INTO USUARIO VALUES('"+ id.get() + 
		"','" + nombre.get() + 
		"','" + apellido.get() +
		"','" + cial.get() +
		"','" + clase.get() + 
		"','" + domicilio.get() + 
		"','" + correo.get() +
		"','" + cuadroComentario.get("1.0", END) + "')")"""

	dates= id.get(), nombre.get(), apellido.get(), cial.get(), clase.get(), domicilio.get(), correo.get(), cuadroComentario.get("1.0", END)

	cursor.execute("INSERT INTO USUARIO VALUES(?,?,?,?,?,?,?,?)", dates)

	conexion.commit()

	messagebox.showinfo("Base de Datos", "Registro insertado con exito")

def read():
	conexion= sqlite3.connect("BaseDatos")
	cursor= conexion.cursor()

	cursor.execute("SELECT * FROM USUARIO WHERE ID=" + id.get())

	usuario= cursor.fetchall()

	for user in usuario:
		id.set(user[0])
		nombre.set(user[1])
		apellido.set(user[2])
		cial.set(user[3])
		clase.set(user[4])
		domicilio.set(user[5])
		correo.set(user[6])
		cuadroComentario.insert(1.0, user[7])

	conexion.commit()


def update():
	conexion= sqlite3.connect("BaseDatos")
	cursor= conexion.cursor()

	"""cursor.execute("UPDATE USUARIO SET NOMBRE='" + nombre.get() +
		"', APELLIDO= '"+ apellido.get() +
		"', CIAL= '"+ cial.get() +
		"', CLASE= '"+ clase.get() +
		"', DOMICILIO= '"+ domicilio.get() +
		"', CORREO= '"+ correo.get() +
		"', COMENTARIO= '"+ cuadroComentario.get("1.0", END) +
		"' WHERE ID=" + id.get()
		)"""

	dates= nombre.get(), apellido.get(), cial.get(), clase.get(), domicilio.get(), correo.get(), cuadroComentario.get(1.0, END)

	cursor.execute("UPDATE USUARIO SET NOMBRE=?, APELLIDO=?, CIAL=?, CLASE=?, DOMICILIO=?, CORREO=?, COMENTARIO=?" + 
					"WHERE ID=" + id.get(), dates)

	conexion.commit()

	messagebox.showinfo("Update", "Registro actualizado con exito")


def delete():
	conexion= sqlite3.connect("BaseDatos")
	cursor= conexion.cursor()

	cursor.execute("DELETE FROM USUARIO WHERE ID=" + id.get())

	conexion.commit()

	messagebox.showinfo("Delete", "Registro eliminado con exito")

def paginaWeb():
	import webbrowser
	webbrowser.open("https://github.com/RoberVF/Python-SQL/edit/master/README.md", new=2, autoraise=True)

#===Menu===#
barraMenu= Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu= Menu(barraMenu, tearoff= 0)
bbddMenu.add_command(label= "Crear BBDD", command=conexionBase)
bbddMenu.add_command(label= "Salir", command=salirAplicacion)

borrarMenu= Menu(barraMenu, tearoff= 0)
borrarMenu.add_command(label= "Borrar campos", command=limpiarCampos)

crudMenu= Menu(barraMenu, tearoff= 0)
crudMenu.add_command(label= "Create", command= create)
crudMenu.add_command(label= "Read", command= read)
crudMenu.add_command(label= "Update", command= update)
crudMenu.add_command(label= "Delete", command= delete)

ayudaMenu= Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Ayuda", command=paginaWeb)

barraMenu.add_cascade(label= "BBDD", menu=bbddMenu)
barraMenu.add_cascade(label= "Borrar", menu=borrarMenu)
barraMenu.add_cascade(label= "CRUD", menu=crudMenu)
barraMenu.add_cascade(label= "Ayuda", menu=ayudaMenu)


#===Comienzo===#

frame= Frame(root)
frame.pack()

id= StringVar()
nombre= StringVar()
apellido= StringVar()
cial= StringVar()
clase= StringVar()
domicilio= StringVar()
correo= StringVar()


cuadroID= Entry(frame, textvariable= id) #textvariable-> Asi podremos modificar los string de Entry()
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre= Entry(frame, textvariable= nombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

cuadroApellido= Entry(frame, textvariable= apellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroCIAL= Entry(frame, textvariable= cial)
cuadroCIAL.grid(row=3, column=1, padx=10, pady=10)

cuadroClase= Entry(frame, textvariable= clase)
cuadroClase.grid(row=4, column=1, padx=10, pady=10)

cuadroDomicilio= Entry(frame, textvariable= domicilio)
cuadroDomicilio.grid(row=5, column=1, padx=10, pady=10)

cuadroCorreo= Entry(frame, textvariable= correo)
cuadroCorreo.grid(row=6, column=1, padx=10, pady=10)

cuadroComentario= Text(frame, width=16, height=5)
cuadroComentario.grid(row=7, column=1, padx=10, pady=10)
scrollVert= Scrollbar(frame, command= cuadroComentario.yview)
scrollVert.grid(row=7, column=2, sticky="nsew")

cuadroComentario.config(yscrollcommand= scrollVert.set)

#===Etiquetas===#

idLabel= Label(frame, text= "ID : ")
idLabel.grid(row=0, column=0)

nombreLabel= Label(frame, text="Nombre : ")
nombreLabel.grid(row=1, column=0)

apellidoLabel= Label(frame, text="Apellido : ")
apellidoLabel.grid(row=2, column=0)

cialLabel= Label(frame, text="CIAL : ")
cialLabel.grid(row=3, column=0)

claseLabel= Label(frame, text="Clase : ")
claseLabel.grid(row=4, column=0)

domicilioLabel= Label(frame, text="Domicilio : ")
domicilioLabel.grid(row=5, column=0)

correoLabel= Label(frame, text="Correo : ")
correoLabel.grid(row=6, column=0)

comentarioLabel= Label(frame, text="Comentario : ")
comentarioLabel.grid(row=7, column=0)


#===Botones===#

frame2= Frame(root)
frame2.pack()

botonCreate= Button(frame2, text="Create", command=create)
botonCreate.grid(row=0, column=0, padx=10, pady=10)

botonRead= Button(frame2, text="Read", command= read)
botonRead.grid(row=0, column=1, padx=10, pady=10)

botonUpdate= Button(frame2, text="Update", command= update)
botonUpdate.grid(row=0, column=2, padx=10, pady=10)

botonDelete= Button(frame2, text="Delete", command= delete)
botonDelete.grid(row=0, column=3, padx=10, pady=10)




root.mainloop()