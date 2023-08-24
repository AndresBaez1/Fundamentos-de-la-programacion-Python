
def menu1():

	op = input ("""\n\n
	[0] SALIR
	[1] ABRIR ARCHIVO EXISTENTE
	[2] CREAR NUEVO ARCHIVO

	INGRESE NUMERO DE OPCION    : """ )
	return op



def menu2():

	op = input ("""\n\n
	[0] SALIR
	[1] CARGAR ALUMNOS
	[2] IMPRIMIR LISTA DE ALUMNOS 
	[3] CANTIDAD DE ALUMNOS INSCRIPTOS 
	[4] LISTA DE ALUMNOS DE UNA MISMA COMISION
	[5] PREGUNTAR SI UN ALUMNO SE ENCUENTRA EN LA LISTA
	[6] PREGUNTAR ALUMNOS CON PROMEDIO MAS ALTO
	[7] PREGUNTAR EL PROMEDIO DE NOTAS DE UN ALUMNO
	[8] VOLVER AL MENU ANTERIOR

		INGRESE NUMERO DE OPCION                       : """ )

	return op

def leer_alumno():
#LEE UN ALUMNO Y LO RETORNA

	alumno = dict()
	#'alumno' contiene {dni: "", nombre: "", apellido: "", comision: "", notas:[0,0,0,0]}

	os.system(limpiar_pantalla) #Limpia la pantalla
	print("\n	PARA SALIR INGRESE DNI: '999' \n")
	alumno['dni'] = input("	ingrese DNI               : ")
	if (alumno['dni'] != '999'):
		alumno['nombre']   = input("	ingrese nombre            : ")
		alumno['apellido'] = input("	ingrese apellido          : ")
		alumno['comision'] = input("	ingrese numero de comision: ")

		alumno['notas']= [] #Crea una lista de notas
		for i in ("primera", "segunda", "tercera", "cuarta "):
			alumno['notas'].append(int(input("	ingrese %s nota      : " % i)))
	
	return alumno
    
def imprimir_alumno(alumno):
	
	print("\n")
	print("	Nombre y Apellido: %s" % alumno['nombre']+" "+alumno['apellido'])
	print("	DNI              : %s" % alumno['dni'])
	print("	Comision         : %s" % alumno['comision'])
	print("	Notas            :", alumno['notas'])
	

def cargar(NOMBRE_ARCHIVO):
#CARGA ALUMNOS HASTA RECIBIR UN ALUMNO CON DNI 999

	alumno = dict()
	archivo = open (NOMBRE_ARCHIVO, 'a')

	
	alumno = leer_alumno()
	while (alumno['dni'] != '999'):
		archivo.write(str(alumno)+"\n")
		alumno = leer_alumno()
		
	archivo.close()


def imprimir_archivo(NOMBRE_ARCHIVO):
#IMPRIME CADA ALUMNO DEL ARCHIVO

	archivo = open (NOMBRE_ARCHIVO, 'r')
	
	
	for linea in archivo:
		imprimir_alumno(eval(linea))
		
		
	archivo.close()


def cantidad_de_alumnos(NOMBRE_ARCHIVO):
#CADA ALUMNO SE ESCRIBE EN UNA LINEA DEL ARCHIVO
#SE CUENTA LA CANTIDAD DE LINEAS DEL ARCHIVO
#RETORNA UN VALOR ENTERO QUE REPRESENTA LA CANTIDAD DE ALUMNOS EN EL ARCHIVO

    archivo = open (NOMBRE_ARCHIVO, 'r')
	
    cont = 0
    for lineas in archivo:
        cont = cont + 1
    
    archivo.close()

    return cont


def consulta_comision(NOMBRE_ARCHIVO, nro):
#RECIBE NUMERO DE COMISION POR PARAMETRO
#RETORNA UNA LISTA DE ALUMNOS DE LA COMISION QUE RESIBE POR PARAMETRO

    lista_comision = []
    archivo = open(NOMBRE_ARCHIVO, 'r')

    for linea in archivo:
        alumno = eval(linea)
        if (alumno['comision'] == str(nro)):
            lista_comision.append(alumno)

    archivo.close()

    return lista_comision

def se_encuentra_alumno(NOMBRE_ARCHIVO, nro_dni):
#BUSCA EL DNI DE UN ALUMNO EN EL ARCHIVO
#RETORNA UN VALOR BOOLEAN INFORMANO SI EL ALUMNO SE ENCONTRO EN EL ARCHIVO

	alumno = dict()
	archivo = open(NOMBRE_ARCHIVO, 'r')
	fin = False
	encontro = False

	alumno = archivo.readline()
	while((not(fin)) and (not(encontro))):
		if(alumno):#Si no llego a EOF
			if(eval(alumno)['dni'] == nro_dni):
				encontro = True #Si encontró el alumno
			else:
				alumno = archivo.readline()# Si no encontro sigue leyendo
		else:
			fin = True
		

	archivo.close()
	return (encontro)

def calcula_promedio(lista):
#CALCULA Y RETORNA EL PROMEDIO DE UNA LISTA DE ENTEROS QUE RECIBE POR PARAMETRO

    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]

    return (suma/len(lista))



def promedio_mas_alto(NOMBRE_ARCHIVO):
#RECORRE EL ARCHIVO Y RETORNA EL PROMEDIO MAS ALTO

    maximo  = 0
    alumno = dict()
    archivo = open(NOMBRE_ARCHIVO, 'r')

    for linea in archivo:
        alumno = eval(linea)
        promedio = calcula_promedio(alumno['notas'])#PASA LA LISTA DE NOTAS POR PARAMETRO
        if (maximo < promedio):
            maximo = promedio

    archivo.close()

    return maximo

def lista_alumnos_promedio(NOMBRE_ARCHIVO, promedio):
#RETORNO UNA LISTA DE ALUMNOS CON EL PROMEDIO QUE RECIBE POR PARAMETRO

    alumnos = []
    leido = dict()
    archivo = open(NOMBRE_ARCHIVO, 'r')

    for linea in archivo:
        leido = eval(linea)
        if(calcula_promedio(leido['notas']) == promedio):
            alumnos.append(leido)
    archivo.close()

    return alumnos

def imprimir_lista(lista):
#IMPRIME UNA LISTA DE ALUMNOS QUE RECIBE POR PARAMETRO
	
	for i in range(len(lista)):
		print("\n	")
		imprimir_alumno(lista[i])


def promedio_de_un_alumno(NOMBRE_ARCHIVO, nro_dni):
#RECIBE EL DNI DE UN ALUMNO
#RETORNA EL PROMEDIO DE UN ALUMNO

	archivo = open(NOMBRE_ARCHIVO, 'r')
	alumno = dict()
	fin = False
	encontro = False
	promedio = 0
		
	alumno = archivo.readline()
	while (not fin) and (not encontro):
		if(alumno):
			if(eval(alumno)['dni'] == nro_dni):
				encontro = True
			else:
				alumno = archivo.readline()
		else:
			fin = True
		
		
        
	if(encontro):
		promedio = calcula_promedio(eval(alumno)['notas'])
	else:
		print("\n	EL ALUMNO NO SE ENCUENTRA")

	archivo.close()

	return promedio
	            
#====================================================================================    

#PROGRAMA_PRINCIPAL

import os

if (os.name == "ce" or os.name == "nt" or os.name == "dos"):
   limpiar_pantalla = "cls" #Limpiar pantalla en windows
else: limpiar_pantalla = "clear" #limpiar pantalla en linux

op2 = 1
op1 = int(menu1()) #Optiene la opción a realizar del menu 1
while (op1 != 0 and op2 != 0):
	os.system(limpiar_pantalla)
	if( op1 == 1) or ( op1 == 2):
		if ( op1 == 1):
			NOMBRE_ARCHIVO = input("\n	Ingrese nombre de archivo: ")
			archivo = open (NOMBRE_ARCHIVO, 'a') #archivo existente
		elif( op1 == 2 ):
			NOMBRE_ARCHIVO = input("\n	Ingrese nombre de archivo nuevo: ")
			archivo = open (NOMBRE_ARCHIVO, 'w') #archivo nuevo
		
		os.system(limpiar_pantalla) #Limpia la pantalla
		print("\n	NOMBRE DE ARCHIVO: ", NOMBRE_ARCHIVO) #IMPRIME EL NOMBRE DEL ARCHIVO ABIERTO
		op2 = int(menu2())  #Optiene la opción a realizar del menu 2
		while (op2 != 0 and op2 != 8):

			if( op2 == 1):
				os.system(limpiar_pantalla) #Limpia la pantalla
				print("\n	NOMBRE DE ARCHIVO: ", NOMBRE_ARCHIVO)
				cargar(NOMBRE_ARCHIVO)
				os.system(limpiar_pantalla) #Limpia la pantalla
                
			elif( op2 == 2):
				os.system(limpiar_pantalla) #Limpia la pantalla
				print("\n	NOMBRE DE ARCHIVO: ", NOMBRE_ARCHIVO)
				imprimir_archivo(NOMBRE_ARCHIVO)
				
				input("\n	presiones cualquier tecla para continuar...")
				os.system(limpiar_pantalla) #Limpia la pantalla

			elif( op2 == 3):
				os.system(limpiar_pantalla) #Limpia la pantalla
				print("\n	La cantidad de alumnos es: ", cantidad_de_alumnos(NOMBRE_ARCHIVO))
				
				input("\n	presione cualquier tecla para continuar")
				os.system(limpiar_pantalla) #Limpia la pantalla
				
			elif( op2 == 4):
				os.system(limpiar_pantalla) #Limpia la pantalla
				nro_de_comision = input("\n	Ingrese numero de comision a listar: ")
				print("\n	LISTA DE LA COMISION %s: " % nro_de_comision)
				imprimir_lista(consulta_comision(NOMBRE_ARCHIVO, nro_de_comision))
				
				input("\n	presione cualquier tecla para continuar")
				os.system(limpiar_pantalla) #Limpia la pantalla

			elif( op2 == 5):
				os.system(limpiar_pantalla) #Limpia la pantalla
				nro_dni = input("\n	Ingrese DNI del alumno a buscar: ")
				if(se_encuentra_alumno(NOMBRE_ARCHIVO, nro_dni)):
					print("\n	El alumno con DNI %s se encuentra en la lista" % nro_dni)
				else:
					print("\n	El alumno con DNI %s NO se encuentra en la lista" % nro_dni)
					
				input("\n	presione cualquier tecla para continuar")
				os.system(limpiar_pantalla) #Limpia la pantalla

			elif( op2 == 6):
				os.system(limpiar_pantalla) #Limpia la pantalla
				maximo = promedio_mas_alto(NOMBRE_ARCHIVO)
				print("\n	El promedio mas alto es: ", maximo)
				imprimir_lista(lista_alumnos_promedio(NOMBRE_ARCHIVO, maximo))
				#IMPRIME LISTA DE ALUMNOS CON PROMEDIO MAS ALTO
				input("\n	presione cualquier tecla para continuar")
				os.system(limpiar_pantalla) #Limpia la pantalla

			elif( op2 == 7):
				os.system(limpiar_pantalla) #Limpia la pantalla
				nro_dni  = input("\n	Ingrese DNI del alumno para calcular promedio: ")
				promedio = promedio_de_un_alumno(NOMBRE_ARCHIVO, nro_dni)
				print("\n	El promedio del alumno es: ", promedio)
				
				input("\n	presione cualquier tecla para continuar")
				os.system(limpiar_pantalla) #Limpia la pantalla
            
			elif( op2 != 8 ):
				os.system(limpiar_pantalla) #Limpia la pantalla
				print("\n	OPCION INCORRECTA")
				input("\n	presione cualquier tecla para continuar")
				os.system(limpiar_pantalla) #Limpia la pantalla
			
			os.system(limpiar_pantalla) #Limpia la pantalla
			print("\n	NOMBRE DE ARCHIVO: ", NOMBRE_ARCHIVO) #IMPRIME EL NOMBRE DEL ARCHIVO ABIERTO
			op2 = int(menu2())  #Optiene nuevamente la opción a realizar del menu 2

	elif (op1 != 0):
		os.system(limpiar_pantalla) #Limpia la pantalla
		print( "\n	OPCION INCORRECTA \n" )
		op1 =  int(menu1())        
		      
	if(op2 == 8):
		
		os.system(limpiar_pantalla)
		op1=int(menu1())
